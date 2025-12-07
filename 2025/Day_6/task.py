'''
Advent of Code 
2025 day 6
my solution to tasks 

task 1 - simple string splitting and then taking correct values to be reduced to a single answer
task 2 - more complex input parsing - having input as list of strings, then split to get numbers by finding indexes of operations to be performed

'''
import time
from functools import reduce


def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        print(f'time taken by {func.__name__} is {round(time.time()-start, 4)}')

        return result
    return wrapper


class Solution:
    OPERATIONS = {'+': lambda a, b: a + b,
                  '*': lambda a, b: a * b}
    
    def __init__(self, filename: str) -> None:
        '''
        initialize Solution
        '''
        self.data, self.operations = self.get_data(filename)
        self.filename = filename

    def get_data(self, filename) -> tuple[list[list[str]], list[str]]:
        '''
        parse data
        '''
        result = []
        with open(filename, 'r') as my_file:
            for line in my_file:
                result.append(line.strip().split())
        return result[:-1], result[-1]

    @time_it
    def solution_1(self) -> int:
        '''
        get result for task 1
        '''
        result = 0
        for i, oper in enumerate(self.operations):
            result += reduce(self.OPERATIONS[oper], (int(line[i]) for line in self.data))
        
        return result
    
    def get_data_2(self):
        result = []
        with open(self.filename, 'r') as my_file:
            for line in my_file:
                result.append(line.strip('\n'))
        return result[:-1], result[-1]

    @staticmethod
    def _get_next_oper_index(line: str, str_index: int) -> int:
        new_indexes = [line.find(x, str_index) for x in Solution.OPERATIONS.keys()]
        if len(set(new_indexes)) == 1 and -1 in new_indexes:
            return -1
        if -1 in new_indexes:
            return max(new_indexes)
        return min(new_indexes)
    
    def _get_act_result(self, act_index: int, next_index: int, numbers: list[str], oper: str) -> int:
        nums = []
        for i in range(act_index, next_index):
            nums.append(int("".join(numbers[j][i] for j in range(len(numbers))).strip()))
        return reduce(self.OPERATIONS[oper], nums)

    @time_it
    def solution_2(self) -> int:
        '''
        get result for task 2
        '''
        numbers, operations = self.get_data_2()
        act_index = 0
        oper = operations[act_index]
        result = 0
        next_index = self._get_next_oper_index(operations, act_index + 1)
        while next_index != -1:
            result += self._get_act_result(act_index, next_index - 1, numbers, oper)
            act_index = next_index
            oper = operations[act_index]
            next_index = self._get_next_oper_index(operations, act_index + 1)
        result += self._get_act_result(act_index, len(numbers[0]), numbers, oper)

        return result


def main():
    print('TEST 1')
    sol = Solution('2025/Day_6/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 4277556')
    print('test 2:', sol.solution_2(), 'should equal 3263827')
    print('SOLUTION')
    sol = Solution('2025/Day_6/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2())
   


if __name__ == '__main__':
    main()
