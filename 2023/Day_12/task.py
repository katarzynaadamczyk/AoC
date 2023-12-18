'''
Advent of Code 
2023 day 12
my solution to task 1 & 2

solution 1 - 

solution 2 - 

'''

from functools import reduce


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
        print(substrs)
        return substrs


    def get_possibilities_for_one_substr(self, substr, num):
        print(substr, num)
        substr_len = len(substr)
        if substr_len < num or substr.count('#') > num:
            return 0
        if substr_len == num:
            return 1
        if substr.count('#') == 0:
            return substr_len - num + 1
        i_min = substr.find('#')
        i_max = substr.rfind('#')
        return min([i_min, substr_len - 1 - i_max, num - (i_max - i_min + 1)]) + 1
    

    def get_possible_substr_divisions(self, substrs, num):
        results = []
        for substr in substrs:
            if substr.count('#') == len(substr):
                results.append([substr])
                continue
            tmp = []
            for i in range(1, len(substr) - 1):
                if substr[i] == '?':
                    tmp.append([substr[:i], substr[i+1:]])
            results.append(tmp)
        print(results)
        return []


    def get_possibilities_for_few_nums(self, substrs, nums):
        self.get_possible_substr_divisions(substrs, 2)
        return sum([])
    

    def get_result_for_ideal_match(self, substrs, nums):
        return reduce(lambda x, y: x * y, [self.get_possibilities_for_one_substr(substr, num) for num, substr in zip(nums, substrs)])


    def solution_1(self):
        results = []
        for i, (row, row_len, nums) in enumerate(zip(self.data, self.data_lens, self.nums)):
            act_substrs = self.get_substr(row, row_len)
            if len(act_substrs) == len(nums):
                results.append(self.get_result_for_ideal_match(act_substrs, nums))
            else:
                results.append(self.get_possibilities_for_few_nums(act_substrs, nums))
            
            print(i, results[-1])
        
        return sum(results)


def main():
    print('TASK 1')
    sol = Solution('2023/Day_12/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1())
   # sol = Solution('2023/Day_12/task.txt')
   # print('SOLUTION')
   # print('Solution 1:', sol.solution_1())


if __name__ == '__main__':
    main()
