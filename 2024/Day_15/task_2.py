'''
Advent of Code 
2024 day 15
my solution to task 2 - more complicated than task 1 so another file

first create a set of boxes_left, boxes_right and walls positions and keep robot position as well

task 2 - for each direction:
            prepare set of all possible left positions of boxes and check if robot (and boxes) can move
            if so update boxes_left, boxes_right and robot_position
        return sum of GPS for boxes_left positions 

'''

from tqdm import tqdm
import numpy as np
from PIL import Image


class Solution:

    def __init__(self, filename) -> None:
        self.robot_position = (0, 0)
        self.walls = set()
        self.boxes_left, self.boxes_right = set(), set()
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
                        self.max_y = y
                        continue
                    for x, val in enumerate(line.strip()):
                        if val == '@':
                            self.robot_position = (y, 2 * x)
                            continue
                        if val == '#':
                            self.walls.add((y, 2 * x))
                            self.walls.add((y, 2 * x + 1))
                            continue
                        if val == 'O':
                            self.boxes_left.add((y, 2 * x))
                            self.boxes_right.add((y, 2 * x + 1))
                    self.max_x = 2 * (x + 1)
                else:
                    self.moves_sequence.append(line.strip())


    def get_next_point(self, point, direction):
        '''
        classically get next point by adding direction to point
        '''
        return (point[0] + self.directions[direction][0], point[1] + self.directions[direction][1])
    
    def get_right_box_point(self, box_left_point):
        '''
        given box left point return box right point
        '''
        return (box_left_point[0], box_left_point[1] + 1)

    def get_next_box_points(self, point, direction, if_robot_move=False):
        '''
        given point, direction and if we get next box after robot (if_robot_move=True) or box(if_robot_move=False)
        return possible next points for left side of a box
        '''
        if direction == '>' and if_robot_move:
            return [(point[0], point[1] + self.directions[direction][1])]
        if direction in ['<', '>']:
            return [(point[0], point[1] + 2 * self.directions[direction][1])]
        possible_points = [(point[0] + self.directions[direction][0], point[1]),
                           (point[0] + self.directions[direction][0], point[1] - 1)]
        if not if_robot_move:
            possible_points.append((point[0] + self.directions[direction][0], point[1] + 1))
        return possible_points
        
    
    def check_possible_boxes_points(self, points):
        '''
        given all possible points for left side of boxes check which of them are really left side of boxes and return them
        '''
        possible_points = []
        for point in points:
            if point in self.boxes_left:
                possible_points.append(point)
        return possible_points
    
    def save_an_image(self, second=0):
        '''
        function to visualize actual positions of boxes and robot -> needed for debugging
        '''
        new_array = []
        for y in range(self.max_y):
            new_line = []
            for x in range(self.max_x):
                if (y, x) in self.boxes_left:
                    new_line.append('[')
                elif (y, x) in self.boxes_right:
                    new_line.append(']')
                elif (y, x) == self.robot_position:
                    new_line.append('@')
                elif (y, x) in self.walls:
                    new_line.append('#')
                else:
                    new_line.append('.')
            new_array.append(new_line)
        print(second)
        for line in new_array:
            print(''.join(line))
        print()


    def save_an_image_2(self, second=0):
        '''
        function to save an image of actual positions of boxes and robot
        '''
        new_array = []
        for y in range(self.max_y):
            new_line = []
            for x in range(self.max_x):
                if (y, x) in self.boxes_left or (y, x) in self.boxes_right:
                    new_line.append(1)
                elif (y, x) == self.robot_position:
                    new_line.append(0.75)
                elif (y, x) in self.walls:
                    new_line.append(0.25)
                else:
                    new_line.append(0)
            new_array.append(new_line)
        new_array = np.array(new_array)
        data = Image.fromarray((new_array * 255).astype(np.uint8))
        data.save(str(second) + '.png')

    def get_set_of_boxes_to_move(self, start_point, direction):
        '''
        given actual robot position and direction get all boxes that will move with robot and if robot and boxes can actually move
        '''
        if self.get_next_point(start_point, direction) in self.walls:
            return set(), False
        boxes_to_move = set()
        new_left_points = self.check_possible_boxes_points(self.get_next_box_points(start_point, direction, True))
        while len(new_left_points) > 0:
            boxes_to_move = boxes_to_move.union(set(new_left_points))
            new_new_left_points = set()
            for point in new_left_points:
                new_new_left_points = new_new_left_points.union(self.check_possible_boxes_points(self.get_next_box_points(point, direction)))
            new_left_points = new_new_left_points
        can_move = True
        for point in boxes_to_move:
            if self.get_next_point(point, direction) in self.walls or \
                self.get_next_point(self.get_right_box_point(point), direction) in self.walls:
                can_move = False
                break
        return boxes_to_move, can_move

    def let_robot_move(self):
        '''
        move robot for each direction in self.moves_sequence
        in each iteration update boxes_left, boxes_right and robot_position
        '''
        for i, direction in tqdm(enumerate(''.join(self.moves_sequence))):
            boxes_to_move, can_move = self.get_set_of_boxes_to_move(self.robot_position, direction)
            if can_move:
                self.robot_position = self.get_next_point(self.robot_position, direction)
                self.boxes_left = self.boxes_left.difference(boxes_to_move)
                boxes_to_move_right = set([self.get_right_box_point(box) for box in boxes_to_move])
                self.boxes_right = self.boxes_right.difference(boxes_to_move_right)
                for left, right in zip(boxes_to_move, boxes_to_move_right):
                    self.boxes_left.add(self.get_next_point(left, direction))
                    self.boxes_right.add(self.get_next_point(right, direction))

    def get_GPS(self, box):
        '''
        return GPS of given box location
        '''
        return 100 * box[0] + box[1]
    
    def solution_2(self) -> int:
        '''
        get result for task 2
        '''
        self.let_robot_move()
        print(self.robot_position)
        self.save_an_image()
        self.save_an_image_2()
        return sum([self.get_GPS(box) for box in self.boxes_left])
    


    

def main():

    print('TEST 1')
    sol = Solution('2024/Day_15/test_2.txt')
    print('TEST 1')
 #   print('test 1:', sol.solution_1(), 'should equal ?')
    print('test 1:', sol.solution_2(), 'should equal ?')
    sol = Solution('2024/Day_15/task.txt')
    print('SOLUTION')
 #   print('Solution 1:', sol.solution_1()) 
    print('Solution 2:', sol.solution_2()) 
   


if __name__ == '__main__':
    main()
