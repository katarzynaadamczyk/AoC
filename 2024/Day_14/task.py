'''
Advent of Code 
2024 day 14
my solution to tasks

task 1 - using math operations calculate position of each robot after 100 s, divide robots into 4 groups and 
multiply len of the groups together
task 2 - first approach was to brute force each second and save picture of it and look through all pictures to find the Christmas Tree
second approach -> after getting positions 
                search for first 4 lines of Christmas Tree, 
                if it is in positions set then save the picture and return time


'''

from tqdm import tqdm
import numpy as np
from PIL import Image


class Solution:

    def __init__(self, filename) -> None:
        self.robots = {}
        self.get_data(filename)
    
    def get_num_values(self, line):
        return [int(x) for x in line[line.find('=')+1:].split(',')]   
        

    def get_data(self, filename):
        robot_index = 0
        with open(filename, 'r') as myfile:
            for line in myfile:
                point, velocity = line.strip().split()
                self.robots.setdefault(robot_index, {'start': self.get_num_values(point),
                                                     'velocity': self.get_num_values(velocity)})
                robot_index += 1
   
    def get_robot_final_position(self, robot, max_x, max_y, seconds):
        final_x = (robot['start'][0] + seconds * robot['velocity'][0]) % max_x
        final_y = (robot['start'][1] + seconds * robot['velocity'][1]) % max_y
        return (final_x, final_y)
    
    def check_if_there_is_a_tree(self, positions):
        for point in positions:
            new_set = set()
            for y in range(4):
                for x in range(point[0] - y - 1, point[0] + y + 2):
                    new_set.add((x, point[1] + y))
            if len(new_set.difference(positions)) == 0:
                return True
        return False
    
    def save_an_image(self, positions, max_x, max_y, second):
        new_array = []
        for y in range(max_y):
            new_line = []
            for x in range(max_x):
                if (x, y) in positions:
                    new_line.append(1)
                else:
                    new_line.append(0)
            new_array.append(new_line)
        new_array = np.array(new_array)
        data = Image.fromarray((new_array * 255).astype(np.uint8))
        data.save(str(second) + '.png')

    
    def solution_1(self, max_x=101, max_y=103, seconds=100) -> int:
        up_left_points, up_right_points, down_left_points, down_right_points = [], [], [], []
        x_line, y_line = max_x // 2, max_y // 2 
        for robot in tqdm(self.robots.values()):
            final_position = self.get_robot_final_position(robot, max_x, max_y, seconds)
            if final_position[0] < x_line and final_position[1] < y_line:
                up_left_points.append(final_position)
            elif final_position[0] < x_line and final_position[1] > y_line:
                down_left_points.append(final_position)
            elif final_position[0] > x_line and final_position[1] < y_line:
                up_right_points.append(final_position)
            elif final_position[0] > x_line and final_position[1] > y_line:
                down_right_points.append(final_position)
        return len(up_left_points) * len(up_right_points) * len(down_left_points) * len(down_right_points)
    

    
    def solution_2(self, max_x=101, max_y=103) -> int:
        for sec in tqdm(range(0, 10000)):
            positions = set()
            for robot in self.robots.values():
                positions.add(self.get_robot_final_position(robot, max_x, max_y, sec))
            if self.check_if_there_is_a_tree(positions):
                self.save_an_image(positions, max_x, max_y, sec)
                return sec
        return 0


    

def main():

    print('TASK 1')
    sol = Solution('2024/Day_14/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(max_x=11, max_y=7), 'should equal 12')
 #   print('test 1:', sol.solution_2(max_x=11, max_y=7), 'should equal ?')
    sol = Solution('2024/Day_14/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1()) 
    print('Solution 2:', sol.solution_2()) 
   


if __name__ == '__main__':
    main()
