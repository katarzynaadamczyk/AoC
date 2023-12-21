'''
Advent of Code 
2023 day 18
my solution to task 2 

solution 2 - idea (Picks theorem) -> count integer points inside and outside and use the formula. To count points inside I count independently 
points up and down y=0 axis -> when going left add area of rectangle below (above) to y=0 line, when going right substract this area. In addition
sum all lines going up and left -> this gives 1/2 of all points on the boundary. Then add absolute values of each of given above parameter and add 1 ->
this is the result.

'''
from queue import Queue

class Solution:

    LEFT = '2'
    RIGHT = '0'
    DOWN = '1'
    UP = '3'


    next_point = {LEFT: lambda point, diff: (point[0] - diff, point[1]),
                  RIGHT: lambda point, diff: (point[0] + diff, point[1]),
                  DOWN: lambda point, diff: (point[0], point[1] + diff),
                  UP: lambda point, diff: (point[0], point[1] - diff)}
    
    rectangle_size_up = {LEFT: lambda start_point, end_point: abs((end_point[0] - start_point[0]) * end_point[1]),
                         RIGHT: lambda start_point, end_point: - 1 * abs((end_point[0] - start_point[0]) * end_point[1]),
                         DOWN: lambda start_point, end_point: 0,
                         UP: lambda start_point, end_point: 0}


    def __init__(self, filename) -> None:
        self.get_data(filename)


    def get_data(self, filename):
        self.data = []
        with open(filename, 'r') as myfile:
            for line in myfile:
                line = line.strip().split()
                self.data.append((line[2][-2], int(line[2][2:-2], 16)))

    # point[0] -> x
    # point[1] -> y
    def solution_1(self):
        act_point = (0, 0)
        self.ups = 0
        self.lefts = 0
        self.rectangles_down = 0
        self.rectangles_up = 0
        for direction, how_many in self.data:
            new_point = Solution.next_point[direction](act_point, how_many)
            if new_point[1] > 0:
                self.rectangles_down += Solution.rectangle_size_up[direction](act_point, new_point)
            else:
                self.rectangles_up += Solution.rectangle_size_up[direction](act_point, new_point)
            if direction == Solution.UP:
                self.ups += abs(act_point[1] - new_point[1])
            elif direction == Solution.LEFT:
                self.lefts += abs(act_point[0] - new_point[0])
            act_point = new_point
        print(act_point)
        print([self.ups, self.lefts, self.rectangles_down, self.rectangles_up])
        return (self.ups + self.lefts) + abs(self.rectangles_down) + abs(self.rectangles_up) + 1


def main():
    print('TASK 1')
    sol = Solution('2023/Day_18/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1())
    sol = Solution('2023/Day_18/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())


if __name__ == '__main__':
    main()
