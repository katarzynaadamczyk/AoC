'''
Advent of Code 
2024 day 2
my solution to tasks
task 1 - create a table of report[i+ 1] - report[i], count min and max value and check if these values are in (1, 3) or (-3, -1) scope,
if so report is valid
task 2 - remove one level from report and perform check as in task 1, if it passes, report is valid


'''
import re
from functools import reduce

class Solution:

    def __init__(self, filename) -> None:
        self.commands = []
        self.get_data(filename)

    def get_data(self, filename):
        with open(filename, 'r') as myfile:
            for line in myfile:
                self.commands.append(re.findall(r'mul\(\d{1,3},\d{1,3}\)', line.strip())) # (\d{1-3},\d{1-3})'


    def solution_1(self) -> int:
        result = 0
        for line in self.commands:
            for chunk in line:
                result += reduce(lambda a, b: a * b, [int(x) for x in re.findall(r'\d{1,3}', chunk)])
        return result
    
    
    
    

def main():

    print('TASK 1')
    sol = Solution('2024/Day_3/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 161')
  #  print('test 1:', sol.solution_2(), 'should equal 4')
    sol = Solution('2024/Day_3/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
  #  print('Solution 2:', sol.solution_2())
   


if __name__ == '__main__':
    main()
