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

    def get_data(self, filename):
        self.data, self.nums, self.data_lens = [], [], []
        with open(filename, 'r') as myfile:
            for line in myfile:
                line = line.strip().split()
                self.data.append(line[0])
                self.data_lens.append(len(self.data[-1]))
                self.nums.append([int(x) for x in line[1].split(',')])

    def get_substr(self, row, row_len):
        act_min_i, act_i = 0, 0
        substrs = []
        while act_i < row_len:
            while act_i < row_len and row[act_i] in '?#':
                act_i += 1
            if act_i != act_min_i:
                substrs.append(row[act_min_i:act_i])
            act_i += 1
            act_min_i = act_i
        return substrs

    def get_first_line(self, row, nums):
        pass

    def get_possibilities_for_few_nums(self, row, nums):
        # rejecting unnecessary '.' in the string
        substrs = self.get_substr(row, len(row))
        row = '.'.join(substrs)

        # create table for dynamic programming
        # each row is for unique num
        # each column is data for cumulative i + 1 signs from string (i -> column index in each row) 
        result = []

        return result
    


    def solution_1(self):
        results = []
        for row, nums in zip(self.data, self.nums):
            results.append(self.get_possibilities_for_few_nums(row, nums))
            
            print(row, results[-1])
        
        return sum(results)

    def solution_2(self):
        results = []
        for row, nums in zip(self.data, self.nums):
            act_row = '?'.join([row] * 5)
            nums = nums * 5
            results.append(self.get_possibilities_for_few_nums(act_row, nums))
            
            print(row, results[-1])
        
        return sum(results)

def main():
    print('TASK 1')
    sol = Solution('2023/Day_12/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1())
    print('test 1:', sol.solution_2())
    sol = Solution('2023/Day_12/test_2.txt')
    print('test 2:', sol.solution_1())
    print('test 2:', sol.solution_2())
   # sol = Solution('2023/Day_12/task.txt')
    #print('SOLUTION')
   # print('Solution 1:', sol.solution_1(), '? 6949')
   # print('Solution 1:', sol.solution_2())


if __name__ == '__main__':
    main()
