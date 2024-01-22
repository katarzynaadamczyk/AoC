'''
Advent of Code 
2023 day 12
my solution to task 1 & 2

working solution with all commented code removed

solution 1 - Each line is solved with use of dynamic programming. I use 2D table -> rows are for numbers (lengths of groups of damaged springs -> '#' hash),
columns are possibilities for each line in given index of the string. Before getting to the table I shorten the line by removing unnecessary operational
springs ('.' -  dots). Then create first line of our table by putting 1 to every possible place for the end of first group of #. Then middle lines:
check when they may start by finding first index with non-zero value in previous line, add actual num value to it. Then find last possible index - 
len(row) - sum(nums[num_index+1:]) - len(nums[num_index+1:]). Then check surrounding dots and add the difference to min_index and max_index.
Then put 0 to line[:min_index]. Then calculate possibilities for each index in range(min_index, max_index + 1). Add to table sum of values from previous
line starting from last previous hash index to actual_index - actual_num. 
Then calculate similarily for last line with remembering to have last hash in the result.
Result for line is sum of values in last line.
Result for whole task is sum of results for each line.


solution 2 - works same as solution 1, with the difference that for each line I firstly join with '.' [line] * 5. Then it is all the same as solution 1.

'''

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
        return word_len - len(nums[num_no + 1:]) - sum(nums[num_no + 1:]) - 1
    
    def insert_zeros(self, line, start_index, last_index):
        for _ in range(start_index, last_index):
            line.append(0)
        return line
    
    def calculate_sum_index(self, row, min_index, num, sum_index):
        hash_index = row[:min_index - num + 1].rfind('#')
        if hash_index > 0:
            sum_index = hash_index
        return sum_index
    
    def calculate_last_position(self, row, num, nums):
        row_len = len(row)
        if row[-1] == '#' or not '.' in row[row_len - num:row_len] and row[row_len - 1 - num] != '#': # TODO !!!
            return 0
        for i in range(row_len - 2, sum(nums[:-1]) + len(nums[:-1]), -1):
            if not '.' in row[i + 1 - num:i + 1] and row[i + 1] != '#' and row[i-num] != '#':
                return row_len - 1 - i
        return 0

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
        max_index = self.get_last_available_index(len(row), nums, num_index) - self.last_pos
        sum_index = max(min_index - nums[num_index] - 1, 0)
        sum_index = self.calculate_sum_index(row, min_index, nums[num_index], sum_index)
        
        max_last_dot = row[:max_index+1].rfind('.')
        
        if max_last_dot >= 0 and max_index - max_last_dot < nums[num_index]:
            max_index = max_last_dot - 1
        min_last_dot = row[:min_index+1].rfind('.')
        if min_last_dot >=0 and min_index - min_last_dot < nums[num_index]:
            min_index = min_last_dot + nums[num_index]
        if max_index < min_index:
            min_index = max_index
        
        line = []
        line = self.insert_zeros(line, 0, min_index)
        for i, val in enumerate(self.get_val(min_index, max_index, nums[num_index], row), min_index):
            sum_index = self.calculate_sum_index(row, i, nums[num_index], sum_index)
            line.append(val * sum(result[-1][sum_index:i - nums[num_index]])) 
        line = self.insert_zeros(line, max_index + 1, len(row))
        return line

    def get_last_line(self, row, num, result):
        min_index = self.get_first_available_index(result, num)
        sum_index = self.calculate_sum_index(row, min_index, num, min_index - num - 1)
        
        last_hash_in_row = row.rfind('#')
        if last_hash_in_row >=0:
            min_index = max(last_hash_in_row, min_index)
        line = []
        line = self.insert_zeros(line, 0, min_index)
        for i, val in enumerate(self.get_val(min_index, len(row) - 2, num, row), min_index):
            sum_index = self.calculate_sum_index(row, i, num, sum_index)
            line.append(val * sum(result[-1][sum_index:i - num]))
        if row[-num - 1] != '#' and '.' not in row[-num::]:
            sum_index = self.calculate_sum_index(row, len(row) - 1, num, sum_index)
            line.append(sum(result[-1][sum_index:-1 - num]))
        else:
            line.append(0)
        return line

    def get_possibilities_for_one_string(self, row, nums):
       # print(row, nums)
        # rejecting unnecessary '.' in the string
        substrs = self.get_substr(row, len(row))
        row = '.'.join(substrs)
        
        self.last_pos = self.calculate_last_position(row, nums[-1], nums)
        
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
        #print(result)
        return sum(result[-1])
    


    def solution_1(self):
        results = []
        for row, nums in zip(self.data, self.nums):
            results.append(self.get_possibilities_for_one_string(row, nums))
            
            #print(row, results[-1])
        return sum(results)

    def solution_2(self):
        results = []
        for row, nums in zip(self.data, self.nums):
            act_row = '?'.join([row] * 5)
            nums = nums * 5
            results.append(self.get_possibilities_for_one_string(act_row, nums))
            
          #  print(row, results[-1])
        
        return sum(results)

def main():
    results = []
    true_results = [21, 525152, 16, 2, 23, 4, 7, 2]
    print('TASK 1')
    sol = Solution('2023/Day_12/test.txt')
    print('TEST 1')
    results.append(sol.solution_1())
    results.append(sol.solution_2())
    sol = Solution('2023/Day_12/test_2.txt')
    results.append(sol.solution_1())
    sol = Solution('2023/Day_12/test_3.txt')
    results.append(sol.solution_1())
    sol = Solution('2023/Day_12/test_4.txt')
    results.append(sol.solution_1())
    sol = Solution('2023/Day_12/test_5.txt')
    results.append(sol.solution_1())
    sol = Solution('2023/Day_12/test_7.txt')
    results.append(sol.solution_1())
    sol = Solution('2023/Day_12/test_8.txt')
    results.append(sol.solution_1())
    for x, y in zip(results, true_results):
        print(x, '?', y)
    sol = Solution('2023/Day_12/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1(), '? 6949')
    results.append(sol.solution_1())
    print('Solution 2:', sol.solution_2(), '? 51456609952403')


if __name__ == '__main__':
    main()
