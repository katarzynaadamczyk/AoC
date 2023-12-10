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

    directions = {(): 0}
    
    def __init__(self, filename, start_name) -> None:
        self.get_data(filename, start_name)
        self.map_constraits_x_min = 0
        self.map_constraits_y_min = 0
        self.map_constraits_x_max = len(self.data[0])
        self.map_constraits_y_max = len(self.data)
        self.map = self.prepare_map()
        self.visited_points = {self.start: 0}

    def get_data(self, filename, start_name):
        self.data, self.start = [], (0, 0)
        with open(filename, 'r') as myfile:
            for line in myfile:
                if start_name in line:
                    self.start = (len(self.data), line.index(start_name))
                self.data.append([x for x in line.strip()])
    
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

    def change_start_point(self):
        if (self.start[0] - 1, self.start[1]) in self.first_points:
            if (self.start[0] + 1, self.start[1]) in self.first_points:
                self.data[self.start[0]][self.start[1]] = '|'
            elif (self.start[0], self.start[1] - 1) in self.first_points:
                self.data[self.start[0]][self.start[1]] = 'J'
            elif (self.start[0], self.start[1] + 1) in self.first_points:
                self.data[self.start[0]][self.start[1]] = 'L'
        elif (self.start[0] + 1, self.start[1]) in self.first_points:
            if (self.start[0], self.start[1] - 1) in self.first_points:
                self.data[self.start[0]][self.start[1]] = '7'
            elif (self.start[0], self.start[1] + 1) in self.first_points:
                self.data[self.start[0]][self.start[1]] = 'F'
        elif (self.start[0], self.start[1] - 1) in self.first_points:
            if (self.start[0], self.start[1] + 1) in self.first_points:
                self.data[self.start[0]][self.start[1]] = '-'

    
    def solution_2(self):
        points_to_exclude = set()
        self.change_start_point()
        for x in range(self.map_constraits_x_max):
            y = 0
            while y < self.map_constraits_y_max and (y, x) not in self.visited_points.keys():
                points_to_exclude.add((y, x))
                y += 1
            if y < self.map_constraits_y_max:
                y = self.map_constraits_y_max - 1
                while y > self.map_constraits_y_min and (y, x) not in self.visited_points.keys():
                    points_to_exclude.add((y, x))
                    y -= 1
        for y in range(1, self.map_constraits_y_max - 1):
            x = 0
            while x < self.map_constraits_x_max and (y, x) not in self.visited_points.keys():
                points_to_exclude.add((y, x))
                x += 1
            if x < self.map_constraits_x_max:
                x = self.map_constraits_x_max - 1
                while x > self.map_constraits_x_min and (y, x) not in self.visited_points.keys():
                    points_to_exclude.add((y, x))
                    x -= 1
        print('total_points:', self.map_constraits_x_max * self.map_constraits_y_max)
        print('exclude:', len(points_to_exclude))
        print('visited:', len(self.visited_points))
        return self.map_constraits_x_max * self.map_constraits_y_max - len(self.visited_points) - len(points_to_exclude)
    


def main():
    sol = Solution('2023/Day_10/test_1.txt', 'S')
    print('TEST 1')
    print('solution 1:', sol.solution_1())
    print('solution 2:', sol.solution_2())
    sol = Solution('2023/Day_10/test_2.txt', 'S')
    print('TEST 2')
    print('solution 1:', sol.solution_1())
    print('solution 2:', sol.solution_2())
    sol = Solution('2023/Day_10/test_3.txt', 'S')
    print('TEST 3')
    print('solution 1:', sol.solution_1())
    print('solution 2:', sol.solution_2())
    sol = Solution('2023/Day_10/test_4.txt', 'S')
    print('TEST 4')
    print('solution 1:', sol.solution_1())
    print('solution 2:', sol.solution_2())
    sol = Solution('2023/Day_10/test_5.txt', 'S')
    print('TEST 5')
    print('solution 1:', sol.solution_1())
    print('solution 2:', sol.solution_2())
    sol = Solution('2023/Day_10/task.txt', 'S')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 1:', sol.solution_2())


if __name__ == '__main__':
    main()
