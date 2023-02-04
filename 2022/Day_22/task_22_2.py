'''
Advent of Code 
2022 day 22
my solution to tasks from day 22


solution 2 - pomysl jest taki, zeby polaczyc ze soba sciany -> przygotowac to w init w Board. a pozniej operowac podobnie jak do tej pory
do zrobienia: polaczenia Walli (wall i cube) i przeskakiwanie miedzy scianami w Cube
# TODO - klasa Cube i Wall ewentualnie
'''

import re
from itertools import product, zip_longest
from copy import copy

class Wall:
    
    no = 1
    left = '<'
    right = '>'
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
        self.left = ((x_min, y_min), (x_min, y_min + size - 1)) # line on the left, last point excluded from the wall
        self.right = ((x_min + size - 1, y_min), (x_min + size - 1, y_min + size - 1)) # line on the right, not included in the space of the wall
        self.up = ((x_min, y_min), (x_min + size - 1, y_min)) # line on the top, last point excluded from the wall
        self.bottom = ((x_min, y_min + size - 1), (x_min + size - 1, y_min + size - 1)) # line on the down, not included in the space of the wall
        
        # points demarking walls
        self.points = set([(x_min, y_min), (x_min, y_min + size - 1), (x_min + size - 1, y_min), (x_min + size - 1, y_min + size - 1)])
        
        # data needed to make a cube
        self.entrances = {self.left: Wall.left, self.right: Wall.right, self.up: Wall.up, self.bottom: Wall.down} # this is the wall and the facing in which you LEAVE this wall
        
        # data needed to operate in wall
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
    
    def __eq__(self, other):
        if other is None:
            return False
        return self.serial_no == other.serial_no and self.x_min == other.x_min and self.y_min == other.y_min and self.size == other.size
    
    def get_next_wall(self, dir):
        return self.next_walls.get(dir, None)
    
    
class Cube:
    
    # x and y are as x_offset and y_offset
    facing_to_new_x_y = {'>': lambda x, y: (x + 1, y),
                         'v': lambda x, y: (x, y + 1),
                         '<': lambda x, y: (x - 1, y),
                         '^': lambda x, y: (x, y - 1)
                         }
    
    facings_opposites = {'>': '<',
                         '<': '>',
                         '^': 'v',
                         'v': '^'
                         }
    
    simple_offset_change = {'<>': lambda x, y, size: (0, y),
                            '><': lambda x, y, size: (size - 1, y),
                            'v^': lambda x, y, size: (x, size - 1),
                            '^v': lambda x, y, size: (x, 0),
                            '>v': lambda x, y, size: (y, size - 1),
                            'v>': lambda x, y, size: (size - 1, x),
                            '^<': lambda x, y, size: (y, 0),
                            '<^': lambda x, y, size: (0, x),
                            '>>': lambda x, y, size: (size - 1, y),
                            '<<': lambda x, y, size: (0, y)
                            }
    
    regular_offset_change = {'<>': lambda x, y, size: (x, size - 1 - y),
                            '><': lambda x, y, size: (x, size - 1 - y),
                            'v^': lambda x, y, size: (x, size - 1),
                            '^v': lambda x, y, size: (x, 0),
                            '>v': lambda x, y, size: (y, x),
                            'v>': lambda x, y, size: (y, x),
                            '^<': lambda x, y, size: (y, 0),
                            '<^': lambda x, y, size: (0, x),
                            '>>': lambda x, y, size: (x, size - 1 - y),
                            '<<': lambda x, y, size: (0, size - 1 - y)
                            }
    
    
    facing_connections = [(Wall.up, Wall.right, Wall.left, Wall.down),
                          (Wall.right, Wall.up, Wall.down, Wall.left),
                          (Wall.up, Wall.right, Wall.down, Wall.right),
                          (Wall.up, Wall.left, Wall.down, Wall.left),
                          (Wall.right, Wall.down, Wall.right, Wall.up)] #, (), (), ()] # fill TODO
        
    
    facings = ['>', 'v', '<', '^']
    len_facings = 4
    
    def manhattan_distance(point_1, point_2):
        return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])
    
    def __init__(self, new_map, size):
        self.map = new_map
        self.walls = []
        self.x_offset = new_map[0].find('.') % size
        self.y_offset = 0
        self.size = size
        Wall.reset_serial_no()
        for y in range(0, len(new_map), size):
            for x in range(0, len(new_map[y]), size):
                if new_map[y][x] != ' ':
                    self.walls.append(Wall(x, y, size))
            
        # setting actual wall to the first wall found
        self.act_wall = self.walls[0]
        
        # actualize walls left, right, top, bottom
        # first just touching walls on the map
        for i, wall_1 in enumerate(self.walls):
            for wall_2 in self.walls[i+1:]:
                common_points_1 = []
                common_points_2 = []
                for point_1, point_2 in product(wall_1.points, wall_2.points):
                    if Cube.manhattan_distance(point_1, point_2) <= 2:
                        common_points_1.append(point_1)
                        common_points_2.append(point_2)
                if len(common_points_1) == 2:
                    common_points_1 = tuple(sorted(common_points_1))
                    common_points_2 = tuple(sorted(common_points_2))
                    point_1_entrance = wall_1.entrances[common_points_1]
                    point_2_entrance = wall_2.entrances[common_points_2]
                    self.create_connection(wall_1, point_1_entrance, wall_2, point_2_entrance, Cube.simple_offset_change)
        
        no_of_it = 0
      #  self.walls = self.walls[1:] + self.walls[:1]
        while not self.all_connections_closed():
            # TODO 
            # just close all connections and it will be done ;)
            no_of_it += 1
            for dir_1, entr_1, dir_2, entr_2 in Cube.facing_connections:
                for i, wall_1 in enumerate(self.walls):
                    for wall_2 in self.walls[i+1:]:
                        if self.check_if_may_create_connection(wall_1, dir_1, entr_1, wall_2, dir_2, entr_2):
                            print('#####', wall_1, wall_2, dir_1, dir_2, entr_1, entr_2)
                            self.create_connection(wall_1, entr_1, wall_2, entr_2, Cube.regular_offset_change)
                            break
                        if self.check_if_may_create_connection(wall_2, dir_1, entr_1, wall_1, dir_2, entr_2): 
                            print('#####', wall_1, wall_2, dir_1, dir_2, entr_1, entr_2)
                            self.create_connection(wall_2, entr_1, wall_1, entr_2, Cube.regular_offset_change)
                            break
                        
            if no_of_it > 10:
                break
        #
        print('iterations: ', no_of_it)
        for wall in self.walls:
            print(wall)
            print(wall.next_walls)
            print(wall.facings_change)
            print(wall.offsets_change)
        
        self.changes = {}
            
    def all_connections_closed(self):
        for wall in self.walls:
            if None in wall.next_walls.values():
                return False
        return True
    
    def check_if_may_create_connection(self, wall_1, dir_1, entr_1, wall_2, dir_2, entr_2):
        if wall_1.get_next_wall(dir_1) and wall_2.get_next_wall(dir_2) and wall_1.get_next_wall(entr_1) is None and wall_2.get_next_wall(entr_2) is None:
            if wall_1.get_next_wall(dir_1) == wall_2.get_next_wall(dir_2):
                return True
        return False
    
    def create_connection(self, wall_1, entr_1, wall_2, entr_2, offset_change):
        wall_1.next_walls[entr_1] = wall_2
        wall_2.next_walls[entr_2] = wall_1
        wall_1.facings_change[entr_1] = Cube.facings_opposites[entr_2]
        wall_2.facings_change[entr_2] = Cube.facings_opposites[entr_1]
        wall_1.offsets_change[entr_1] = offset_change[entr_2 + entr_1]
        wall_2.offsets_change[entr_2] = offset_change[entr_1 + entr_2]
    
    def get_act_y(self):
        return self.act_wall.get_min_y() + self.y_offset
    
    def get_act_x(self):
        return self.act_wall.get_min_x() + self.x_offset
    
    def get_new_position(self, facing):
        new_x, new_y = Cube.facing_to_new_x_y[facing](self.x_offset, self.y_offset)
        if 0 <= new_x < self.size and 0 <= new_y < self.size:
            return self.act_wall, new_x, new_y, facing
       # print('old:', self.act_wall, self.x_offset, self.y_offset, facing)
        new_facing = self.act_wall.facings_change[facing]
        new_x, new_y = self.act_wall.offsets_change[facing](self.x_offset, self.y_offset, self.size)
        new_wall = self.act_wall.next_walls[facing]
       # print('new:', new_wall, new_x, new_y, new_facing)
        self.changes.setdefault((self.act_wall.serial_no, new_wall.serial_no), ((self.x_offset, self.y_offset, facing), (new_x, new_y, new_facing)))
        return new_wall, new_x, new_y, new_facing
    
    # move for single walk value
    def move(self, walk, facing):
        for _ in range(walk):
            new_wall, new_x_offset, new_y_offset, new_facing = self.get_new_position(facing)
            if self.map[new_wall.get_min_y()+new_y_offset][new_wall.get_min_x()+new_x_offset] == '.':
                self.x_offset = new_x_offset
                self.y_offset = new_y_offset
                facing = new_facing
                self.act_wall = new_wall
            else:
                break
        return facing
        

