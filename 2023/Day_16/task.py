'''
Advent of Code 
2023 day 16
my solution to task 1 & 2

solution 1 - follow the road as in the instruction using queue and set of (point, direction) already used so that the beam does not go to an eternal cycle.
then return the count of unique points in given set

solution 2 - perform as in solution 1 for each starting point described in the task and return the highest energy value

'''
from queue import Queue

class Solution:

    EMPTY = '.'
    SPLITTER_VER = '|'
    SPLITTER_HOR = '-'
    MIRROR_DOWN = '\\'
    MIRROR_UP = '/'

    RIGHT = 'r'
    LEFT = 'l'
    UP = 'u'
    DOWN = 'd'

    # if a combination is not in change_direction_map -> direction does not change
    change_direction_map = {(RIGHT, SPLITTER_VER): (UP, DOWN),
                            (LEFT, SPLITTER_VER): (UP, DOWN),
                            (UP, SPLITTER_HOR): (LEFT, RIGHT),
                            (DOWN, SPLITTER_HOR): (LEFT, RIGHT),
                            (RIGHT, MIRROR_DOWN): (DOWN,),
                            (LEFT, MIRROR_DOWN): (UP,),
                            (UP, MIRROR_DOWN): (LEFT,),
                            (DOWN, MIRROR_DOWN): (RIGHT,),
                            (RIGHT, MIRROR_UP): (UP,),
                            (LEFT, MIRROR_UP): (DOWN,),
                            (UP, MIRROR_UP): (RIGHT,),
                            (DOWN, MIRROR_UP): (LEFT,)}
    

    get_next_point = {LEFT: lambda y, x: (y, x - 1),
                      RIGHT: lambda y, x: (y, x + 1), 
                      UP: lambda y, x: (y - 1, x),
                      DOWN: lambda y, x: (y + 1, x)}


    def __init__(self, filename) -> None:
        self.get_data(filename)
        self.min_x, self.min_y = -1, -1
        self.max_x, self.max_y = len(self.data[0]), len(self.data)


    def get_data(self, filename):
        self.data = []
        with open(filename, 'r') as myfile:
            for line in myfile:
                self.data.append(line.strip())


    def get_point(self, point, direction):
        return Solution.get_next_point[direction](point[0], point[1])
    
    
    def get_directions(self, point, direction):
        return Solution.change_direction_map.get((direction, self.data[point[0]][point[1]]), (direction,))
    
    
    def check_point(self, point):
        if not (self.min_y < point[0] < self.max_y):
            return False
        if not (self.min_x < point[1] < self.max_x):
            return False
        return True
    

    def move_beam(self, starting_point, direction):
        # queue of (point, direction)
        points_queue = Queue()
        # set of (point, direction) so that bean move ends somewhere -> if a (point, direction) is in this set then do not put it to the queue
        points_directions_set = set()
        new_directions = self.get_directions(starting_point, direction)
        for direction in new_directions:
            points_queue.put((starting_point, direction))
        points_directions_set.add((starting_point, direction))
        while not points_queue.empty():
            point, direction = points_queue.get()
            new_point = self.get_point(point, direction)
            if not self.check_point(new_point):
                continue
            new_directions = self.get_directions(new_point, direction)
            for new_direction in new_directions:
                if (new_point, new_direction) not in points_directions_set:
                    points_queue.put((new_point, new_direction))
                    points_directions_set.add((new_point, new_direction))

        return len(set([point for point, _ in points_directions_set]))

    def solution_1(self):
        return self.move_beam((0, 0), Solution.RIGHT)


    def solution_2(self):
        max_energy = 0
        # top row
        for x in range(self.max_x):
            act_energy = self.move_beam((0, x), Solution.DOWN)
            if act_energy > max_energy:
                max_energy = act_energy
        # down row
        for x in range(self.max_x):
            act_energy = self.move_beam((self.max_y - 1, x), Solution.UP)
            if act_energy > max_energy:
                max_energy = act_energy
        # leftmost column
        for y in range(self.max_y):
            act_energy = self.move_beam((y, 0), Solution.RIGHT)
            if act_energy > max_energy:
                max_energy = act_energy
        # rightmost column
        for y in range(self.max_y):
            act_energy = self.move_beam((y, self.max_x - 1), Solution.LEFT)
            if act_energy > max_energy:
                max_energy = act_energy
        return max_energy


def main():
    sol = Solution('2023/Day_16/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1())
    print('test 1:', sol.solution_2())
    sol = Solution('2023/Day_16/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 1:', sol.solution_2())


if __name__ == '__main__':
    main()
