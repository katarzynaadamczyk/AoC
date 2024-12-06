'''
Advent of Code 
2024 day 6
my solution to tasks
task 1 - 

'''
from tqdm import tqdm

class Solution:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    positions = [UP, RIGHT, DOWN, LEFT]
    no_of_positions = 4

    def __init__(self, filename) -> None:
        self.lab_map = []
        self.start_position, self.direction = (0, 0), Solution.UP
        self.get_data(filename)
        self.min_x, self.min_y, self.max_x, self.max_y = 0, 0, len(self.lab_map[0]) - 1, len(self.lab_map) - 1

    def get_data(self, filename):
        with open(filename, 'r') as myfile:
            for i, line in enumerate(myfile):
                if '^' in line:
                    self.start_position = (i, line.find('^'))
                self.lab_map.append(line.strip())

    def get_next_position(self, act_position):
        return (Solution.positions.index(act_position) + 1) % Solution.no_of_positions
    
    def get_next_stop_up(self, act_position):
        route = ''.join([self.lab_map[i][act_position[1]] for i in range(act_position[0] - 1, self.min_y - 1, -1)])
        next_stop = route.find('#')
        if next_stop >= 0:
            return (act_position[0] - next_stop, act_position[1])
        return (self.min_y, act_position[1])
    
    def get_next_stop_right(self, act_position):
        route = self.lab_map[act_position[0]][act_position[1] + 1:]
        next_stop = route.find('#')
        if next_stop >= 0:
            return (act_position[0], act_position[1] + next_stop)
        return (act_position[0], self.max_x)
    
    def get_next_stop_down(self, act_position):
        route = ''.join([self.lab_map[i][act_position[1]] for i in range(act_position[0] + 1, self.max_y + 1)])
        next_stop = route.find('#')
        if next_stop >= 0:
            return (act_position[0] + next_stop, act_position[1])
        return (self.max_y, act_position[1])
    
    def get_next_stop_left(self, act_position):
        route = self.lab_map[act_position[0]][:act_position[1]]
        next_stop = route.rfind('#')
        if next_stop >= 0:
            return (act_position[0], next_stop + 1)
        return (act_position[0], self.max_x)
    
    def put_to_set(self, act_position, new_position, set_of_positions):
        if self.direction in (Solution.LEFT, Solution.RIGHT):
            for i in range(min(act_position[1], new_position[1]), max(act_position[1], new_position[1]) + 1):
                set_of_positions.add((act_position[0], i))
        else:
            for i in range(min(act_position[0], new_position[0]), max(act_position[0], new_position[0]) + 1):
                set_of_positions.add((i, act_position[1]))
        return set_of_positions

    
    def solution_1(self) -> int:
        self.dir_move_dict = {Solution.UP: self.get_next_stop_up,
                         Solution.RIGHT: self.get_next_stop_right,
                         Solution.DOWN: self.get_next_stop_down,
                         Solution.LEFT: self.get_next_stop_left}
        self.dir_end_dict = {Solution.UP: lambda position: True if position[0] == self.min_y else False,
                         Solution.RIGHT: lambda position: True if position[1] == self.max_x else False,
                         Solution.DOWN: lambda position: True if position[0] == self.max_y else False,
                         Solution.LEFT: lambda position: True if position[1] == self.min_x else False}
        set_of_visited_positions = set()
        act_position = self.start_position
        new_direction = Solution.UP
        while not self.dir_end_dict[self.direction](act_position):
            self.direction = new_direction
            new_position = self.dir_move_dict[self.direction](act_position)
            set_of_visited_positions = self.put_to_set(act_position, new_position, set_of_visited_positions)
            new_direction = self.get_next_position(self.direction)
            act_position = new_position
        self.positions_to_check = set_of_visited_positions.difference(set([self.start_position]))
        return len(set_of_visited_positions)

    
    def solution_2(self) -> int:
        result = 0
        self.lst_of_obstacles = set()
        for obstacle in tqdm(self.positions_to_check):
            self.lab_map[obstacle[0]] = self.lab_map[obstacle[0]][:obstacle[1]] + '#' + self.lab_map[obstacle[0]][obstacle[1]+1:]
            set_of_visited_positions = set()
            act_position = self.start_position
            new_direction = Solution.UP
            while not self.dir_end_dict[self.direction](act_position):
                if (self.direction, act_position) in set_of_visited_positions:
                    result += 1
                    self.lst_of_obstacles.add(obstacle)
                    break
                set_of_visited_positions.add((self.direction, act_position))
                self.direction = new_direction
                new_position = self.dir_move_dict[self.direction](act_position)
                new_direction = self.get_next_position(self.direction)
                act_position = new_position
            self.lab_map[obstacle[0]] = self.lab_map[obstacle[0]][:obstacle[1]] + '.' + self.lab_map[obstacle[0]][obstacle[1]+1:]
        return result

    def solution_2_2(self) -> int:
        result = 0
        for obstacle in self.positions_to_check:
            self.lab_map[obstacle[0]] = self.lab_map[obstacle[0]][:obstacle[1]] + '#' + self.lab_map[obstacle[0]][obstacle[1]+1:]
            possible_positions = set([(obstacle[0] + 1, obstacle[1]), (obstacle[0] - 1, obstacle[1]), (obstacle[0], obstacle[1] + 1), (obstacle[0], obstacle[1] - 1)])
            set_of_visited_positions = set()
            act_position = self.start_position
            new_direction = Solution.UP
            while not self.dir_end_dict[self.direction](act_position):
                self.direction = new_direction
                new_position = self.dir_move_dict[self.direction](act_position)
                if new_position in possible_positions:
                    if (self.direction, new_position) in set_of_visited_positions:
                        result += 1
                        break
                    set_of_visited_positions.add((self.direction, new_position))
                new_direction = self.get_next_position(self.direction)
                act_position = new_position
            self.lab_map[obstacle[0]] = self.lab_map[obstacle[0]][:obstacle[1]] + '.' + self.lab_map[obstacle[0]][obstacle[1]+1:]
        return result


    

def main():

    print('TASK 1')
    sol = Solution('2024/Day_6/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 41')
    print('test 1:', sol.solution_2(), 'should equal 6')
    sol = Solution('2024/Day_6/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2()) # 2269 too high
   


if __name__ == '__main__':
    main()
