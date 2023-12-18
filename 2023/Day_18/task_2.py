'''
Advent of Code 
2023 day 18
my solution to task 2 

solution 2 - 

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
    

    def __init__(self, filename) -> None:
        self.get_data(filename)


    def get_data(self, filename):
        self.data = []
        with open(filename, 'r') as myfile:
            for line in myfile:
                line = line.strip().split()
                self.data.append((line[2][-2], int(line[2][2:-2], 16)))


    def solution_1(self):
        act_point = (0, 0)
        self.lines = {}
        self.lines.setdefault(act_point, set())
        for direction, how_many in self.data:
            new_point = Solution.next_point[direction](act_point, how_many)
            self.lines[act_point].add(new_point)
            self.lines.setdefault(new_point, set())
            self.lines[new_point].add(act_point)
            act_point = new_point
        print(self.lines)
        print(act_point)
        return len(self.lines)


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
