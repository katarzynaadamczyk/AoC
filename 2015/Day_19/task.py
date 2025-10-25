'''
Advent of Code 
2015 day 18
my solution to tasks

task 1 - brute force on tuples


'''
import time

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
        self.possible_changes = {}
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
                    self.parse_molecule(line)
    
    def parse_replacement(self, line: str):
        pass

    def parse_molecule(self, line: str):
        pass             

    @time_it
    def solution_1(self) -> int:
        '''
        get result for task 1
        '''
        result = 0
        return result


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
