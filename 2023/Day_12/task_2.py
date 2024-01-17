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

    def get_val(self, i_start, i_end, num, word):
        for i in range(i_start, i_end + 1):
            if not '.' in word[i + 1 - num:i + 1] and word[i + 1] != '#' and word[i-num] != '#':
                yield 1
            else:
                yield 0

    def get_first_available_index(self, result, num, start_index=0):
        for i, val in enumerate(result[-1][start_index:], start_index):
            if val != 0:
                return i + num + 1
        return None
    
    def get_last_available_index(self, word_len, nums, num_no):
        return word_len - len(nums[num_no + 1:]) - sum(nums[num_no + 1:])
    
    def insert_zeros(self, line, start_index, last_index):
        for _ in range(start_index, last_index):
            line.append(0)
        return line

    def get_first_line(self, row, nums):
        line = []
        # check first possibility
        line = self.insert_zeros(line, 0, nums[0] - 1)
        if '.' not in row[:nums[0]] and row[nums[0]] != '#':
            line.append(1)
        else:
            line.append(0)
        first_hash_in_row = row.find('#')
        last_index = self.get_last_available_index(len(row), nums, 0)
        if first_hash_in_row >= 0:
            last_index = min(last_index, first_hash_in_row + nums[0] - 1)
        for val in self.get_val(nums[0], last_index, nums[0], row):
            line.append(val)
        line = self.insert_zeros(line, last_index + 1, len(row))
        return line
    
    def get_middle_line(self, row, nums, num_index, result):
        min_index = self.get_first_available_index(result, nums[num_index])
        max_index = self.get_last_available_index(len(row), nums, num_index)
        min_hash_index = row[min_index:max_index + 1].find('#')
        max_hash_index = row[min_index:max_index + 1].rfind('#')
       # print(result)
       # print(min_index)
       # print(max_index)
       # print(min_hash_index)
       # print(max_hash_index)
        if max_hash_index >= 0:
          #  min_index += min_hash_index
            max_index = min(max_index, min_index + max_hash_index + nums[num_index])
        line = []
        line = self.insert_zeros(line, 0, min_index)
        for i, val in enumerate(self.get_val(min_index, max_index, nums[num_index], row), min_index):
            line.append(val * sum(result[-1][:i - nums[num_index]]))
        line = self.insert_zeros(line, max_index + 1, len(row))
        return line

    def get_last_line(self, row, num, result):
        min_index = self.get_first_available_index(result, num)
        last_hash_in_row = row.rfind('#')
        if last_hash_in_row >=0:
            min_index = max(last_hash_in_row, min_index)
        line = []
        line = self.insert_zeros(line, 0, min_index)
        for i, val in enumerate(self.get_val(min_index, len(row) - 2, num, row), min_index):
            line.append(val * sum(result[-1][:i - num]))
        if row[-num - 1] != '#' and '.' not in row[-num::]:
            line.append(sum(result[-1][:-1 - num]))
        else:
            line.append(0)
        return line

    def get_possibilities_for_one_string(self, row, nums):
        print(row, nums)
        # rejecting unnecessary '.' in the string
        substrs = self.get_substr(row, len(row))
        row = '.'.join(substrs)
        
        # create table for dynamic programming
        # each row is for unique num
        # each column is data for i signs from string (i -> column index in each row) 
        # result is sum of possibilities for last line
        # I called dynamic programming table as result
        result = []
        result.append(self.get_first_line(row, nums))
        for num_no in range(1, len(nums) - 1):
            result.append(self.get_middle_line(row, nums, num_no, result))
        result.append(self.get_last_line(row, nums[-1], result))
        print(result)
        return sum(result[-1])
    


    def solution_1(self):
        results = []
        for row, nums in zip(self.data, self.nums):
            results.append(self.get_possibilities_for_one_string(row, nums))
            
            print(row, results[-1])
        
        return sum(results)

    def solution_2(self):
        results = []
        for row, nums in zip(self.data, self.nums):
            act_row = '?'.join([row] * 5)
            nums = nums * 5
            results.append(self.get_possibilities_for_one_string(act_row, nums))
            
            print(row, results[-1])
        
        return sum(results)

def main():
    print('TASK 1')
    sol = Solution('2023/Day_12/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1())
   # print('test 1:', sol.solution_2())
    sol = Solution('2023/Day_12/test_2.txt')
    print('test 2:', sol.solution_1())
   # print('test 2:', sol.solution_2())
    sol = Solution('2023/Day_12/test_3.txt')
    print('test 3:', sol.solution_1())
    #sol = Solution('2023/Day_12/task.txt')
   # print('SOLUTION')
  #  print('Solution 1:', sol.solution_1(), '? 6949')
   # print('Solution 1:', sol.solution_2())


if __name__ == '__main__':
    main()
