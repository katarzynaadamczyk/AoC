'''
Advent of Code 
2025 day 7
my solution to tasks 

task 1 - working on sets - keep adding to actual points new points until all points are removed from set of points
task 2 - working on sets - analogical as above but need to keep count of each point divisions 

'''
from collections import defaultdict
from functools import reduce
import time


def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        print(f'time taken by {func.__name__} is {round(time.time()-start, 4)}')

        return result
    return wrapper


class Solution:
    
    def __init__(self, filename: str) -> None:
        '''
        initialize Solution
        '''
        self.start, self.stops = self.get_data(filename)

    def get_data(self, filename) -> tuple[tuple[int, int], set[tuple[int, int]]]:
        '''
        parse data
        '''
        result = set()
        with open(filename, 'r') as my_file:
            line = my_file.readline()
            start = (0, line.find('S'))
            for y, line in enumerate(my_file, 1):
                for x, char in enumerate(line):
                    if char == '^':
                        result.add((y, x))
        return start, result
    
    def _get_next_split(self, point: tuple[int, int]) -> tuple[int, int] | None:
        possible_next_splits = tuple(x for x in self.stops if x[0] > point[0] and x[1] == point[1])
        if possible_next_splits:
            return min(possible_next_splits, key=lambda x: x[0])
        return None 

    @time_it
    def solution_1(self) -> int:
        '''
        get result for task 1
        '''
        result = 0
        visited_points = set()
        actual_points = set()
        actual_points.add(self.start)
        while actual_points:
            point = actual_points.pop()
            next_split = self._get_next_split(point)
            if next_split is not None and next_split not in visited_points:
                visited_points.add(next_split)
                point_1, point_2 = (next_split[0], next_split[1] + 1), (next_split[0], next_split[1] - 1)
                result += 1
                actual_points.add(point_1)
                actual_points.add(point_2)
        
        return result

    @time_it
    def solution_2(self) -> int:
        '''
        get result for task 2
        '''
        points_that_ended = set()
        results_dict = defaultdict(int)
        actual_points = set()
        actual_points.add(self.start)
        results_dict[self.start] = 1
        while actual_points:
            point = min(actual_points)
            next_split = self._get_next_split(point)
            if next_split is not None:
                point_1, point_2 = (next_split[0], next_split[1] + 1), (next_split[0], next_split[1] - 1)
                actual_points.add(point_1)
                actual_points.add(point_2)
                results_dict[point_1] += results_dict[point]
                results_dict[point_2] += results_dict[point]
            else:
                points_that_ended.add(point)
            actual_points.remove(point)

        return reduce(lambda x, y: x + y, (results_dict[point] for point in points_that_ended))


def main():
    print('TEST 1')
    sol = Solution('2025/Day_7/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 21')
    print('test 2:', sol.solution_2(), 'should equal 40')
    print('SOLUTION')
    sol = Solution('2025/Day_7/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2())
   


if __name__ == '__main__':
    main()
