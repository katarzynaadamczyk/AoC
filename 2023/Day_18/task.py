'''
Advent of Code 
2023 day 18
my solution to task 1 & 2

solution 1 - 

solution 2 - 

'''
from queue import Queue

class Solution:

    LEFT = 'L'
    RIGHT = 'R'
    DOWN = 'D'
    UP = 'U'



    next_point = {LEFT: lambda point: (point[0] - 1, point[1]),
                  RIGHT: lambda point: (point[0] + 1, point[1]),
                  DOWN: lambda point: (point[0], point[1] + 1),
                  UP: lambda point: (point[0], point[1] - 1)}
    
    neighbor_point = {LEFT: lambda point: (point[0], point[1] - 1),
                      RIGHT: lambda point: (point[0], point[1] + 1),
                      DOWN: lambda point: (point[0] - 1, point[1]),
                      UP: lambda point: (point[0] + 1, point[1])}
    

    def __init__(self, filename) -> None:
        self.get_data(filename)


    def get_data(self, filename):
        self.data = []
        with open(filename, 'r') as myfile:
            for line in myfile:
                line = line.strip().split()
                self.data.append((line[0], int(line[1]), line[2][1:-1]))

    def expand_point(self, point):
        act_queue = Queue()
        act_queue.put(point)
        while not act_queue.empty():
            point = act_queue.get()
            if point not in self.set_of_points_boundary and point not in self.set_of_points_inside:
                self.set_of_points_inside.add(point)
                act_queue.put(Solution.next_point[Solution.UP](point))
                act_queue.put(Solution.next_point[Solution.DOWN](point))
                act_queue.put(Solution.next_point[Solution.LEFT](point))
                act_queue.put(Solution.next_point[Solution.RIGHT](point))


    def solution_1(self):
        act_point = (0, 0)
        self.set_of_points_boundary = set()
        for direction, how_many, _ in self.data:
            for _ in range(how_many):
                new_point = Solution.next_point[direction](act_point)
                act_point = new_point
                self.set_of_points_boundary.add(new_point)
        print(act_point)
        self.set_of_points_inside = set()
        for direction, how_many, _ in self.data:
            for _ in range(how_many):
                new_point = Solution.neighbor_point[direction](act_point)
                act_point = Solution.next_point[direction](act_point)
                self.expand_point(new_point)
        return len(self.set_of_points_boundary) + len(self.set_of_points_inside)


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
