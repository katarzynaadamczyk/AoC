'''
Advent of Code 
2022 day 24
my solution to tasks from day 24


solution 1 - 
solution 2 - 

'''
from queue import PriorityQueue
from copy import deepcopy

class Solution:
    def __init__(self, new_map) -> None:
        self.x = 0
        self.y = 0
        self.x_goal = len(new_map[-1]) - 1
        self.y_goal = len(new_map) - 1
        self.map = [new_map]
    
    def solve(self):
        # data to be put to queue
        minutes, x, y = 0, self.x, self.y
        # defining the queue and putting there first data
        stack_of_moments = PriorityQueue()
        stack_of_moments.put((minutes, x, y))
        # the 'magic'
        while not stack_of_moments.empty():
            act_minute, act_x, act_y = stack_of_moments.get()
            # checking if what we got is our goal
            if act_x == self.x_goal and act_y == self.y_goal:
                return act_minute
            # new minute
            act_minute += 1
            # move blizzards if necessary
            if len(self.map) <= act_minute:
                self.move_blizzards(act_minute)
            
            # adding do nothing option to the queue    
            if self.map[act_minute][act_y][act_x] == '':
                stack_of_moments.put((act_minute, act_x, act_y))
            
            # adding any other option to the queue
            for x, y in self.check_where_to_go(act_minute, act_x, act_y):
                stack_of_moments.put((act_minute, x, y))
            
            break
        return -1
    
    def check_where_to_go(self, minute, x, y):
        #if 0 <= y < len(map[minute]) and 0 <= x < len(map[minute][y]):
        if 0 <= x - 1 < len(self.map[minute][y]) and self.map[minute][y][x-1] == '':
            yield x - 1, y
        if 0 <= x + 1 < len(self.map[minute][y]) and self.map[minute][y][x+1] == '':
            yield x + 1, y
        if 0 <= y - 1 < len(self.map[minute]) and self.map[minute][y-1][x] == '':
            yield x, y - 1
        if 0 <= y + 1 < len(self.map[minute]) and self.map[minute][y+1][x] == '':
            yield x, y + 1
    
    def move_blizzards(self, minute):
        # TODO
        # prepare an empty new map with all places filled with ''
        new_map = []
        # for each blizzard in previous map add corresponding blizzard to a new one
        for row in self.map[minute-1]: # previous map
            tmp = []
            # TODO
        # append new map to self.map
        self.map.append(self.map[-1])
        

def get_map(filename):
    new_map = []
    with open(filename, 'r') as myfile:
        for line in myfile:
            tmp = []
            line = line[1:-2]
            for char in line:
                if char == '.':
                    tmp.append('')
                else:
                    tmp.append(char)
            new_map.append(tmp)
    return new_map 


def solution_1(task_map):
    solver = Solution(task_map)
    return solver.solve()

  
def main():
    test_map_1, test_map_2 = get_map('2022/Day_24/test_1.txt'), get_map('2022/Day_24/test_2.txt')
    print('test 1:', solution_1(test_map_1))
    print('test 1:', solution_1(test_map_2))
    task_map = get_map('2022/Day_24/task.txt')
    print('Solution 1:', solution_1(task_map))
    
    
if __name__ == '__main__':
    main()
    