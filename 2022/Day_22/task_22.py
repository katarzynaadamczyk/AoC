'''
Advent of Code 
2022 day 22
my solution to tasks from day 22


solution 1 - 
solution 2 - 

'''

import re
from itertools import zip_longest


class Board:
    
    points_for_facing = {'>': 0, 'v': 1, '<': 2, '^': 3}
    facings = ['>', 'v', '<', '^']
    len_facings = 4
    directions_to_facings = {'R': lambda face: Board.facings[(Board.facings.index(face) + 1) % Board.len_facings],
                             'L': lambda face: Board.facings[(Board.facings.index(face) - 1) % Board.len_facings],
                             'O': lambda face: face} # for the last one, 'O' will be the filler for zip_longest
    
    
    def __init__(self, new_map, dirs):
        self.map = new_map
        self.dirs = dirs[0]
        self.walks = dirs[1]
        self.x = self.map[0].find('.')
        self.y = 0
        self.facing = '>'
    
    # get chunk of map where the walk shoud be
    def get_where_to_go(self):
        if self.facing == '>':
            print(self.map[self.y][self.x + 1:].strip() + self.map[self.y][:self.x].strip())
            return self.map[self.y][self.x + 1:].strip() + self.map[self.y][:self.x].strip()
        elif self.facing == '<':
            pass
        elif self.facing == 'v':
            pass
        elif self.facing == '^':
            pass
    
    # move for single walk value
    def move(self, walk):
        self.get_where_to_go()
        pass
    
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
    return new_map 

def get_dirs(filename):
    dirs, walks = [], []
    with open(filename, 'r') as myfile:
        line = myfile.readline().strip()
        walks = [int(i) for i in re.findall(r"\d+", line)]
        dirs = re.findall(r'[RL]{1}', line)
    return (dirs, walks)


def solution_1(task_map, task_dirs):
    solution_board = Board(task_map, task_dirs)
    solution_board.simulate()
    return solution_board.get_the_password()

  
def main():
    test_map, test_dirs = get_map('2022/Day_22/test_map.txt'), get_dirs('2022/Day_22/test_dirs.txt') 
    print('test 1:', solution_1(test_map, test_dirs))
   # task_map, task_dirs = get_map('2022/Day_22/task_map.txt'), get_dirs('2022/Day_22/task_dirs.txt') 
   # print('Solution 1:', solution_1(task_map, task_dirs))
    
    
if __name__ == '__main__':
    main()
    