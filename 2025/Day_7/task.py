'''
Advent of Code 
2025 day 7
my solution to tasks 

task 1 - 
task 2 - 

'''
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
            new_points = set()
            for point in actual_points:
                next_split = self._get_next_split(point)
                if next_split is not None and next_split not in visited_points:
                    visited_points.add(next_split)
                    point_1, point_2 = (next_split[0], next_split[1] + 1), (next_split[0], next_split[1] - 1)
                    result += 1
                    new_points.add(point_1)
                    new_points.add(point_2)
            actual_points = new_points
        
        return result

    @time_it
    def solution_2(self) -> int:
        '''
        get result for task 2
        '''
        result = 0

        return result


def main():
    print('TEST 1')
    sol = Solution('2025/Day_7/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 21')
 #   print('test 2:', sol.solution_2(), 'should equal 3263827')
    print('SOLUTION')
    sol = Solution('2025/Day_7/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
  #  print('Solution 2:', sol.solution_2())
   


if __name__ == '__main__':
    main()