class Simulation:
    
    points_for_facing = {'>': 0, 'v': 1, '<': 2, '^': 3}
    facings = ['>', 'v', '<', '^']
    len_facings = 4
    directions_to_facings = {'R': lambda face: Simulation.facings[(Simulation.facings.index(face) + 1) % Simulation.len_facings],
                             'L': lambda face: Simulation.facings[(Simulation.facings.index(face) - 1) % Simulation.len_facings],
                             'O': lambda face: face} # for the last one, 'O' will be the filler for zip_longest
    
    
    def __init__(self, new_map, dirs, cube_size):
       # self.map = new_map
        self.dirs = dirs[0]
        self.walks = dirs[1]
        self.facing = '>'
        self.cube = Cube(new_map, cube_size)
    
    def simulate(self):
      #  i = 0
        for walk, turn in zip_longest(self.walks, self.dirs, fillvalue='O'):
            #print(self.cube.act_wall)
            self.facing = self.cube.move(walk, self.facing)
            self.facing = Simulation.directions_to_facings[turn](self.facing)
       #     i += 1
        #    if i > 100:
         #       break
    
    def get_the_password(self):
        return 1000 * (self.cube.get_act_y() + 1) + 4 * (self.cube.get_act_x() + 1) + Simulation.points_for_facing[self.facing]



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
    for key, item in solution_board.cube.changes.items():
        print(key)
        print(item)
    return solution_board.get_the_password()

  
def main():
    #test_map, test_dirs = get_map('2022/Day_22/test_map.txt'), get_dirs('2022/Day_22/test_dirs.txt') 
    #print('test 2:', solution_2(test_map, test_dirs, 4))
    task_map, task_dirs = get_map('2022/Day_22/task_map.txt'), get_dirs('2022/Day_22/task_dirs.txt') 
    print('Solution 2:', solution_2(task_map, task_dirs, 50))
    
    
if __name__ == '__main__':
    main()
    