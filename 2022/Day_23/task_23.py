'''
Advent of Code 
2022 day 23
my solution to tasks from day 23


solution 1 - 
solution 2 - 

'''
from copy import copy

class Elf:
    
    directions = ['N', 'S', 'W', 'E']
    
    def __init__(self, position) -> None:
        self.position = position
        self.directions = copy(Elf.directions)
            
    def get_position(self):
        return self.position
        
    def get_directions(self):
        return self.directions
    
    def move(self, point):
        self.position = point
        self.directions = self.directions[1:] + self.directions[:1]
        
    def __repr__(self):
        return 'Elf on pos: ' + str(self.position)
    
    def __str__(self):
        return 'Elf on pos: ' + str(self.position)
    
class Board:
    
    positions_to_check = {'N': lambda point: set([(point[0] + i, point[1] - 1) for i in range(-1, 2)]),
                          'S': lambda point: set([(point[0] + i, point[1] + 1) for i in range(-1, 2)]),
                          'W': lambda point: set([(point[0] + 1, point[1] + i) for i in range(-1, 2)]),
                          'E': lambda point: set([(point[0] - 1, point[1] + i) for i in range(-1, 2)])}
    
    new_positions = {'N': lambda point: (point[0], point[1] - 1),
                     'S': lambda point: (point[0], point[1] + 1),
                     'W': lambda point: (point[0] + 1, point[1]),
                     'E': lambda point: (point[0] - 1, point[1])}
    
    new_x_y = {'N': lambda y: y - 1,
               'S': lambda y: y + 1, 
               'W': lambda x: x + 1,
               'E': lambda x: x - 1}

    def __init__(self, elves_positions) -> None:
        self.Elves = [Elf(position) for position in elves_positions]
        self.actual_positions = elves_positions
    
    def get_max_x(self):
        return max(self.actual_positions, key=lambda point: point[0])[0]
    
    def get_max_y(self):
        return max(self.actual_positions, key=lambda point: point[1])[1]
    
    def get_min_y(self):
        return min(self.actual_positions, key=lambda point: point[1])[1]
    
    def get_min_x(self):
        return min(self.actual_positions, key=lambda point: point[0])[0]
    
    def get_set_for_row_and_columns(self):
        dict_of_sets = {}
        for x in range(self.get_min_x(), self.get_max_x() + 1):
            dict_of_sets.setdefault('x' + str(x), set(filter(lambda point: point[0] == x, self.actual_positions)))
        for y in range(self.get_min_y(), self.get_max_y() + 1):
            dict_of_sets.setdefault('y' + str(y), set(filter(lambda point: point[0] == x, self.actual_positions)))
        return dict_of_sets
    
    def elf_may_stay(self, elf):
        return [self.elf_may_move(elf, direction) for direction in elf.get_directions()]
    
    def elf_may_move(self, elf, direction):
        # TODO
        if direction in ['S', 'N']:
            new_y = Board.new_x_y[direction](elf.get_position()[1])
            if not 'y' + str(new_y) in self.dict_of_positions.keys() or \
                len(self.dict_of_positions['y' + str(new_y)].intersection(Board.positions_to_check[direction](elf.get_position()))) == 0:
                    return True
        else:
            new_x = Board.new_x_y[direction](elf.get_position()[0])
            if not 'x' + str(new_x) in self.dict_of_positions.keys() or \
                len(self.dict_of_positions['x' + str(new_x)].intersection(Board.positions_to_check[direction](elf.get_position()))) == 0:
                    return True
        return False
    
    def get_new_position(self, elf, move_table):
        #print(elf.get_directions()) # bug in there
        return Board.new_positions[elf.get_directions().index(move_table.index(True))](elf.get_position())    
    
    def elves_go(self):
        # part 1
        # prepare a dict of sets for each line and column
        self.dict_of_positions = self.get_set_for_row_and_columns()
        self.new_elves_positions = {}
        for elf in self.Elves:
            move_table = self.elf_may_stay(elf)
            if sum(move_table) < 4:
                new_position = self.get_new_position(elf, move_table)
                self.new_elves_positions.setdefault(new_position, set())
                self.new_elves_positions[new_position].add(elf)
        
        # part 2
        for position, elves in self.new_elves_positions:
            if len(elves) == 1:
                for elf in elves:
                    elf.move(position)
        self.actual_positions = set([elf.get_position() for elf in self.Elves])
                        
    

def get_elves_positions(filename):
    elves_positions, y = set(), 0
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line.strip()
            for x, char in enumerate(line):
                if char == '#':
                    elves_positions.add((x, y))
            y += 1
            
    return elves_positions


def solution_1(elves_positions, no_of_iterations):
    board = Board(elves_positions)
    for _ in range(no_of_iterations):
        board.elves_go()
    return (board.get_max_x() - board.get_min_x() + 1) * (board.get_max_y() - board.get_min_y() + 1)


  
def main():
    test_positions = get_elves_positions('2022/Day_23/test.txt')
    print('test 1:', solution_1(test_positions, 10))
    task_positions = get_elves_positions('2022/Day_23/task.txt')
    print('Solution 1:', solution_1(task_positions, 10))
 #   print('test 2:', solution_2(test_results, test_monkey_operations, 'root', 'humn'))
 #   print('Solution 2:', solution_2(task_results, task_monkey_operations, 'root', 'humn'))
    
    
if __name__ == '__main__':
    main()
    