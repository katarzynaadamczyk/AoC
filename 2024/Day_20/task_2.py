'''
Advent of Code 
2024 day 20
my solution to tasks


task 1 & 2 solved using manhattan distance - is not as fast as I thought it would be, brute force takes similar amount of time ~12 s

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


    def manhattan_distance(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


    def calculate_distances_between_points(self):
        '''
        get all pairs of points for needed distances
        '''
        self.distances = {}
        not_saw_points = set(self.point_len.keys())
        for point in self.point_len.keys():
            not_saw_points.remove(point)
            for point_2 in not_saw_points:
                dist = self.manhattan_distance(point, point_2)
                if dist <= 20: # no need to keep dist > 20 as it will not be needed
                    self.distances.setdefault(dist, [])
                    self.distances[dist].append(sorted([point, point_2], key=lambda x: -1 * (self.point_len[x])))


    def check_cheating_possibilities(self, distance, treshold):
        '''
        get all possible cheating possibilities that have value above treshold
        '''
        result = 0
        for distance in range(2, distance + 1):
            if distance in self.distances.keys():
                for point1, point2 in self.distances[distance]:
                    if self.point_len[point1] - self.point_len[point2] - distance >= treshold:
                        result += 1 
        return result
    
    
    
    @time_it
    def solution_1(self, treshold=100) -> int:
        '''
        get result for task 1
        '''
        self.get_route()
        self.calculate_distances_between_points()
        return self.check_cheating_possibilities(2, treshold)
    

    @time_it
    def solution_2(self, treshold=100) -> int:
        '''
        get result for task 2
        '''
        return self.check_cheating_possibilities(20, treshold)
    


    

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
