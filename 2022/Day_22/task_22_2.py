'''
Advent of Code 
2022 day 22
my solution to tasks from day 22


solution 1 - 
solution 2 - 

'''

import re
from itertools import zip_longest

class Wall:
    
    no = 1
    
    def __init__(self, x_min, y_min, size) -> None:
        self.x_min = x_min
        self.y_min = y_min
        self.size = size
        self.serial_no = Wall.no
        Wall.no += 1
        self.up, self.down, self.left, self.right = None, None, None, None
    
    def __repr__(self) -> str:
        return 'Wall ' + str(self.serial_no) + ': ' + str((self.x_min, self.y_min, self.size))

    def __str__(self) -> str:
        return 'Wall ' + str(self.serial_no) + ': ' + str((self.x_min, self.y_min, self.size))
    
    def set_up(self, other):
        self.up = other
    
    def set_down(self, other):
        self.down = other
        
    def reset_serial_no():
        Wall.no = 1
    
class Cube:
    def __init__(self, new_map, size):
        self.walls = []
        Wall.reset_serial_no()
        for y in range(0, len(new_map), size):
            for x in range(0, len(new_map[y]), size):
                if new_map[y][x] != ' ':
                    self.walls.append(Wall(x, y, size))
        for wall in self.walls:
            print(wall)
        

class Board:
    
    points_for_facing = {'>': 0, 'v': 1, '<': 2, '^': 3}
    facings = ['>', 'v', '<', '^']
    len_facings = 4
    directions_to_facings = {'R': lambda face: Board.facings[(Board.facings.index(face) + 1) % Board.len_facings],
                             'L': lambda face: Board.facings[(Board.facings.index(face) - 1) % Board.len_facings],
                             'O': lambda face: face} # for the last one, 'O' will be the filler for zip_longest
    facing_to_new_x_y = {'>': lambda x, y, task_map: ((x + 1) % len(task_map[y]), y),
                         'v': lambda x, y, task_map: (x, (y + 1) % len(task_map)),
                         '<': lambda x, y, task_map: ((x - 1) % len(task_map[y]), y),
                         '^': lambda x, y, task_map: (x, (y - 1) % len(task_map))
                         }
    
    def __init__(self, new_map, dirs, cube_size):
        self.map = new_map
        self.dirs = dirs[0]
        self.walks = dirs[1]
        self.x = self.map[0].find('.')
        self.y = 0
        self.facing = '>'
        self.cube = Cube(new_map, cube_size)
    
    # get new x and y positions
    def get_where_to_go(self):
        new_x, new_y = Board.facing_to_new_x_y[self.facing](self.x, self.y, self.map)
        while self.map[new_y][new_x] == ' ':
            new_x, new_y = Board.facing_to_new_x_y[self.facing](new_x, new_y, self.map)
        return new_x, new_y
    
    # move for single walk value
    def move(self, walk):
        for _ in range(walk):
            new_x, new_y = self.get_where_to_go()
            if self.map[new_y][new_x] == '.':
                self.x = new_x
                self.y = new_y
            else:
                break
    
    def simulate(self):
        for walk, turn in zip_longest(self.walks, self.dirs, fillvalue='O'):
            self.move(walk)
            self.facing = Board.directions_to_facings[turn](self.facing)
    
    def get_the_password(self):
        return 1000 * (self.y + 1) + 4 * (self.x + 1) + Board.points_for_facing[self.facing]



def get_map(filename):
    new_map = []
    with open(filename, 'r') as myfile:
        for line in myfile:
            new_map.append(line.strip('\n'))
    max_len = max([len(row) for row in new_map])
    new_map = [row.ljust(max_len) for row in new_map]
    return new_map 

def get_dirs(filename):
    dirs, walks = [], []
    with open(filename, 'r') as myfile:
        line = myfile.readline().strip()
        walks = [int(i) for i in re.findall(r"\d+", line)]
        dirs = re.findall(r'[RL]{1}', line)
    return (dirs, walks)


def solution_2(task_map, task_dirs, cube_size):
    solution_board = Board(task_map, task_dirs, cube_size)
    solution_board.simulate()
    return solution_board.get_the_password()

  
def main():
    test_map, test_dirs = get_map('2022/Day_22/test_map.txt'), get_dirs('2022/Day_22/test_dirs.txt') 
    print('test 1:', solution_2(test_map, test_dirs, 4))
    task_map, task_dirs = get_map('2022/Day_22/task_map.txt'), get_dirs('2022/Day_22/task_dirs.txt') 
    print('Solution 1:', solution_2(task_map, task_dirs, 50))
    
    
if __name__ == '__main__':
    main()
    