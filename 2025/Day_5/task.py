'''
Advent of Code 
2025 day 5
my solution to tasks (operations on sets)
prepare well data - squash the ranges

task 1 - for each ingredient check if it exists in any range
task 2 - simple sum of (range_max - range_min + 1)

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
        self.set_of_ranges, self.ingredients = self.get_data(filename)
        self._prepare_tuple_of_ranges()

    def get_data(self, filename) -> tuple[set[tuple[int, int]], set[int]]:
        '''
        parse data
        '''
        set_of_ranges, ingredients = set(), set()
        with open(filename, 'r') as my_file:
            contents = my_file.read().split("\n\n")
        
        for chunk in contents[0].split():
            a, b = chunk.split('-')
            set_of_ranges.add((int(a), int(b)))
        ingredients = set(int(x) for x in contents[1].split())
        return set_of_ranges, ingredients

    def _get_joined_range(self, i1: int, i2: int):
        return (min(x[0] for x in self.set_of_ranges[i1:i2+1]), max(x[1] for x in self.set_of_ranges[i1:i2+1]))


    def _prepare_tuple_of_ranges(self):
        self.set_of_ranges = tuple(sorted(self.set_of_ranges))
        changes_made = True
        while changes_made:
            changes_made = False
            i = 0
            join = 0
            new_set_of_ranges = set()
            while i < len(self.set_of_ranges):
                if join >= len(self.set_of_ranges) - 1:
                    new_set_of_ranges.add(self._get_joined_range(i, join))
                    break
                if (self.set_of_ranges[join + 1][0] - 1) <= self.set_of_ranges[join][1] <= self.set_of_ranges[join + 1][1] \
                    or (self.set_of_ranges[join][0] - 1) <= self.set_of_ranges[join + 1][0] <= self.set_of_ranges[join][1] \
                    or (self.set_of_ranges[join + 1][0] - 1) <= self.set_of_ranges[join][0] <= self.set_of_ranges[join + 1][1] \
                    or (self.set_of_ranges[join][0] - 1) <= self.set_of_ranges[join + 1][1] <= self.set_of_ranges[join][1]:
                    join += 1
                else:
                    new_set_of_ranges.add(self._get_joined_range(i, join))
                    join += 1
                    i = join
            if len(self.set_of_ranges) != len(new_set_of_ranges):
                self.set_of_ranges = tuple(sorted(new_set_of_ranges))
                changes_made = True




    @time_it
    def solution_1(self) -> int:
        '''
        get result for task 1
        '''
        result = 0
        for ingredient in self.ingredients:
            if ingredient < self.set_of_ranges[0][0] or ingredient > self.set_of_ranges[-1][1]:
                continue
            for _range in self.set_of_ranges:
                if _range[0] <= ingredient <= _range[1]:
                    result += 1
                    break
        return result

    @time_it
    def solution_2(self) -> int:
        '''
        get result for task 2
        '''

        return sum(_range[1] - _range[0] + 1 for _range in self.set_of_ranges)


def main():
    print('TEST 1')
    sol = Solution('2025/Day_5/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 3')
    print('test 2:', sol.solution_2(), 'should equal 14')
    print('SOLUTION')
    sol = Solution('2025/Day_5/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2())
   


if __name__ == '__main__':
    main()
