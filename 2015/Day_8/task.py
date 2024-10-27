'''
Advent of Code 
2015 day 8
my solution to task 1


'''
import re

class Solution:
    possible_chars = (r'\\', r'\"', r'\x\w\w')
    def __init__(self, filename) -> None:
        self.get_data(filename)

    def get_data(self, filename):
        self.result = 0
        with open(filename, 'r') as myfile:
            for line in myfile:
                line = line.strip()
                self.result += len(line)
                line.strip('"')
                

    def solution_1(self):
        return self.result
    


def main():
    print('TASK 1')
    sol = Solution('2015/Day_8/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1())
    sol = Solution('2015/Day_8/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())


if __name__ == '__main__':
    main()
