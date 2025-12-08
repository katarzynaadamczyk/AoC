'''
Advent of Code 
2025 day 3
my solution to tasks

task 1 - find max char in s[:-1] and then max char s[min_index_for_first_char]
task 2 - (watched a video on reddit as I was stuck on this one) iterate through each bank and while current number is higher that previous one(s), delete all that are lower \
    (but bear in mind the length of the number to get) and then if length of the actual result is less than 12 add current number to actual result

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
            act_result = []
            for i, num in enumerate(bank[:]):
                while act_result and act_result[-1] < num and bank_len - i > 12 - len(act_result):
                    act_result.pop()
                if len(act_result) < 12:
                    act_result.append(num)

            result += int("".join(act_result))

        return result


def main():
    print('TEST 1')
    sol = Solution('2025/Day_3/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 357')
    print('test 2:', sol.solution_2(), 'should equal 3121910778619')
    print('SOLUTION')
    sol = Solution('2025/Day_3/test_2.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1(), 'should equal 88')
    print('Solution 2:', sol.solution_2(), 'should equal 888822615742')
    sol = Solution('2025/Day_3/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2())
   


if __name__ == '__main__':
    main()
