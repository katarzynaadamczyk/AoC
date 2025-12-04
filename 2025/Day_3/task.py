'''
Advent of Code 
2025 day 3
my solution to tasks

task 1 - 
task 2 - 


'''
from typing import Generator
from collections import defaultdict
import time


def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        print(f'time taken by {func.__name__} is {round(time.time()-start, 4)}')

        return result
    return wrapper

nums = '9876543210'

class Solution:
    def __init__(self, filename: str) -> None:
        '''
        initialize Solution
        '''
        self.filename = filename

    def get_data(self) -> Generator[str, None, None]:
        '''
        parse data
        '''
        with open(self.filename, 'r') as my_file:
            contents = my_file.read().strip()
        for bank in contents.split():
            yield bank
    

    @time_it
    def solution_1(self) -> int:
        '''
        get result for task 1
        '''
        result = 0
        for bank in self.get_data():
            max_value_1 = max(set(bank[:-1]))
            max_value_2 = max(set(bank[bank.index(max_value_1) + 1:]))
            result += int(max_value_1 + max_value_2)

        return result


    @time_it
    def solution_2(self) -> int:
        '''
        get result for task 2
        '''
        result = 0
        for bank in self.get_data():
            bank_len = len(bank)
            bank_dict = defaultdict(list)
            for i, num in enumerate(bank):
                bank_dict[num].append(i)
            i_result = []
            for num in nums:
                if not i_result:
                    i_result += bank_dict[num][:12]
                elif bank_len - (act_min := min(i_result)) >= 12:
                    i_result += sorted(list(x for x in bank_dict[num] if x > act_min), reverse=False)[-(12 - len(i_result)):]
                else:
                    i_result += bank_dict[num][-(12 - len(i_result)):]
                print(num)
                print(i_result)
                if len(i_result) == 12:
                    break
            print("".join(bank[i] for i in sorted(i_result)))
            print(i_result)
            result += int("".join(bank[i] for i in sorted(i_result)))
            break

        return result


def main():
    print('TEST 1')
    sol = Solution('2025/Day_3/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 357')
    print('test 2:', sol.solution_2(), 'should equal 3121910778619')
    print('SOLUTION')
    sol = Solution('2025/Day_3/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2())
   


if __name__ == '__main__':
    main()
