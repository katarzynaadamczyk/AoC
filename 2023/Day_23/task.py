'''
Advent of Code 
2023 day 23
my solution to task 1 & 2 

** old version, working for task 1, for task 2 is too slow
solution 1 - 

solution 2 - 

'''
from copy import copy
from queue import PriorityQueue

class Solution:
    dot = '.'
    possible_moves = '.><v^'
    slopes = '><v^'
    slope_next = {'>': lambda point: (point[0], point[1] + 1),
                  '<': lambda point: (point[0], point[1] - 1),
                  'v': lambda point: (point[0] + 1, point[1]),
                  '^': lambda point: (point[0] - 1, point[1])}

    def __init__(self, filename) -> None:
        self.get_data(filename)


    def get_data(self, filename):
        self.hill_map = []
        with open(filename, 'r') as myfile:
            for line in myfile:
                self.hill_map.append(line.strip())
        self.start_point = (0, 1)
        self.end_point = (len(self.hill_map) - 1, len(self.hill_map[-1]) - 2)

    def get_point_value(self, point):
        return self.hill_map[point[0]][point[1]]

    def get_next_moves(self, point, visited_points):
        if self.get_point_value(point) == Solution.dot:
            for new_point in [(point[0] - 1, point[1]), (point[0] + 1, point[1]), (point[0], point[1] - 1), (point[0], point[1] + 1)]:
                if new_point not in visited_points and self.get_point_value(new_point) in Solution.possible_moves:
                    yield new_point
        elif self.get_point_value(point) in Solution.slopes:
            new_point = Solution.slope_next[self.get_point_value(point)](point)
            if new_point not in visited_points and self.get_point_value(new_point) in Solution.possible_moves:
                yield new_point 

    def get_next_moves_2(self, point, visited_points):
        if self.get_point_value(point) in Solution.possible_moves:
            for new_point in [(point[0] - 1, point[1]), (point[0] + 1, point[1]), (point[0], point[1] - 1), (point[0], point[1] + 1)]:
                if new_point not in visited_points and self.get_point_value(new_point) in Solution.possible_moves:
                    yield new_point


    def solution_1(self):
        visited_points = set()
        visited_points.add(self.start_point)
        visited_points_max_vals = dict()
        points_queue = PriorityQueue()
        points_queue.put((self.start_point, 0, visited_points))
        while not points_queue.empty():
            act_point, steps, visited_points = points_queue.get()
            if act_point == self.end_point:
                return -1 * steps
            visited_points_max_vals.setdefault(act_point, steps)
            if steps > visited_points_max_vals[act_point]:
                continue
            visited_points_max_vals[act_point] = min(visited_points_max_vals[act_point], steps)
            for new_point in self.get_next_moves(act_point, visited_points):
                new_visited_points = copy(visited_points)
                new_visited_points.add(new_point)
                points_queue.put((new_point, steps - 1, new_visited_points))
        return steps
    
    def solution_2(self):
        visited_points = set()
        visited_points.add(self.start_point)
        points_queue = PriorityQueue()
        points_queue.put((self.start_point, 0, visited_points))
        hikes_len = []
        while not points_queue.empty():
            act_point, steps, visited_points = points_queue.get()
            if act_point == self.end_point:
                hikes_len.append(-1 * steps)
                continue
            for new_point in self.get_next_moves_2(act_point, visited_points):
                new_visited_points = copy(visited_points)
                new_visited_points.add(new_point)
                points_queue.put((new_point, steps - 1, new_visited_points))
        print(hikes_len)
        return max(hikes_len)
        



def main():
    print('TASK 1')
    sol = Solution('2023/Day_23/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1())
    print('test 2:', sol.solution_2())
    sol = Solution('2023/Day_23/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
  #  print('Solution 2:', sol.solution_2())


if __name__ == '__main__':
    main()
