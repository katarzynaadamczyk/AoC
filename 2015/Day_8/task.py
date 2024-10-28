'''
Advent of Code 
2015 day 8
my solution to task 1
1364 - too high
1344 - too low

'''
import re

class Solution:
    possible_chars = {re.escape('\\') + re.escape('\\'): 1, 
                      re.escape('\\') + r'"': 1, 
                      re.escape('\\') + r'x[0-9a-f][0-9a-f]': 3}

    possible_chars_replace = {re.escape('\\') + re.escape('\\'): 'A', 
                              re.escape('\\') + r'"': 'B', 
                              re.escape('\\') + r'x[0-9a-f][0-9a-f]': 'C'}

    def __init__(self, filename) -> None:
        self.get_data_replace(filename)

    def get_data_replace(self, filename):
        self.result = 0
        with open(filename, 'r') as myfile:
            for line in myfile:
                line = line.strip()
                self.result += len(line)
                line = line.strip('"')
                print(self.result)
                print(line)
                for char, repl in Solution.possible_chars_replace.items():
                    line = re.sub(char, repl, line)
                   ## i = line.find(char)
                   # while i > 0:
                   #     line = line.replace(char, repl)
                   #     i = line.find(char)
                print(line)
                self.result -= len(line)
                print(self.result)


    # not working for my data, working for test data
    def get_data_2(self, filename):
        self.result = 0
        with open(filename, 'r') as myfile:
            for line in myfile:
                line = line.strip()
                self.result += 2
                line = line.strip('"')
                line_res = 0
                for char, val in Solution.possible_chars.items():
                    line_res += len(re.findall(char, line))
                    self.result += (len(re.findall(char, line)) * val)
                
                print(line, line_res)


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
