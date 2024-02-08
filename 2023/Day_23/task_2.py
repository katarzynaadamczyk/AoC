'''
Advent of Code 
2023 day 23
my solution to task 1 & 2 

** new, working well version
solution 1 as in task 1
solution 2 - first, shorten map -> make a dict of points which lead to other points and keep their distance in (point_1: [(point_2, distance),
(point_3, distance)]). Then go using priority queue and keep the number of steps so far * (-1) as priority. End the while loop when there is 10 
final distances and return lowest of them multiplied by -1. 


'''
from copy import copy
from queue import PriorityQueue, Queue

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

    def get_next_moves_3(self, point, last_point):
        if self.get_point_value(point) in Solution.possible_moves:
            for new_point in [(point[0] - 1, point[1]), (point[0] + 1, point[1]), (point[0], point[1] - 1), (point[0], point[1] + 1)]:
                if new_point != last_point and self.get_point_value(new_point) in Solution.possible_moves:
                    yield new_point
    

    def shorten_hike_map_2(self):
        self.short_hike_map_2 = dict()
        hike_queue = Queue()
        visited_points = set()
        visited_points.add(self.start_point)
        hike_queue.put((self.start_point, self.start_point))
        while not hike_queue.empty():
            act_point, new_point = hike_queue.get()
            if act_point == self.end_point or new_point == self.end_point:
                continue
            self.short_hike_map_2.setdefault(act_point, dict())
            steps = 0 if act_point == new_point else 1
            next_points = list(self.get_next_moves_3(new_point, act_point))
            while len(next_points) == 1 and next_points[0] != self.end_point:
                steps += 1
                visited_points.add(next_points[0])
                last_point = next_points[0]
                next_points = list(self.get_next_moves_3(last_point, new_point))
                new_point = last_point
            if len(next_points) == 1:
                self.short_hike_map_2.setdefault(next_points[0], dict())
                self.short_hike_map_2[act_point].setdefault(next_points[0], steps + 1)
                self.short_hike_map_2[next_points[0]].setdefault(act_point, steps + 1)
            else:
                self.short_hike_map_2.setdefault(last_point, dict())
                self.short_hike_map_2[act_point].setdefault(last_point, steps)
                self.short_hike_map_2[last_point].setdefault(act_point, steps)
                for point in next_points:
                    if point not in visited_points:
                        visited_points.add(point)
                        hike_queue.put((last_point, point))





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
        self.shorten_hike_map_2()
        hikes_lens = []
        hikes_queue = PriorityQueue()
        visited_points = set()
        visited_points.add(self.start_point)
        hikes_queue.put((0, self.start_point, visited_points))
        while not hikes_queue.empty():
            act_step, act_point, visited_points = hikes_queue.get()
            if act_point == self.end_point:
                hikes_lens.append(act_step)
                if len(hikes_lens) > 10: # to end the program
                    break
            for point, steps in self.short_hike_map_2[act_point].items():
                if point not in visited_points:
                    new_visited_points = copy(visited_points)
                    new_visited_points.add(point)
                    hikes_queue.put((act_step - steps, point, new_visited_points))
       # print(hikes_lens)
        return -1 * min(hikes_lens)
        



def main():
    print('TASK 1')
    sol = Solution('2023/Day_23/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1())
    print('test 2:', sol.solution_2())
    sol = Solution('2023/Day_23/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2())


if __name__ == '__main__':
    main()
