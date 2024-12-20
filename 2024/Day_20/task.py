'''
Advent of Code 
2024 day 20
my solution to tasks


task 1 - 

task 2 - 

'''

import time
import heapq
from collections import Counter

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        print(f'time taken by {func.__name__} is {round(time.time()-start, 4)}')

        return result
    return wrapper


class Solution:

    def __init__(self, filename) -> None:
        '''
        initialize Solution
        '''
        self.walls = set()
        self.start_pos, self.end_pos = (0, 0), (0, 0)
        self.get_data(filename)
        self.directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        self.min_x, self.min_y = 0, 0
        self.point_len = {self.start_pos: 0}
        self.min_point, self.max_point = (self.min_y, self.min_x), (self.max_y, self.max_x)



    def get_data(self, filename):
        '''
        parse data
        '''
        with open(filename, 'r') as myfile:
            for y, line in enumerate(myfile):
                for x, val in enumerate(line.strip()):
                    if val == '#':
                        self.walls.add((y, x))
                    elif val == 'S':
                        self.start_pos = (y, x)
                    elif val == 'E':
                        self.end_pos = (y, x)
                self.max_x = x
            self.max_y = y

    def get_next_possible_points(self, point):
        '''
        get next possible point while serching for unique no cheating path
        '''
        for direction in self.directions:
            new_point = (direction[0] + point[0], direction[1] + point[1])
            if self.min_point <= new_point <= self.max_point and \
                new_point not in self.walls and new_point not in self.point_len.keys():
                yield new_point
    
    def get_route(self):
        '''
        function to fill up self.point_len dict to get time values 
        for each point of the route 
        '''
        stack = []
        heapq.heapify(stack)
        heapq.heappush(stack, (0, self.start_pos))
        while stack:
            act_len, act_point = heapq.heappop(stack)
            if act_point == self.end_pos:
                continue
            for new_point in self.get_next_possible_points(act_point):
                self.point_len[new_point] = act_len + 1
                heapq.heappush(stack, (act_len + 1, new_point))
        return 0

    def get_possible_cheating_points(self, point):
        '''
        get possible cheating points given position
        '''
        for direction in self.directions:
            wall_point = (direction[0] + point[0], direction[1] + point[1])
            new_point = (2 * direction[0] + point[0], 2 * direction[1] + point[1])
            if wall_point in self.walls and new_point in self.point_len.keys():
                yield new_point

    def check_cheating_possibilities(self, treshold):
        '''
        get all possible cheating possibilities in one dictionary
        '''
        result = 0
        for point in self.point_len.keys():
            for new_point in self.get_possible_cheating_points(point):
                if self.point_len[new_point] > self.point_len[point] and \
                    self.point_len[new_point] - self.point_len[point] - 2 >= treshold:
                        result += 1
        return result

# points_small = dict(filter(lambda (a,(b,c)): b<5 and c < 5, points.items()))
    
    
    @time_it
    def solution_1(self, treshold=100) -> int:
        '''
        get result for task 1
        '''
        self.get_route()
        return self.check_cheating_possibilities(treshold)
    

    @time_it
    def solution_2(self) -> int:
        '''
        get result for task 2
        '''
        result = 0
        return result
    


    

def main():

    print('TEST 1')
    sol = Solution('2024/Day_20/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(20), 'should equal 5')
   # print('test 1:', sol.solution_2(50), 'should equal 285')
    print('SOLUTION')
    sol = Solution('2024/Day_20/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    #print('Solution 2:', sol.solution_2()) 
   


if __name__ == '__main__':
    main()
