'''
Advent of Code 
2025 day 2
my solution to tasks

task 1 - check all possible halves by for each of even numbers in ranges
task 2 - check all possible combinations of sequences (with additional for for sequence length)


'''
from typing import Generator
import time


def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        print(f'time taken by {func.__name__} is {round(time.time()-start, 4)}')

        return result
    return wrapper


class Solution:
    def __init__(self, filename: str) -> None:
        '''
        initialize Solution
        '''
        self.filename = filename

    def get_data(self) -> Generator[tuple[str, str], None, None]:
        '''
        parse data
        '''
        with open(self.filename, 'r') as my_file:
            contents = my_file.read().strip()
        for _range in contents.split(','):
            x_min, x_max = _range.split('-')
            yield x_min, x_max
    
    @staticmethod
    def _get_act_half_and_value(act_half: str) -> tuple[str, int]:
        act_half = str(int(act_half) + 1)
        act_value = int(act_half * 2)
        return act_half, act_value

    @time_it
    def solution_1(self) -> int:
        '''
        get result for task 1
        '''
        results = set()
        for x_min, x_max in self.get_data():
            if len(x_min) % 2 == 0:
                act_half = x_min[:len(x_min) // 2]
            elif len(x_max) % 2 == 0:
                act_half = '1' + '0' * (len(x_min) // 2)
            else: 
                continue
        
            act_value = int(act_half * 2)
            act_min, act_max = int(x_min), int(x_max)
            while act_value <= act_max:
                if act_value >= act_min:
                    results.add(act_value)
                act_half, act_value = self._get_act_half_and_value(act_half)

        return sum(results)
    
    @staticmethod
    def _get_result_for_one_multiplier(multiplier: int, sequence: str, x_min: str, x_max: str) -> int:
        results = set()
        act_value = int(sequence * multiplier)
        act_min, act_max = int(x_min), int(x_max)
        while act_value <= act_max:
            if act_value >= act_min:
                results.add(act_value)
            sequence = str(int(sequence) + 1)
            act_value = int(sequence * multiplier)
        return results


    @time_it
    def solution_2(self) -> int:
        '''
        get result for task 2
        '''
        results = set()
        for x_min, x_max in self.get_data():
            for chars_num in range(1, len(x_max) // 2 + 1):
                sequence = '1' + '0' * (chars_num - 1)
                min_multiplier, max_multiplier = len(x_min) // chars_num, len(x_max) // chars_num
                if len(x_min) % chars_num == 0 and min_multiplier > 1:
                    results = results.union(self._get_result_for_one_multiplier(min_multiplier, sequence, x_min, x_max))
                if len(x_max) % chars_num == 0 and len(x_max) != len(x_min) and max_multiplier > 1:
                    results = results.union(self._get_result_for_one_multiplier(max_multiplier, sequence, x_min, x_max))
        

        return sum((int(x) for x in results))


def main():
    print('TEST 1')
    sol = Solution('2025/Day_2/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 1227775554')
    print('test 2:', sol.solution_2(), 'should equal 4174379265')
    print('SOLUTION')
    sol = Solution('2025/Day_2/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2())
   


if __name__ == '__main__':
    main()
