'''
Advent of Code 
2015 day 18
my solution to tasks

task 1 - brute force on sets - keep the sets of lights switched on and filter on their  


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
    def __init__(self, filename) -> None:
        '''
        initialize Solution
        '''
        self.lights = set()
        self.filename = filename
        self.get_data(filename)

    def get_data(self, filename):
        '''
        parse data
        '''
        with open(filename, 'r') as my_file:
            for y, line in enumerate(my_file):
                for x, char in enumerate(line.strip()):
                    if char == '#':
                        self.lights.add((y, x))
        self.max_y = y
        self.max_x = x

    def _count_surrounding_lights(self, y: int, x: int) -> int:
        surrounding_lights = 0
        for y1 in range(y-1, y+2):
            if (y1, x-1) in self.lights:
                surrounding_lights += 1
            if (y1, x+1) in self.lights:
                surrounding_lights += 1
        if (y-1, x) in self.lights:
            surrounding_lights += 1
        if (y+1, x) in self.lights:
            surrounding_lights += 1
        return surrounding_lights
    
    def _will_be_light(self, y: int, x: int) -> bool:
        surrounding_lights = self._count_surrounding_lights(y, x)
        if surrounding_lights == 3 or (surrounding_lights == 2 and (y, x) in self.lights):
            return True
        return False
                                       

    @time_it
    def solution_1(self, steps: int) -> int:
        '''
        get result for task 1
        '''
        for _ in range(steps):
            tmp = set()
            for y in range(self.max_y + 1):
                for x in range(self.max_x + 1):
                    if self._will_be_light(y, x):
                        tmp.add((y, x))
            self.lights = tmp
        return len(self.lights)


    @time_it
    def solution_2(self, steps: int) -> int:
        '''
        get result for task 2
        '''
        self.__init__(self.filename)
        always_on = {(0,0), (self.max_y, 0), (self.max_y, self.max_x), (0, self.max_x)}
        self.lights = self.lights.union(always_on)
        for _ in range(steps):
            tmp = set()
            for y in range(self.max_y + 1):
                for x in range(self.max_x + 1):
                    if self._will_be_light(y, x):
                        tmp.add((y, x))
            self.lights = tmp.union(always_on)
        return len(self.lights)


def main():
    print('TEST 1')
    sol = Solution('2015/Day_18/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(4), 'should equal 4')
    print('test 2:', sol.solution_2(5), 'should equal 17')
    print('SOLUTION')
    sol = Solution('2015/Day_18/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1(100))
    print('Solution 2:', sol.solution_2(100))
   


if __name__ == '__main__':
    main()
