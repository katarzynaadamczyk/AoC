'''
Advent of Code 
2022 day 24
my solution to tasks from day 24


solution 1 - podzielic na dwie mapy -> down/up i left/right. zrobic tyle map ile jest powtarzajacych sie a pozniej zrobic sciezke i zwrocic w ilu iteracjach udalo sie ja zrobic
robienie sciezki - sprawdzanie na obu odpowiednich mapach czy jest puste i jak tak to dodawanie do sciezki. sciezka jako set tupli (x, y)
solution 2 - 

'''
from queue import PriorityQueue
from copy import deepcopy

class Solution:
    
    new_positions = {'>': lambda x, y, max_x, max_y: ((x + 1) % max_x, y),
                     '<': lambda x, y, max_x, max_y: ((x - 1) % max_x, y),
                     'v': lambda x, y, max_x, max_y: (x, (y + 1) % max_y),
                     '^': lambda x, y, max_x, max_y: (x, (y - 1) % max_y),
                     }
    
    diagonals = '^v'
    verticals = '><'
    
    def __init__(self, new_map) -> None:
        self.x = 0
        self.y = 0
        self.x_goal = len(new_map[-1]) - 1
        self.y_goal = len(new_map) - 1
        self.map = new_map
        self.len_verticals = len(new_map[0])
        self.len_diagonals = len(new_map) - 2
        self.map_diagonals = [[[val if val not in Solution.verticals else '.' for val in row] for row in self.map[1:-1]]]
        self.map_verticals = [[[val if val not in Solution.diagonals else '.' for val in row] for row in self.map[1:-1]]]
        self.map_diagonals = self.move_blizzards(self.map_diagonals, self.len_diagonals)
        self.map_verticals = self.move_blizzards(self.map_verticals, self.len_verticals)
        self.map = [self.map[0]] + [['.' for _ in range(len(row))] for row in self.map[1:-1]] + [self.map[-1]] 
        self.map[0][0] = '.'
        self.map[-1][-1] = '.'
    
    def solve(self):
        # data needed for looping -> initial minutes and set of points
        minutes, set_of_points = 0, set()
        set_of_points.add((self.x, self.y))
        # the 'magic'
        while len(set_of_points):
            minutes += 1
            new_set_of_points = set()
            for x, y in set_of_points:
                for new_x, new_y in self.check_where_to_go(minutes, x, y):
                    if new_x == self.x_goal and new_y == self.y_goal:
                        return minutes
                    new_set_of_points.add((new_x, new_y))
            set_of_points = new_set_of_points

        return -1
    
    def solve_get_back_snacks(self):
        minutes, set_of_points, goals = 0, set(), [(self.x_goal, self.y_goal), (0, 0), (self.x_goal, self.y_goal)]
        set_of_points.add((self.x, self.y))
        act_goal = 0
        # the 'magic'
        while len(set_of_points):
            minutes += 1
            new_set_of_points = set()
            goal_reached = False
            for x, y in set_of_points:
                for new_x, new_y in self.check_where_to_go(minutes, x, y):
                    if new_x == goals[act_goal][0] and new_y == goals[act_goal][1]:
                        act_goal += 1
                        goal_reached = True
                        if act_goal == len(goals):
                            return minutes
                        new_set_of_points = set()
                        new_set_of_points.add((new_x, new_y))
                        break
                    new_set_of_points.add((new_x, new_y))
                if goal_reached:
                    break
            set_of_points = new_set_of_points

        return -1
    
    def check_other_maps(self, minute, x, y):
        if y == 0 or y == len(self.map) - 1:
            if self.map[y][x] == '.':
                return True
            else:
                return False
        if self.map_diagonals[minute % self.len_diagonals][y - 1][x] == '.' and self.map_verticals[minute % self.len_verticals][y - 1][x] == '.':
            return True
        return False
    
    def check_where_to_go(self, minute, x, y):
        if self.check_other_maps(minute, x, y):
            yield x, y
        if 0 <= x - 1 < len(self.map[y]) and self.check_other_maps(minute, x - 1, y): # and self.map[y][x-1] != '#' 
            yield x - 1, y
        if 0 <= x + 1 < len(self.map[y]) and self.check_other_maps(minute, x + 1, y):
            yield x + 1, y
        if 0 <= y - 1 < len(self.map) and self.check_other_maps(minute, x, y - 1):
            yield x, y - 1
        if 0 <= y + 1 < len(self.map) and self.check_other_maps(minute, x, y + 1):
            yield x, y + 1
    
    def move_blizzards(self, act_map, minutes):
        # iterate over all minutes
        for _ in range(minutes - 1):
            # prepare an empty new map with all places filled with '.'
            new_map = [['.' for _ in range(len(row))] for row in act_map[-1]]
            # for each blizzard in previous map add corresponding blizzard to a new one
            for y, row in enumerate(act_map[-1]): # previous map
                for x, data in enumerate(row):
                    if data != '.':
                        for blizzard in data:
                            new_x, new_y = Solution.new_positions[blizzard](x, y, len(row), len(act_map[-1]))
                            if new_map[new_y][new_x] == '.':
                                new_map[new_y][new_x] = blizzard
                            else:
                                new_map[new_y][new_x] += blizzard
            # append new map to act_map
            act_map.append(new_map)
        return act_map
        

def get_map(filename):
    new_map = []
    with open(filename, 'r') as myfile:
        for line in myfile:
            tmp = []
            line = line[1:-2]
            for char in line:
                if char == '.':
                    tmp.append('')
                else:
                    tmp.append(char)
            new_map.append(tmp)
    return new_map 


def solution_1(task_map):
    solver = Solution(task_map)
    return solver.solve()


def solution_2(task_map):
    solver = Solution(task_map)
    return solver.solve_get_back_snacks()


  
def main():
    test_map_1, test_map_2 = get_map('2022/Day_24/test_1.txt'), get_map('2022/Day_24/test_2.txt')
    print('test 1:', solution_1(test_map_1))
    print('test 1:', solution_1(test_map_2))
    task_map = get_map('2022/Day_24/task.txt')
    print('Solution 1:', solution_1(task_map))
    print('test 2:', solution_2(test_map_1))
    print('test 2:', solution_2(test_map_2))
    print('Solution 2:', solution_2(task_map))
    
    
if __name__ == '__main__':
    main()
    