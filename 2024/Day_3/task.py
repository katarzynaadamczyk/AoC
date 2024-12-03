'''
Advent of Code 
2024 day 3
my solution to tasks
task 1 - find all valid chunks of code using re.findall method, then in each chunk find numbers and multiply them
task 2 - use a flag to keep the information if we should add result of next mul or not - 
important: even though the task file is in few line we must keep the flag continously between lines 
that is why it is not reset in each iteration 


'''
import re
from functools import reduce

class Solution:

    def __init__(self, filename) -> None:
        self.mul_commands = []
        self.commands = []
        self.get_data(filename)

    def get_data(self, filename):
        with open(filename, 'r') as myfile:
            for line in myfile:
                self.commands.append(line.strip())
                self.mul_commands.append(re.findall(r'mul\(\d{1,3},\d{1,3}\)', line.strip())) 
   
    def get_chunk_result(self, chunk):
        return reduce(lambda a, b: a * b, [int(x) for x in re.findall(r'\d{1,3}', chunk)])

    def get_line_result(self, chunks):
        return sum([self.get_chunk_result(chunk) for chunk in chunks])

    def solution_1(self) -> int:
        result = 0
        for line in self.mul_commands:
            result += self.get_line_result(line)
        return result

    
    def solution_2(self) -> int:
        result = 0
        flag = True
        for line in self.commands:
            for chunk in re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line):
                if chunk == 'do()':
                    flag = True
                elif chunk == "don't()":
                    flag = False
                else:
                    if flag:
                        result += self.get_chunk_result(chunk)

            
        return result
    
    
    

def main():

    print('TASK 1')
    sol = Solution('2024/Day_3/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 161')
    print('test 1:', sol.solution_2(), 'should equal 48')
    sol = Solution('2024/Day_3/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2()) 
   


if __name__ == '__main__':
    main()
