'''
Advent of Code 
2023 day 17
my solution to task 2

solution 2 - same as task 1, with changed conditions -> crucible may go in one direction until 10 move, and it cannot turn until the no of moves
in actual direction is less than 4.

'''

from queue import PriorityQueue

class Solution:
    
    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'


    next_directions = {UP: (LEFT, RIGHT),
                       DOWN: (LEFT, RIGHT),
                       LEFT: (UP, DOWN),
                       RIGHT: (UP, DOWN)}
    

    next_point = {LEFT: lambda point: (point[0], point[1] - 1),
                  RIGHT: lambda point: (point[0], point[1] + 1),
                  UP: lambda point: (point[0] - 1, point[1]),
                  DOWN: lambda point: (point[0] + 1, point[1])}
    

    def __init__(self, filename) -> None:
        self.get_data(filename)
        self.min_x, self.min_y = -1, -1
        self.max_x, self.max_y = len(self.data[0]), len(self.data)


    def get_data(self, filename):
        self.data, self.nums, self.data_lens = [], [], []
        with open(filename, 'r') as myfile:
            for line in myfile:
                self.data.append([int(x) for x in line.strip()])


    def set_starting_values(self):
        self.start_point = (0, 0)
        self.direction = Solution.RIGHT
        self.ending_point = (self.max_y - 1, self.max_x - 1)


    def check_point(self, point):
        if not (self.min_x < point[1] < self.max_x):
            return False
        if not (self.min_y < point[0] < self.max_y):
            return False
        return True


    def get_next_point(self, point, direction):
        return Solution.next_point[direction](point)


    def get_point_value(self, point):
        return self.data[point[0]][point[1]]
    

    def make_a_move(self, result, point, direction, moves_count, moves_queue, visited_points):
        new_point = self.get_next_point(point, direction)
        if self.check_point(new_point) and (new_point, direction, moves_count + 1) not in visited_points:
            moves_queue.put((result + self.get_point_value(new_point), new_point, direction, moves_count + 1))
            visited_points.add((new_point, direction, moves_count + 1))


    def solution_1(self, limit_forward=10, min_moves_before_turning=4):
        self.set_starting_values()
        moves_queue = PriorityQueue()
        moves_queue.put((0, self.start_point, self.direction, 0))
        visited_points_with_dir = set()
        while not moves_queue.empty():
            act_result, act_point, act_direction, act_moves_count = moves_queue.get()
            print(act_result, act_point, act_direction, act_moves_count)
            if act_point == self.ending_point:
                return act_result
            if act_moves_count < limit_forward:
                self.make_a_move(act_result, act_point, act_direction, act_moves_count, moves_queue, visited_points_with_dir)
            if act_moves_count >= min_moves_before_turning:
                for new_direction in Solution.next_directions[act_direction]:
                    self.make_a_move(act_result, act_point, new_direction, 0, moves_queue, visited_points_with_dir)
        
        return 0


def main():
    print('TASK 1')
    sol = Solution('2023/Day_17/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1())
    sol = Solution('2023/Day_17/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())


if __name__ == '__main__':
    main()
