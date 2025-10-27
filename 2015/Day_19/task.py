'''
Advent of Code 
2015 day 18
my solution to tasks

task 1 - brute force on lists & tuples (for adding to set and counting the number of distinct tuples)
task 2 - using memoization (seen_molecules) and heapq as priority queue (instead of PriorityQueue from queue module) -> need to re-think this idea
task 2 -> better solution: reverse engineering
create a dict of tuples changing to unique molecule

loop over molecule and change what suits 
    molecule_copy = copy(molecule)
    changes = 0
    i = 0
    while i < len(molecule_copy):
        if len(molecule_copy) == 1:
            break
        for tuple_, new_molecule in tuple_to_molecule_dict.items():
            tuple_len = len(tuple_)
            if molecule_copy[i:i+tuple_len] == tuple:
                changes += 1
                molecule_copy = molecule_copy[:i] + [new_molecule] + molecule_copy[i+tuple_len:]
                break
    
'''
import time
from collections import defaultdict
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
    
    def check_compatibility(self, new_molecules: list[str], common_number: int = 0) -> int:
        result = common_number
        for a, b in zip(new_molecules, self.molecule):
            if a != b:
                break
            result += 1
        return result


    @time_it
    def solution_2(self, init_molecule: str = 'e') -> int:
        '''
        get result for task 2
        '''
        # prepare heap
        queue = []
        seen_molecules = set()
        for molecule in self.possible_changes.get(init_molecule, []):
            common_number = self.check_compatibility(molecule)
            heapq.heappush(queue, (1, -1 * common_number, molecule))
            seen_molecules.add(tuple(molecule))
        # get len of desired molecule
        final_len = len(self.molecule)
        # run queue
        index = 0
        while queue:
            result, common_number, molecules = heapq.heappop(queue)
            print(common_number, result, molecules)
            common_number *= -1
            if len(molecules) > final_len:
                continue
            if common_number == final_len:
                return result
            for i, molecule in enumerate(molecules[common_number-1], start=common_number-1):
                for values in self.possible_changes[molecule]:
                    new_molecules = molecules[:i] + values + molecules[i+1:]
                    new_molecules_tuple = tuple(new_molecules)
                    if new_molecules_tuple in seen_molecules:
                        continue
                    seen_molecules.add(new_molecules_tuple)
                    common_number = self.check_compatibility(new_molecules)
                    heapq.heappush(queue, (result + 1, -1 * common_number,  new_molecules))
            index += 1
            if index > 100:
                break
        print(len(seen_molecules))
        print(len(queue))
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
