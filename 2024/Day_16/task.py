'''
Advent of Code 
2024 day 16
my solution to tasks

today's solution_1 solves both tasks

BFS algorithm

task 1

'''

from copy import copy
import heapq
import time
from sys import maxsize

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
        self.get_data(filename)
        self.reindeer_direction = '>'
        
        self.directions = {'>': (0, 1),
                           '<': (0, -1),
                           '^': (-1, 0),
                           'v': (1, 0)}
        
        self.next_directions = {'>': ('^', 'v'),
                                '<': ('^', 'v'),
                                '^': ('>', '<'),
                                'v': ('>', '<')}


    def get_data(self, filename):
        '''
        parse data
        '''
        with open(filename, 'r') as myfile:
            for y, line in enumerate(myfile):
                for x, val in enumerate(line.strip()):
                    if val == 'E':
                        self.final_position = (y, x)
                    elif val == '#':
                        self.walls.add((y, x))
                    elif val == 'S':
                        self.reindeer_position = (y, x)

    
    def get_next_move(self, position, direction):
        '''
        get next possible position given actual position and direction
        if next position is a wall return None
        '''
        new_position = (position[0] + self.directions[direction][0], position[1] + self.directions[direction][1])
        if new_position not in self.walls:
            return new_position
        return None
    
    
    def check_next_move(self, point, direction, visited_points, path_len, change_dir=False):
        '''
        after getting new reindeer location (point), actual direction, visited_points, path_length and if direction was changed
        determine if reindeer will move and update self.general_visited_points and new_visited_points
        '''
        added_value = 1 if not change_dir else 1001
        if point is not None and point not in visited_points and \
           ((point, direction) not in self.general_visited_points.keys() or \
            ((point, direction) in self.general_visited_points.keys() and \
             self.general_visited_points[(point, direction)] >= path_len + added_value)):
                new_visited_points = copy(visited_points)
                new_visited_points.add(point)
                self.general_visited_points[(point, direction)] = path_len + added_value
                return True, new_visited_points
        return False, set()

    
    def let_reindeer_move(self):
        '''
        return value of lowest-valued-track and number of tiles for all lowest-value-tracks 
        '''
        
        # prepare heap (priority queue)
        stack = []
        heapq.heapify(stack)
        # keep in stack (path len, act_position, act_direction, set of visited points)
        heapq.heappush(stack, (0, self.reindeer_position, self.reindeer_direction, \
                               set([self.reindeer_position])))
        # prepare a dict {(point, direction): lowest_value_at_that_point_and_direction}
        self.general_visited_points = {}
        self.general_visited_points.setdefault((self.reindeer_position, self.reindeer_direction), 0)
        # prepare an empty set of points visited by all lowest-valued-tracks
        visited_points_in_lowest_paths = set()
        # set act_min_value to max_int
        act_min_path = maxsize
        # keep moving
        while stack:
            path_len, act_pos, act_dir, visited_points = heapq.heappop(stack)
            # ending conditions
            if act_pos == self.final_position:
                act_min_path = min(act_min_path, path_len)
                if path_len == act_min_path:
                    visited_points_in_lowest_paths = visited_points_in_lowest_paths.union(visited_points)
                if path_len > act_min_path:
                    break
                continue
            # get next position moving still in same direction
            new_pos = self.get_next_move(act_pos, act_dir)
            # check if reindeer can move, if so, add to heap
            add_to_heap, new_visited_points = self.check_next_move(new_pos, act_dir, visited_points, path_len)
            if add_to_heap:
                heapq.heappush(stack, (path_len + 1, new_pos, act_dir, new_visited_points))
            # for possible change of directions check if reindeer can move, if so add to heap
            for new_dir in self.next_directions[act_dir]:
                new_pos = self.get_next_move(act_pos, new_dir)
                add_to_heap, new_visited_points = self.check_next_move(new_pos, new_dir, visited_points, path_len, True)
                if add_to_heap:
                    heapq.heappush(stack, (path_len + 1001, new_pos, new_dir, new_visited_points))
        return (act_min_path, len(visited_points_in_lowest_paths))
            

    @time_it
    def solution_1(self) -> int:
        '''
        get result for task 1
        '''
        return self.let_reindeer_move()
    


    

def main():

    print('TEST 1')
    sol = Solution('2024/Day_16/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal ?')
  #  print('test 1:', sol.solution_2(), 'should equal ?')
    sol = Solution('2024/Day_16/test_2.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal ?')
  #  print('test 1:', sol.solution_2(), 'should equal ?')
    print('SOLUTION')
    sol = Solution('2024/Day_16/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1()) 
   # print('Solution 2:', sol.solution_2()) 
   


if __name__ == '__main__':
    main()
