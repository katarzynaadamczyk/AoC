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

    def _is_molecule_changing_to_init_molecule(self, molecule: list[str]) -> bool:
        for outcome in self.possible_outcome:
            if molecule == outcome:
                return True
        return False
    
    def change_duplicates(self, molecule: list[str]) -> tuple[int, list[str]]:
        duplicates_dict = {('Ca', 'Ca'): 'Ca', ('Ti', 'Ti'): 'Ti'}
        changes = 0
        changes_made = True
        while changes_made:
            changes_made = False
            i = 0
            while i < len(molecule):
                for tuple_, item in duplicates_dict.items():
                    tuple_len = len(tuple_)
                    tuple_list = list(tuple_)
                    if molecule[i:i+tuple_len] == tuple_list:
                        molecule = molecule[:i] + [item] + molecule[i+tuple_len:]
                        changes_made = True
                        changes += 1
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
        changes, copy_molecule = self.change_duplicates(copy_molecule)
        print(copy_molecule)
        # prepare queue
        queue = [] # (changes, act_molecule)
        seen = set() 
        heapq.heappush(queue, (changes, copy_molecule))
        seen.add(tuple(copy_molecule))
        # iterate over heap
        j = 0
        while heapq:
            j += 1
            changes, molecule = heapq.heappop(queue)
            if self._is_molecule_changing_to_init_molecule(molecule):
                return changes + 1
            for tuple_, new_molecule in self.reversed_changes_to.items():
                tuple_len = len(tuple_)
                for i in range(len(molecule)):
                    if molecule[i:i+tuple_len] == list(tuple_):
                        molecule_copy = molecule[:i] + [new_molecule] + molecule[i+tuple_len:]
                        if tuple(molecule_copy) not in seen:
                            heapq.heappush(queue, (changes + 1, molecule_copy))
                            seen.add(tuple(molecule_copy))
            if j % 2000 == 0:
                print(len(seen))
                print(molecule)
                print(len(molecule))
                print(molecule_copy)
                print(len(molecule_copy))
                print(changes)
                break
        return -1


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
    print('Solution 2:', sol.solution_2())
   


if __name__ == '__main__':
    main()
