'''
Advent of Code 
2022 day 22
my solution to tasks from day 22


solution 2 - pomysl jest taki, zeby polaczyc ze soba sciany -> przygotowac to w init w Board. a pozniej operowac podobnie jak do tej pory
30.01 -> robię przygotowanie klasy Board oprócz łączenia ze sobą Wallsów

'''

import re
from itertools import zip_longest
from copy import copy

class Wall:
    
    no = 1
    left = '>'
    right = '<'
    up = '^'
    down = 'v'
    
    def __init__(self, x_min, y_min, size) -> None:
        # standard info regarding the wall -> x, y starting, the size and serial no just for me to check if everything works properly
        self.x_min = x_min
        self.y_min = y_min
        self.size = size
        self.serial_no = Wall.no
        Wall.no += 1
        
        # lines demarking this wall 
        self.left = ((x_min, y_min), (x_min, y_min + size)) # line on the left, last point excluded from the wall
        self.right = ((x_min + size, y_min), (x_min + size, y_min + size)) # line on the right, not included in the space of the wall
        self.up = ((x_min, y_min), (x_min + size, y_min)) # line on the top, last point excluded from the wall
        self.bottom = ((x_min, y_min + size), (x_min + size, y_min + size)) # line on the down, not included in the space of the wall
        
        # data needed to operate in wall
        self.entrances = {self.left: Wall.left, self.right: Wall.right, self.up: Wall.down, self.bottom: Wall.up} # if you enter this way, this is how facing changes
        
        self.next_walls = {Wall.left: None, Wall.right: None, Wall.down: None, Wall.up: None} # pointers to next walls when reaching the end of given facing
        self.facings_change = copy(self.next_walls) # how changes the facing when going to new next wall
        self.offsets_change = copy(self.next_walls) # how offset changes when reaching new wall 
        
    
    def __repr__(self) -> str:
        return 'Wall ' + str(self.serial_no) + ': ' + str((self.x_min, self.y_min, self.size))

    def __str__(self) -> str:
        return 'Wall ' + str(self.serial_no) + ': ' + str((self.x_min, self.y_min, self.size))
        
    def reset_serial_no():
        Wall.no = 1
        
    def get_min_y(self):
        return self.y_min
    
    def get_min_x(self):
        return self.x_min
    
    
class Cube:
    
    # check if this is needed
    facing_to_new_x_y = {'>': lambda x, y, task_map: ((x + 1) % len(task_map[y]), y),
                         'v': lambda x, y, task_map: (x, (y + 1) % len(task_map)),
                         '<': lambda x, y, task_map: ((x - 1) % len(task_map[y]), y),
                         '^': lambda x, y, task_map: (x, (y - 1) % len(task_map))
                         }
    
    def __init__(self, new_map, size):
        self.walls = []
        Wall.reset_serial_no()
        for y in range(0, len(new_map), size):
            for x in range(0, len(new_map[y]), size):
                if new_map[y][x] != ' ':
                    self.walls.append(Wall(x, y, size))
        for wall in self.walls:
            print(wall)
            
        # setting actual wall to the first wall found
        self.act_wall = self.walls[0]
        
        # actualize walls left, right, top, bottom
        # TODO
    
    def get_act_y(self, y_offset):
        return self.act_wall.get_min_y() + y_offset
    
    def get_act_x(self, x_offset):
        return self.act_wall.get_min_x() + x_offset
    
    def get_new_position(self, x_offset, y_offset, facing):
        # TODO
        return x_offset, y_offset, facing
        

class Simulation:
    
    points_for_facing = {'>': 0, 'v': 1, '<': 2, '^': 3}
    facings = ['>', 'v', '<', '^']
    len_facings = 4
    directions_to_facings = {'R': lambda face: Simulation.facings[(Simulation.facings.index(face) + 1) % Simulation.len_facings],
                             'L': lambda face: Simulation.facings[(Simulation.facings.index(face) - 1) % Simulation.len_facings],
                             'O': lambda face: face} # for the last one, 'O' will be the filler for zip_longest
    
    
    def __init__(self, new_map, dirs, cube_size):
        self.map = new_map
        self.dirs = dirs[0]
        self.walks = dirs[1]
        self.facing = '>'
        self.x_offset = new_map[0].find('.') % cube_size
        self.y_offset = 0
        self.cube = Cube(new_map, cube_size)
    
    # get new x and y positions
    def get_where_to_go(self):
        return self.cube.get_new_position(self.x_offset, self.y_offset, self.facing)
    
    # move for single walk value
    def move(self, walk):
        for _ in range(walk):
            new_x, new_y, new_facing = self.get_where_to_go()
            if self.map[new_y][new_x] == '.':
                self.x_offset = new_x
                self.y_offset = new_y
                self.facing = new_facing
            else:
                break
    
    def simulate(self):
        for walk, turn in zip_longest(self.walks, self.dirs, fillvalue='O'):
            self.move(walk)
            self.facing = Simulation.directions_to_facings[turn](self.facing)
    
    def get_the_password(self):
        return 1000 * (self.cube.get_act_y(self.y_offset) + 1) + 4 * (self.cube.get_act_x(self.x_offset) + 1) + Simulation.points_for_facing[self.facing]



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
    solution_board = Simulation(task_map, task_dirs, cube_size)
    solution_board.simulate()
    return solution_board.get_the_password()

  
def main():
    test_map, test_dirs = get_map('2022/Day_22/test_map.txt'), get_dirs('2022/Day_22/test_dirs.txt') 
    print('test 1:', solution_2(test_map, test_dirs, 4))
    task_map, task_dirs = get_map('2022/Day_22/task_map.txt'), get_dirs('2022/Day_22/task_dirs.txt') 
    print('Solution 1:', solution_2(task_map, task_dirs, 50))
    
    
if __name__ == '__main__':
    main()
    