'''
Advent of Code 
2023 day 10
my solution to task 1 & 2

solution 1 - 

solution 2 - 

'''
from queue import PriorityQueue

class Solution:
    
    @staticmethod
    def north(y, x):
        return (y - 1, x)
    
    @staticmethod
    def east(y, x):
        return (y, x + 1)
    
    @staticmethod
    def south(y, x):
        return (y + 1, x)
    
    @staticmethod 
    def west(y, x):
        return (y, x - 1)

    pipes = {'|': (north, south), 
             '-': (east, west),
             'L': (north, east),
             'J': (north, west),
             '7': (south, west),
             'F': (south, east)}
    
    pipe_types = '|-LJ7F'
    
    def __init__(self, filename, start_name) -> None:
        self.get_data(filename, start_name)
        self.map_constraits_x_min = 0
        self.map_constraits_y_min = 0
        self.map_constraits_x_max = len(self.data[0])
        self.map_constraits_y_max = len(self.data)
        self.map = self.prepare_map()
        self.visited_points = {self.start: 0}
     #   print(self.map)
    #    print(self.visited_points)

    def get_data(self, filename, start_name):
        self.data, self.start = [], (0, 0)
        with open(filename, 'r') as myfile:
            for line in myfile:
                if start_name in line:
                    self.start = (len(self.data), line.index(start_name))
                self.data.append(line.strip())
    
    def check_point(self, point):
        if not (self.map_constraits_x_min <= point[1] < self.map_constraits_x_max):
            return False
        if not (self.map_constraits_y_min <= point[0] < self.map_constraits_y_max):
            return False
        return True
    
    def prepare_map(self):
        self.first_points = set()
        act_map = {}
        for y, line in enumerate(self.data):
            for x, pipe in enumerate(line):
                if pipe in Solution.pipe_types:
                    first_point, second_point = Solution.pipes[pipe][0](y, x), Solution.pipes[pipe][1](y, x)
                    if self.check_point(first_point):
                        act_map.setdefault((y, x), [])
                        act_map[(y, x)].append(first_point)
                        if first_point == self.start:
                            self.first_points.add((y, x))
                    if self.check_point(second_point):
                        act_map.setdefault((y, x), [])
                        act_map[(y, x)].append(second_point)
                        if second_point == self.start:
                            self.first_points.add((y, x))
        return act_map

    def solution_1(self):
        points_q = PriorityQueue()
        for point in self.first_points:
            points_q.put((1, point))
        while not points_q.empty():
            steps, point = points_q.get()
            if point in self.map.keys():
                for next_point in self.map[point]:
                    if next_point not in self.visited_points:
                        self.visited_points.setdefault(next_point, steps + 1)
                        points_q.put((steps + 1, next_point))

        return max(self.visited_points.values())
    


def main():
    sol = Solution('2023/Day_10/test_1.txt', 'S')
    print('test 1:', sol.solution_1())
    sol = Solution('2023/Day_10/test_2.txt', 'S')
    print('test 1:', sol.solution_1())
    sol = Solution('2023/Day_10/task.txt', 'S')
    print('Solution 1:', sol.solution_1())


if __name__ == '__main__':
    main()
