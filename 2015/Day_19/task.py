'''
Advent of Code 
2015 day 18
my solution to tasks

task 1 - brute force on tuples


'''
import time
from collections import defaultdict

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
        print(self.possible_molecules)
        print(self.possible_changes)
        for i, molecule in enumerate(self.molecule):
            for values in self.possible_changes[molecule]:
                result.add(tuple(self.molecule[:i] + values + self.molecule[i+1:]))
        return len(result)


    @time_it
    def solution_2(self) -> int:
        '''
        get result for task 2
        '''
        result = 0
        return result


def main():
    print('TEST 1')
    sol = Solution('2015/Day_19/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 4')
   # print('test 2:', sol.solution_2(5), 'should equal 17')
    print('SOLUTION')
    sol = Solution('2015/Day_19/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
  #  print('Solution 2:', sol.solution_2(100))
   


if __name__ == '__main__':
    main()
