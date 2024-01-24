'''
Advent of Code 
2023 day 22
my solution to task 1 & 2 

solution 1 - 

'''

from typing import Type

class Brick:
    def __init__(self, line: str, name: int) -> None:
        line = line.split('~')
        line = [x.split(',') for x in line]
        self.min_x = line[0][0]
        self.max_x = line[1][0]
        self.min_y = line[0][1]
        self.max_y = line[1][1]
        self.min_z = line[0][2]
        self.max_z = line[1][2]
        self.next = []
        self.name = name

    def move_down(self, min_val: int):
        self.min_z -= 1
        self.max_z -= 1
        if self.min_z == min_val:
            return True
        return False
    
    def is_inside(self, second_brick): # : Type[Brick]):
        pass




class Solution:

    def __init__(self, filename) -> None:
        self.get_data(filename)


    def get_data(self, filename):
        self.nodes, self.points = {}, {}
        with open(filename, 'r') as myfile:
            line = myfile.readline()
            while line and line != '\n':
                line = line.strip()
                node_name = line[:line.find('{')]
                line = line[line.find('{') + 1:-1]
                new_node = self.process_test(line)
                self.nodes[node_name] = new_node
                line = myfile.readline()


    def solution_1(self):
        return 0


def main():
    print('TASK 1')
    sol = Solution('2023/Day_22/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1())
    sol = Solution('2023/Day_22/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())


if __name__ == '__main__':
    main()
