'''
Advent of Code 
2015 day 18
my solution to tasks

task 1 - brute force on lists & tuples (for adding to set and counting the number of distinct tuples)
task 2 -> reverse engineering:
            1. create a dict of tuples changing to unique molecule
            2. loop over molecule to find all possible changes and change them to single molecule until len(molecule) == 1 && molecule == init_molecule (e)
            3. return value of changes made in such a way
    
'''
import time
from collections import defaultdict
from copy import copy
import heapq

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        print(f'time taken by {func.__name__} is {round(time.time()-start, 4)}')

        return result
    return wrapper


class Solution:
    def __init__(self, filename) -> None:
        '''
        initialize Solution
        '''
        self.possible_changes = defaultdict(list)
        self.possible_molecules = set()
        self.molecule = []
        self.filename = filename
        self.blockings = ("Rn", "Y", "Ar")
        self.get_data(filename)

    def get_data(self, filename):
        '''
        parse data
        '''
        with open(filename, 'r') as my_file:
            _is_found_empty_line = False
            for line in my_file:
                line = line.strip()
                if line == "":
                    _is_found_empty_line = True
                    continue
                if not _is_found_empty_line:
                    self.parse_replacement(line)
                else:
                    self.divide_possible_molecules()
                    self.molecule = self.parse_molecule(line)
    
    def parse_replacement(self, line: str):
        """ Parse line X => XX """
        molecule, changes_to = [x.strip() for x in line.split("=>")]
        self.possible_changes[molecule].append(changes_to)
        self.possible_molecules.add(molecule)

    def divide_possible_molecules(self):
        """ Divides all possible molecules into list of single molecules """
        new_possible_changes_dict = defaultdict(list)
        for key, value_list in self.possible_changes.items():
            for new_molecule in value_list:
                new_possible_changes_dict[key].append(self.parse_molecule(new_molecule))
        del self.possible_changes
        self.possible_changes = new_possible_changes_dict

    def parse_molecule(self, line: str) -> list[str]:
        """ change string with complicated molecule into list of strings for single molecules """
        line = line.strip()
        result = []
        while line:
            if line[:2] in self.possible_molecules:
                result.append(line[:2])
                line = line[2:]
            elif line[:1] in self.possible_molecules:
                result.append(line[:1])
                line = line[1:]
            elif line[:1]:
                if line[1:2] in self.possible_molecules or line[1:3] in self.possible_molecules:
                    self.possible_molecules.add(line[:1])
                    result.append(line[:1])
                    line = line[1:]
                else:
                    self.possible_molecules.add(line[:2])
                    result.append(line[:2])
                    line = line[2:]
        return result
            

    @time_it
    def solution_1(self) -> int:
        '''
        get result for task 1
        '''
        result = set()
        for i, molecule in enumerate(self.molecule):
            for values in self.possible_changes[molecule]:
                result.add(tuple(self.molecule[:i] + values + self.molecule[i+1:]))
        return len(result)
    
    def reverse_dict(self, init_molecule: str) -> dict[tuple[str, ...], str]:
        self.reversed_changes_to = {}
        for key, values in self.possible_changes.items():
            if key == init_molecule:
                self.possible_outcome = values
                continue
            for value in values:
                self.reversed_changes_to[tuple(value)] = key
        return self.reversed_changes_to
    
    def reverse_dict_2(self, init_molecule: str) -> dict[str, str]:
        self.reversed_changes_to = {}
        for key, values in self.possible_changes.items():
            if key == init_molecule:
                self.possible_outcome = set(["".join(value) for value in values])
                continue
            for value in values:
                self.reversed_changes_to["".join(value)] = key
        return self.reversed_changes_to 

    def _is_molecule_changing_to_init_molecule(self, molecule: list[str]) -> bool:
        for outcome in self.possible_outcome:
            if molecule == outcome:
                return True
        return False
    
    def change_duplicates(self, molecule: list[str]) -> tuple[int, list[str]]:
        duplicates_dict = {('Ca', 'Ca'): 'Ca', ('Ti', 'Ti'): 'Ti', ("Si", "Th"): "Ca", ("Th", "Ca"): "Th"}
        changes = 0
        changes_made = True
        while changes_made:
            i = 0
            while i < len(molecule):
                changes_made = False
                for tuple_, item in duplicates_dict.items():
                    tuple_len = len(tuple_)
                    tuple_list = list(tuple_)
                    if molecule[i:i+tuple_len] == tuple_list:
                        molecule = molecule[:i] + [item] + molecule[i+tuple_len:]
                        changes_made = True
                        changes += 1
                        break
                if not changes_made:
                    i += 1
        return changes, molecule

    

    @time_it
    def solution_2(self, init_molecule: str = 'e') -> int:
        '''
        get result for task 2
        '''
        # prepare dict
        self.reverse_dict(init_molecule)
        # change CaCa to Ca and TiTi to Ti
        copy_molecule = copy(self.molecule)
        print(len(copy_molecule))
        changes, copy_molecule = self.change_duplicates(copy_molecule)
        print(copy_molecule)
        print(len(copy_molecule))
        print(f"changes: {changes}")
        # prepare queue
        queue = [] # (changes, act_molecule)
        heapq.heapify(queue)
        seen = set() 
        heapq.heappush(queue, (-1 * changes, len(copy_molecule), copy_molecule))
        seen.add(tuple(copy_molecule))
        # iterate over heap
        j = 0
        results = []
        while queue:
            j += 1
            changes, _, molecule = heapq.heappop(queue)
            changes *= -1
            if self._is_molecule_changing_to_init_molecule(molecule):
                print(molecule)
                results.append(changes + 1)
                if len(results) > 5:
                    break
            for tuple_, new_molecule in self.reversed_changes_to.items():
                tuple_len = len(tuple_)
                for i in range(len(molecule)):
                    if molecule[i:i+tuple_len] == list(tuple_):
                        molecule_copy = molecule[:i] + [new_molecule] + molecule[i+tuple_len:]
                        new_changes, molecule_copy = self.change_duplicates(molecule_copy)
                        if tuple(molecule_copy) not in seen:
                            heapq.heappush(queue, (-1 * changes - new_changes - 1, len(molecule_copy), molecule_copy))
                            seen.add(tuple(molecule_copy))
            if j % 2000 == 0:
                print(f"seen {len(seen)}, molecule: {len(molecule)}, changes so far: {changes}, j: {j}")
                print([a[0] for a in heapq.nsmallest(10, queue)])
                print(molecule_copy)
        return min(results) if results else -1
    
    def find_next_stop(self, index_start: int = 0) -> int:
        new_indexes = [self.molecule.index(x, index_start + 1) for x in self.blockings if x in self.molecule[index_start+1:]]
        return min(new_indexes) if new_indexes else -1

    def shorten_molecule(self, index_start: int, index_end: int) -> int:
        changes = 0
        molecule = copy(self.molecule[index_start:index_end])
        print(molecule)
        while len(molecule) >= 2:
          #  print(molecule[:2], self.reversed_changes_to[tuple(molecule[:2])])
            molecule = [self.reversed_changes_to[tuple(molecule[:2])]] + molecule[2:]
            changes += 1
        print(molecule)
        self.molecule = self.molecule[:index_start] + molecule + self.molecule[index_end:]
        return changes

    def solution_2_2(self):
        """
        After read some articles on Reddit. 
        Replace "Rn" with "(", Y with "," and Ar with ")"
        """
        self.reverse_dict("e")
        print(self.possible_outcome)
        print(self.reversed_changes_to)
        print(self.molecule)
        index_start = 0
        index_end = self.find_next_stop(index_start)
        result = 0
      #  while index_start >= 0:
          #  print(index_start)
      #      index_end = self.find_next_stop(index_start)
            # result += self.shorten_molecule(index_start + 1, index_end)
      #      index_start = self.find_next_stop(index_start)
            #print("".join(self.molecule))
        molecule = "".join(self.molecule)
        molecule = molecule.replace("Rn", '(').replace("Y", ',').replace("Ar", ')')
        print(molecule)
        return result
    
    def solution_2_3(self):
        """
        found on reddit:
        equation: number of molecules - # Rn - # Ar - 2 * # Y - 1
        """
        return len(self.molecule) - self.molecule.count("Rn") - self.molecule.count("Ar") - 2 * self.molecule.count("Y") - 1


def main():
    print('TEST 1')
    sol = Solution('2015/Day_19/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 4')
    print('TEST 2')
    sol = Solution('2015/Day_19/test_2.txt')
    print('TEST 2')
    print('test 2:', sol.solution_2(), 'should equal 6')
    print('SOLUTION')
    sol = Solution('2015/Day_19/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2_3())
   


if __name__ == '__main__':
    main()
