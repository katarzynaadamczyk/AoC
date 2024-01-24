'''
Advent of Code 
2023 day 12
my solution to task 1 

in this file there is only task 1 solved properly (I mean, it works well for task 2 too, but it is too slow to get the answer in reasonable time)

solution 1 - each line is solved with Queue approach -> in each iteration I change existing '?' to # and . and each of this possibilities add to
queue if hash count in line is less than sum(nums). If there is no '?' then check if it is a correct string. If so, add 1 to result.


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
      # print(substrs)
        return substrs


    def get_possibilities_for_one_substr(self, substr, num):
       # print(substr, num)
        substr_len = len(substr)
        if substr_len < num or substr.count('#') > num:
            return 0
        if substr_len == num:
            return 1
        if substr.count('#') == 0:
            return substr_len - num + 1
        i_min = substr.find('#')
        i_max = substr.rfind('#')
        if i_max - i_min >= num:
            return 0
       # print(min([i_min, substr_len - 1 - i_max, num - (i_max - i_min + 1)]) + 1)
        return min([i_min, substr_len - 1 - i_max, num - (i_max - i_min + 1)]) + 1 
    
    def get_possibilities_for_one_substr_NEW(self, substr, num):
        if len(substr) == num:
            return 1
        return 0



    def get_possibilities_for_few_nums(self, substrs, nums):
        result = 0
        sub_queue = Queue()
        sub_queue.put(substrs) # put substrings 
        nums_sum, nums_len = sum(nums), len(nums)
        while not sub_queue.empty():
            act_substrs = sub_queue.get()

            act_line = '.'.join(act_substrs)
            if '?' in act_line:
                act_new_i = act_line.find('?')
                # put # in place of ?
                act_line_1 = act_line[:act_new_i] + '#' + act_line[act_new_i+1:]
            #   print(act_line_1)
                if act_line_1.count('#') <= nums_sum: 
                    sub_queue.put(self.get_substr(act_line_1, len(act_line_1)))
                # put . in place of ?
                act_line_1 = act_line[:act_new_i] + '.' + act_line[act_new_i+1:]
                sub_queue.put(self.get_substr(act_line_1, len(act_line_1)))
            else:
            #    print(act_substrs)
                if len(act_substrs) == nums_len:
                    result += self.get_result_for_ideal_match(act_substrs, nums)
              #  print(result)
            
        return result
    

    def get_result_for_ideal_match(self, substrs, nums):
        return reduce(lambda x, y: x * y, [self.get_possibilities_for_one_substr_NEW(substr, num) for num, substr in zip(nums, substrs)])


    def solution_1(self):
        results = []
        for row, row_len, nums in zip(self.data, self.data_lens, self.nums):
            act_substrs = self.get_substr(row, row_len)
            results.append(self.get_possibilities_for_few_nums(act_substrs, nums))
            
            print(row, results[-1])
        print(results)
        return sum(results)


def main():
    print('TASK 1')
    sol = Solution('2023/Day_12/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1())
    sol = Solution('2023/Day_12/test_2.txt')
    print('test 2:', sol.solution_1())
    sol = Solution('2023/Day_12/test_3.txt')
    print('test 3:', sol.solution_1())
    sol = Solution('2023/Day_12/test_4.txt')
    print('test 4:', sol.solution_1())
    sol = Solution('2023/Day_12/test_5.txt')
    print('test 5:', sol.solution_1())
  #  sol = Solution('2023/Day_12/task.txt')
  #  print('SOLUTION')
  #  print('Solution 1:', sol.solution_1())


if __name__ == '__main__':
    main()
