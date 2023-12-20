'''
Advent of Code 
2023 day 12
my solution to task 1 & 2

solution 1 - 

solution 2 - 

'''

from functools import reduce
from queue import Queue

class Solution:

    
    def __init__(self, filename) -> None:
        self.get_data(filename)
        print(self.data)

    def get_data(self, filename):
        self.data, self.nums, self.data_lens = [], [], []
        with open(filename, 'r') as myfile:
            for line in myfile:
                line = line.strip().split(' -> ')
                self.data.append(line)



    def solution_1(self):
        lows, highs = [], []
        # TODO


        return 0


def main():
    print('TASK 1')
    sol = Solution('2023/Day_20/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1())
    sol = Solution('2023/Day_20/test_2.txt')
    print('test 2:', sol.solution_1())
    sol = Solution('2023/Day_20/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())


if __name__ == '__main__':
    main()
