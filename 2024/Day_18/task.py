'''
Advent of Code 
2024 day 18
my solution to tasks


task 1 - BFS algorithm avoiding fallen bytes only

task 2 - linear search to find first byte that prevents having a route to final_position
keep adding new falling bytes to bytes_falling set, after each new byte check if there is a route to the end (let_us_move), if it returns
0 then return lastly fallen byte
linear search works in 11 seconds - fine for me

'''
from tqdm import tqdm
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

    def __init__(self, filename, max_x=70, max_y=70, num=maxsize) -> None:
        '''
        initialize Solution
        '''
        self.bytes_falling = set()
        self.next_bytes_falling = []
        self.get_data(filename, num)
        self.start_position = (0, 0)
        self.final_position = (max_y, max_x)
        self.directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        self.min_x, self.min_y, self.max_x, self.max_y = 0, 0, max_x, max_y


    def get_data(self, filename, num):
        '''
        parse data
        '''
        with open(filename, 'r') as myfile:
            for i, line in enumerate(myfile):
                if i < num:
                    self.bytes_falling.add(tuple(int(x) for x in line.strip().split(',')))
                else:
                    self.next_bytes_falling.append(tuple(int(x) for x in line.strip().split(',')))

    def get_possible_next_points(self, point):
        '''
        function to get next possible positions given actual position
        '''
        for direction in self.directions:
            new_point = (point[0] + direction[0], point[1] + direction[1])
            if self.min_y <= new_point[0] <= self.max_y and self.min_x <= new_point[1] <= self.max_x \
                and new_point not in self.bytes_falling:
                yield new_point

    

    def let_us_move(self):
        '''
        function returning smallest possible number of steps to reach self.final_position
        '''
        stack = []
        heapq.heapify(stack)
        heapq.heappush(stack, (0, self.start_position))
        self.visited_points = {self.start_position: 0}
        while stack:
            path_len, position = heapq.heappop(stack)
            if position == self.final_position:
                return path_len
            for new_position in self.get_possible_next_points(position):
                if new_position not in self.visited_points.keys() or self.visited_points[new_position] > path_len + 1:
                    heapq.heappush(stack, (path_len + 1, new_position))
                    self.visited_points[new_position] = path_len + 1
        return 0


    
    @time_it
    def solution_1(self) -> int:
        '''
        get result for task 1
        '''
        return self.let_us_move()
    
    @time_it
    def solution_2(self) -> int:
        '''
        get result for task 2
        '''
        for byte_fall in tqdm(self.next_bytes_falling):
            self.bytes_falling.add(byte_fall)
            if self.let_us_move() == 0:
                return byte_fall
        return 0
    


    

def main():

    print('TEST 1')
    sol = Solution('2024/Day_18/test.txt', 6, 6, 12)
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal ?')
    print('test 1:', sol.solution_2(), 'should equal ?')
    print('SOLUTION')
    sol = Solution('2024/Day_18/task.txt', num=1024)
    print('SOLUTION')
    print('Solution 1:', sol.solution_1()) 
    print('Solution 2:', sol.solution_2()) 
   


if __name__ == '__main__':
    main()
