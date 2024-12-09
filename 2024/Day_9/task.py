'''
Advent of Code 
2024 day 9
my solution to tasks
task 1 - 


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
            

    
    
    def solution_1(self) -> int:
        result = 0
        self.move_layout()
     #   print(self.new_layout)
        i = 0
        for num, val in self.new_layout:
            for j in range(i, i+num):
                result += j * val
            i += num
        return result
    


    
    def solution_2(self) -> int:
        results = set()
        return len(results)



    

def main():

    print('TASK 1')
    sol = Solution('2024/Day_9/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 1928')
 #   print('test 1:', sol.solution_2(), 'should equal 34')
    sol = Solution('2024/Day_9/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1()) # 24407607019085 too high
  #  print('Solution 2:', sol.solution_2())
   


if __name__ == '__main__':
    main()
