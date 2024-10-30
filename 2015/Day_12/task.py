'''
Advent of Code 
2015 day 12
my solution to task 1
task 1 - 

'''

import re

class Solution:

    digits = r'-?\d+'

    def __init__(self, filename) -> None:
        self.numbers = []
        self.get_data(filename)

    def get_data(self, filename):
        with open(filename, 'r') as myfile:
            for line in myfile:
                line = line.strip()
                self.numbers += [int(x) for x in re.findall(Solution.digits, line)]

    def solution_1(self):
        return sum(self.numbers)
    
    


def main():
    print('TASK 1')
    sol = Solution('2015/Day_12/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 18')
  #  print('test 1:', sol.solution_2())
    sol = Solution('2015/Day_12/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
   # print('Solution 2:', sol.solution_2())


if __name__ == '__main__':
    main()
