'''
Advent of Code 
2024 day 20
my solution to tasks


task 1 - first get the path, then for each point check if there are possible cheating positions of size 2, if so
check if profit is >= treshold, if so add 1 to result

task 2 - also a brute force, for each position get all possible cheating positions with max path len equal to 20, count those points 
for which path length >= treshold, it runs in ~20 s
I got another idea -> instead of counting paths I should get all points that are in manhattan distance <= 20 and are on the path
will try to implement it in task_2.py

'''

import time
import heapq
from tqdm import tqdm

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
            if new_point not in self.walls and new_point not in self.point_len.keys():
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


    def get_possible_cheating_points_2(self, point):
        '''
        get possible cheating points given position for task 2
        path len from point to new_point <= 20
        '''
        stack = []
        heapq.heapify(stack)
        heapq.heappush(stack, (0, point))
        result = set()
        visited_points = set()
        visited_points.add(point)
        while stack:
            act_len, act_point = heapq.heappop(stack)
            if act_point in self.point_len.keys():
                result.add((act_len, act_point))
            if act_len == 20 or act_point[0] < self.min_y or act_point[1] < self.min_x \
                or act_point[0] > self.max_y or act_point[1] > self.max_x:
                continue
            for direction in self.directions:
                new_point = (direction[0] + act_point[0], direction[1] + act_point[1])
                if new_point not in visited_points:
                    visited_points.add(new_point)
                    heapq.heappush(stack, (act_len + 1, new_point))
        return result


    def check_cheating_possibilities(self, treshold):
        '''
        get all possible cheating possibilities that have value above treshold
        only for part 1
        '''
        result = 0
        for point in self.point_len.keys():
            for new_point in self.get_possible_cheating_points(point):
                if self.point_len[new_point] > self.point_len[point] and \
                    self.point_len[new_point] - self.point_len[point] - 2 >= treshold:
                        result += 1
        return result
    
    def check_cheating_possibilities_2(self, treshold):
        '''
        get all possible cheating possibilities that have value above treshold
        only for part 1
        '''
        result = 0
        for point in self.point_len.keys():
            for path_len, new_point in self.get_possible_cheating_points_2(point):
                if self.point_len[new_point] > self.point_len[point] and \
                    self.point_len[new_point] - self.point_len[point] - path_len >= treshold:
                        result += 1
        return result
    
    
    @time_it
    def solution_1(self, treshold=100) -> int:
        '''
        get result for task 1
        '''
        self.get_route()
        return self.check_cheating_possibilities(treshold)
    

    @time_it
    def solution_2(self, treshold=100) -> int:
        '''
        get result for task 2
        '''
        return self.check_cheating_possibilities_2(treshold)
    


    

def main():

    print('TEST 1')
    sol = Solution('2024/Day_20/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(20), 'should equal 5')
    print('test 1:', sol.solution_2(50), 'should equal 285')
    print('SOLUTION')
    sol = Solution('2024/Day_20/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2()) 
   


if __name__ == '__main__':
    main()
