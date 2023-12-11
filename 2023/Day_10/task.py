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
    
    @staticmethod 
    def north_east(y, x):
        return (y - 1, x + 1)
    
    @staticmethod 
    def north_west(y, x):
        return (y - 1, x - 1)
    
    @staticmethod 
    def south_east(y, x):
        return (y + 1, x + 1)
    
    @staticmethod 
    def south_west(y, x):
        return (y + 1, x - 1)

    pipes = {'|': (north, south), 
             '-': (east, west),
             'L': (north, east),
             'J': (north, west),
             '7': (south, west),
             'F': (south, east)}
    
    pipe_types = '|-LJ7F'

    LEFT = 'LEFT'
    DOWN = 'DOWN'
    RIGHT = 'RIGHT'
    UP = 'UP'

    orientations = [LEFT, DOWN, RIGHT, UP]

    solution_2_check_points = {(RIGHT, RIGHT): (north,),
                   (RIGHT, DOWN): (north, east, north_east),
                   (RIGHT, UP): (north_west,),
                   (UP, UP): (west,),
                   (UP, LEFT): (south_west,),
                   (UP, RIGHT): (west, north, north_west),
                   (LEFT, LEFT): (south,),
                   (LEFT, UP): (south, west, south_west),
                   (LEFT, DOWN): (south_east,),
                   (DOWN, DOWN): (east,),
                   (DOWN, LEFT): (east, south, south_east),
                   (DOWN, RIGHT): (north_east,)}

    next_point = {LEFT: west,
                  RIGHT: east,
                  UP: north,
                  DOWN: south}
    
    change_orientation = {(LEFT, '-'): LEFT,
                          (RIGHT, '-'): RIGHT,
                          (LEFT, 'L'): UP,
                          (LEFT, 'F'): DOWN,
                          (UP, 'F'): RIGHT,
                          (DOWN, 'L'): RIGHT,
                          (RIGHT, '7'): DOWN,
                          (RIGHT, 'J'): UP,
                          (UP, '|'): UP,
                          (DOWN, '|'): DOWN,
                          (UP, '7'): LEFT,
                          (DOWN, 'J'): LEFT}
    
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

    def get_value(self, point):
        return self.data[point[0]][point[1]]
    
    def reject_surroundings(self):
        self.solution_2_start_point = None
        for x in range(self.map_constraits_x_max):
            y = 0
            while y < self.map_constraits_y_max and (y, x) not in self.visited_points.keys():
                self.points_to_exclude.add((y, x))
                y += 1
            if self.solution_2_start_point is None and (y, x) in self.visited_points.keys():
                self.solution_2_start_point = (y, x)
            if y < self.map_constraits_y_max:
                y = self.map_constraits_y_max - 1
                while y > self.map_constraits_y_min and (y, x) not in self.visited_points.keys():
                    self.points_to_exclude.add((y, x))
                    y -= 1
        for y in range(1, self.map_constraits_y_max - 1):
            x = 0
            while x < self.map_constraits_x_max and (y, x) not in self.visited_points.keys():
                self.points_to_exclude.add((y, x))
                x += 1
            if x < self.map_constraits_x_max:
                x = self.map_constraits_x_max - 1
                while x > self.map_constraits_x_min and (y, x) not in self.visited_points.keys():
                    self.points_to_exclude.add((y, x))
                    x -= 1
    
    def solution_2_get_next(self, point, orientation):
        new_point = Solution.next_point[orientation](point[0], point[1])
       # print(new_point)
        new_orientation = Solution.change_orientation[(orientation, self.get_value(new_point))]
        return new_point, new_orientation
    
    def check_points(self, starting_check_point):
        if self.check_point(starting_check_point):
            while not (starting_check_point in self.visited_points or starting_check_point in self.points_to_exclude):
                self.points_to_exclude.add(starting_check_point)
                self.check_points(Solution.east(starting_check_point[0], starting_check_point[1]))
                self.check_points(Solution.west(starting_check_point[0], starting_check_point[1]))
                self.check_points(Solution.south(starting_check_point[0], starting_check_point[1]))
                self.check_points(Solution.north(starting_check_point[0], starting_check_point[1]))
                self.check_points(Solution.south_east(starting_check_point[0], starting_check_point[1]))
                self.check_points(Solution.south_west(starting_check_point[0], starting_check_point[1]))
                self.check_points(Solution.north_east(starting_check_point[0], starting_check_point[1]))
                self.check_points(Solution.north_west(starting_check_point[0], starting_check_point[1]))

    def follow_new_line(self):
        act_point = self.solution_2_start_point
        if self.get_value(act_point) in '-F':
            orientation = Solution.RIGHT # no need to implement others as all tests and task start with 'F'
            self.check_points(Solution.north(act_point[0], act_point[1]))
        new_line_set = set()
        while act_point not in new_line_set:
            new_line_set.add(act_point)
            act_point, new_orientation = self.solution_2_get_next(act_point, orientation)
            for point in Solution.solution_2_check_points[(orientation, new_orientation)]:
                self.check_points(point(act_point[0], act_point[1]))
            orientation = new_orientation





    def solution_2(self):
        self.points_to_exclude = set()
        self.change_start_point()
        self.reject_surroundings()
        self.follow_new_line()


        print('total_points:', self.map_constraits_x_max * self.map_constraits_y_max)
        print('exclude:', len(self.points_to_exclude))
        print('visited:', len(self.visited_points))
        print('first_point:', self.solution_2_start_point, self.get_value(self.solution_2_start_point))

        return self.map_constraits_x_max * self.map_constraits_y_max - len(self.visited_points) - len(self.points_to_exclude)
    


def main():
    sol = Solution('2023/Day_10/test_1.txt', 'S')
    print('TEST 1')
    print('solution 1:', sol.solution_1())
    print('solution 2:', sol.solution_2(), '? 1')
    sol = Solution('2023/Day_10/test_2.txt', 'S')
    print('TEST 2')
    print('solution 1:', sol.solution_1())
    print('solution 2:', sol.solution_2(), '? 1')
    sol = Solution('2023/Day_10/test_3.txt', 'S')
    print('TEST 3')
    print('solution 1:', sol.solution_1())
    print('solution 2:', sol.solution_2(), '? 4')
    sol = Solution('2023/Day_10/test_4.txt', 'S')
    print('TEST 4')
    print('solution 1:', sol.solution_1())
    print('solution 2:', sol.solution_2(), '? 8')
    sol = Solution('2023/Day_10/test_5.txt', 'S')
    print('TEST 5')
    print('solution 1:', sol.solution_1())
    print('solution 2:', sol.solution_2(), '? 10')
    sol = Solution('2023/Day_10/task.txt', 'S')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2())


if __name__ == '__main__':
    main()
