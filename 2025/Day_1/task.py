'''
Advent of Code 
2025 day 21
my solution to tasks

task 1&2 - calculations step by step using modulo functions (time: n - number of entrances)


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
    direction_to_move = {'L': lambda pos, value: ((pos - value) % 100, (1 if pos - (value % 100) < 0 and pos != 0 else 0) + value // 100),
                         'R': lambda pos, value: ((pos + value) % 100, (1 if pos + (value % 100) > 100 else 0) + value // 100)}

    def __init__(self, filename: str) -> None:
        '''
        initialize Solution
        '''
        self.filename = filename
        self.position = 50
        self.result_1 = 0
        self.result_2 = 0

    def get_result_1(self):
        with open(self.filename, 'r') as my_file:
            for line in my_file:
                line = line.strip()
                direction, value = line[0], int(line[1:])
                self.move_1(direction, value)

    def get_result_2(self):
        with open(self.filename, 'r') as my_file:
            for line in my_file:
                line = line.strip()
                direction, value = line[0], int(line[1:])
                self.move_2(direction, value)

    def move_1(self, direction: str, value: int) -> None:
        self.position, _ = self.direction_to_move[direction](self.position, value)
        if self.position == 0:
            self.result_1 += 1

    def move_2(self, direction: str, value: int) -> None:
       # print("*** new move ***" )
       # print(self.result_2, self.position, direction, value)
        self.position, through_zero = self.direction_to_move[direction](self.position, value)
        if self.position == 0:
            self.result_2 += 1
        self.result_2 += through_zero
       # print(self.result_2, self.position, through_zero)

    @time_it
    def solution_1(self) -> int:
        '''
        get result for task 1
        '''
        self.position = 50
        self.get_result_1()

        return self.result_1


    @time_it
    def solution_2(self) -> int:
        '''
        get result for task 2
        '''
        self.position = 50
        self.get_result_2()
        return self.result_2

def main():
    print('TEST 1')
    sol = Solution('2025/Day_1/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 3')
    print('test 2:', sol.solution_2(), 'should equal 6')
    print('SOLUTION')
    sol = Solution('2025/Day_1/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2())
   


if __name__ == '__main__':
    main()
