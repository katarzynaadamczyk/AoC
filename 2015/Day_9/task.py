'''
Advent of Code 
2015 day 9
my solution to task 1
task 1 - 

'''

import re


class Solution:


    def __init__(self, filename) -> None:
        self.graph = {}
        self.get_data(filename)

    def get_data(self, filename):
        with open(filename, 'r') as myfile:
            for line in myfile:
                line = re.findall(r'\w+', line)
                self.graph.setdefault(line[0], {})
                self.graph.setdefault(line[-2], {})
                self.graph[line[0]][line[-2]] = int(line[-1])
                self.graph[line[-2]][line[0]] = int(line[-1])
        print(self.graph)

    def solution_1(self):
        return 
    


def main():
    print('TASK 1')
    sol = Solution('2015/Day_9/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1())
  #  print('test 1:', sol.solution_2())
  #  sol = Solution('2015/Day_9/task.txt')
  #  print('SOLUTION')
  #  print('Solution 1:', sol.solution_1())
   # print('Solution 2:', sol.solution_2())


if __name__ == '__main__':
    main()
