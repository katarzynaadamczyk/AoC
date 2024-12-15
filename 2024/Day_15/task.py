'''
Advent of Code 
2024 day 15
my solution to task 1 only

first create a set of all boxes locations and another set of walls locations 
and keep robot postion

task 1 - for each direction in directions:
            check for all boxes that will / could be moved
            check if last position is not a wall
            then move robot and maybe some boxes
        at the end sum GPS of all boxes positions 

'''

from tqdm import tqdm


class Solution:

    def __init__(self, filename) -> None:
        self.robot_position = (0, 0)
        self.boxes, self.walls = set(), set()
        self.moves_sequence = []
        self.get_data(filename)
        self.directions = {'>': (0, 1),
                           '<': (0, -1),
                           '^': (-1, 0),
                           'v': (1, 0)}

    def get_data(self, filename):
        if_map = True
        with open(filename, 'r') as myfile:
            for y, line in enumerate(myfile):
                if if_map:
                    if line == '\n':
                        if_map = False
                        continue
                    for x, val in enumerate(line.strip()):
                        if val == '@':
                            self.robot_position = (y, x)
                            continue
                        if val == '#':
                            self.walls.add((y, x))
                            continue
                        if val == 'O':
                            self.boxes.add((y, x))
                else:
                    self.moves_sequence.append(line.strip())


    def get_next_point(self, point, direction):
        return (point[0] + self.directions[direction][0], point[1] + self.directions[direction][1])

    def get_set_of_boxes_to_move(self, point, direction):
        boxes_to_move = set()
        act_point = self.get_next_point(point, direction)
        while act_point in self.boxes:
            boxes_to_move.add(act_point)
            act_point = self.get_next_point(act_point, direction)
        return boxes_to_move, act_point not in self.walls

    def let_robot_move(self):
        for direction in tqdm(''.join(self.moves_sequence)):
            boxes_to_move, can_move = self.get_set_of_boxes_to_move(self.robot_position, direction)
            if can_move:
                self.robot_position = self.get_next_point(self.robot_position, direction)
                self.boxes = self.boxes.difference(boxes_to_move)
                for box in boxes_to_move:
                    self.boxes.add(self.get_next_point(box, direction))

    def get_GPS(self, position):
        return 100 * position[0] + position[1]
    
    def solution_1(self) -> int:
        self.let_robot_move()
        return sum([self.get_GPS(position) for position in self.boxes])
    

    
    def solution_2(self) -> int:
        result = 0
        return result


    

def main():

    print('TEST 1')
    sol = Solution('2024/Day_15/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal ?')
 #   print('test 1:', sol.solution_2(), 'should equal ?')
    print('TEST 2')
    sol = Solution('2024/Day_15/test_2.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal ?')
 #   print('test 1:', sol.solution_2(), 'should equal ?')
    sol = Solution('2024/Day_15/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1()) 
 #   print('Solution 2:', sol.solution_2()) 
   


if __name__ == '__main__':
    main()
