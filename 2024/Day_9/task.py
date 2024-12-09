'''
Advent of Code 
2024 day 9
my solution to tasks

first prepare layout -> list of tuples (n, index), if index == -1 it is a free space
task 1 - keep track of index of actual right tuple and how many number have already been taken.
iterate over layout from left to right to get a new one. 
if left index >= right index -> stop iterating, take only remaining number of values
if left value != free space then add (num, val) to new layout
else keep adding values from right index until free space is filled up
to get result iterate over new layout while keeping track of index 

task 2 - split layout into list of nums and free spaces containing tuples: (index, (count, values))
keep track of moved tuples
iterate over nums from right to left
    in each iteration iterate over empty to find right spot
        if found then add it to empty list and to set of moved tuples and stop iterating through empty
to get result iterate over nums -> if tuple is in moved set then ignore it
and over empty -> if tuple is free space ignore it


'''

from tqdm import tqdm
import re

class Solution:

    def __init__(self, filename) -> None:
        self.disk_map = []
        self.get_data(filename)
        self.get_layout_of_file()

    def get_data(self, filename):
        with open(filename, 'r') as myfile:
            for line in myfile:
                self.disk_map = [int(x) for x in re.findall(r'\d', line)]   

    def get_layout_of_file(self):
        self.layout = []
        act_id = 0
        self.free_space = -1
        if_id = True
        for num in self.disk_map:
            if if_id:
                if num > 0:
                    self.layout.append((num, act_id))
                act_id += 1
            else:
                if num > 0:
                    self.layout.append((num, self.free_space))
            if_id = not if_id
    
    def get_new_right_values(self, right_pos, took_from_last):
        if took_from_last < self.layout[right_pos][0]:
            return right_pos, took_from_last
        right_pos -= 1
        while self.layout[right_pos][1] == self.free_space:
            right_pos -= 1
        return right_pos, 0 

    def move_layout(self):
        self.new_layout = []
        right_pos, took_from_last = len(self.layout) - 1, 0
        for i, (num, val) in enumerate(self.layout):
            if i == right_pos:
                self.new_layout.append((num - took_from_last, val))
                break
            if i > right_pos:
                break
            if val != self.free_space:
                self.new_layout.append((num, val))
                continue
            while num > 0:
                will_take = min(num, self.layout[right_pos][0] - took_from_last)
                self.new_layout.append((will_take, self.layout[right_pos][1]))
                num -= will_take
                took_from_last += will_take
                right_pos, took_from_last = self.get_new_right_values(right_pos, took_from_last)
            
    def divide_layout_for_empty_and_nums(self):
        i = 0
        empty, nums = [], []
        for tpl in self.layout:
            if tpl[1] == self.free_space:
                empty.append((i, tpl))
            else:
                nums.append((i, tpl))
            i += tpl[0]
        return empty, nums
    
    def solution_1(self) -> int:
        result = 0
        self.move_layout()
        i = 0
        for num, val in self.new_layout:
            for j in range(i, i+num):
                result += j * val
            i += num
        return result
    


    
    def solution_2(self) -> int:
        result = 0
        empty, nums = self.divide_layout_for_empty_and_nums()
        moved = set() # set of tuples moved to empty
        
        for (i, tpl) in tqdm(nums[::-1]):
            new_empty = empty
            for x, (j, empts) in enumerate(empty):
                if j > i:
                    break
                if empts[1] == self.free_space and empts[0] >= tpl[0]:
                    if empts[0] == tpl[0]:
                        new_empty = empty[:x] + [(j, tpl)] + empty[x+1:]
                    else:
                        new_empty = empty[:x] + [(j, tpl), (j + tpl[0], (empts[0] - tpl[0], self.free_space))] + empty[x+1:]
                    moved.add(tpl)
                    break
            empty = new_empty

        for (i, tpl) in nums:
            if tpl not in moved:
                for j in range(i, i+tpl[0]):
                    result += j * tpl[1]
        
        for (i, tpl) in empty:
            if tpl[1] != self.free_space:
                for j in range(i, i+tpl[0]):
                    result += j * tpl[1]
        
        return result



    

def main():

    print('TASK 1')
    sol = Solution('2024/Day_9/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 1928')
    print('test 1:', sol.solution_2(), 'should equal 2858')
    sol = Solution('2024/Day_9/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2())
   


if __name__ == '__main__':
    main()
