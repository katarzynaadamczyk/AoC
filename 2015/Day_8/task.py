'''
Advent of Code 
2015 day 8
my solution to task 1
task 1 - replace all matches by letters - A for \ \, B for \ ", C for \ x h h, counting line lenght before and after replacement to get the result
task 2 - make counter of all characters for all lines, for each \ or " add additional \ + 2 * number of all lines 
(as first and last quote get two additional characters)

'''

import re
from collections import Counter

class Solution:

    possible_chars_replace = {re.escape('\\') + re.escape('\\'): 'A', 
                              re.escape('\\') + r'"': 'B', 
                              re.escape('\\') + r'x[0-9a-f][0-9a-f]': 'C'}

    def __init__(self, filename) -> None:
        self.chars_counter = Counter()
        self.total_lenght = 0
        self.total_lines = 0
        self.result_1 = 0
        self.get_data_replace(filename)

    def get_data_replace(self, filename):
        with open(filename, 'r') as myfile:
            for line in myfile:
                line = line.strip()
                self.total_lines += 1
                self.total_lenght += len(line)
                self.chars_counter += Counter(line)
                line = line[1:-1]
                for char, repl in Solution.possible_chars_replace.items():
                    line = re.sub(char, repl, line)
                self.result_1 -= len(line)

    def solution_1(self):
        return self.total_lenght + self.result_1
    
    def solution_2(self):
        return self.total_lines * 2 + self.chars_counter['\\'] + self.chars_counter['"']
    


def main():
    print('TASK 1')
    sol = Solution('2015/Day_8/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1())
    print('test 1:', sol.solution_2())
    sol = Solution('2015/Day_8/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2())


if __name__ == '__main__':
    main()
