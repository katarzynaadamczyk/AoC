'''
Advent of Code 
2015 day 12
my solution to task 1
task 1 - using re.findall find all occurencies of digits and add them
task 2 - using json module, import data from task.json and then parse it using recursion - if any value in dict is equal to red 
then ignore this dict else count all numbers

'''

import re
import json
from typing import Dict, List



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
    

class Solution_2:

    digits = r'-?\d+'

    def __init__(self, filename: str, word: str) -> None:
        self.word = word
        self.get_data(filename)

    def get_data(self, filename):
        with open(filename, 'r') as myfile:
            self.data = json.load(myfile)
    
    def parse_list(self, lst: List) -> int:
        result = 0
        for item in lst:
            if type(item) == type(1):
                result += item
                continue
            if type(item) in self.parse.keys():
                result += self.parse[type(item)](item)
        return result

    def parse_dict(self, dct: Dict) -> int:
        result = 0
        for key, item in dct.items():
            if (type(key) == type('s') and key == self.word) or (type(item) == type('s') and item == self.word):
                return 0
            if type(key) == type(1):
                result += key
            if type(item) == type(1):
                result += item
            if type(item) in self.parse.keys():
                result += self.parse[type(item)](item)
        return result 




    def solution_1(self):
        self.parse = {type([]): self.parse_list,
                      type({}): self.parse_dict}
        return self.parse[type(self.data)](self.data)
    
    


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
   
    sol = Solution_2('2015/Day_12/task.json', 'red')
    print('SOLUTION')
    print('Solution 2:', sol.solution_1())


if __name__ == '__main__':
    main()
