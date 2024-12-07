'''
Advent of Code 
2024 day 6
my solution to tasks
task 1 & 2 - general idea as in task but this is a brute force solution -> in each iteration get new position with new direction
brute foce solution


'''

from tqdm import tqdm


class Solution:
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    no_of_directions = 4

    def __init__(self, filename) -> None:
        self.lab_map = []
        self.start_position, self.direction = (0, 0), Solution.directions[0]
        self.get_data(filename)
        self.min_x, self.min_y, self.max_x, self.max_y = 0, 0, len(self.lab_map[0]) - 1, len(self.lab_map) - 1

    def get_data(self, filename):
        with open(filename, 'r') as myfile:
            for i, line in enumerate(myfile):
                if '^' in line:
                    self.start_position = (i, line.find('^'))
                self.lab_map.append(line.strip())

    def get_next_direction(self):
        return Solution.directions[(Solution.directions.index(self.direction) + 1) % Solution.no_of_directions]
    
    def get_next_position(self, act_position):
        new_position = (act_position[0] + self.direction[0], act_position[1] + self.direction[1])
        if not (self.min_y <= new_position[0] <= self.max_y and self.min_x <= new_position[1] <= self.max_x):
            raise ValueError('lab exited')
            
        if self.lab_map[new_position[0]][new_position[1]] == '#':
            return act_position, self.get_next_direction()
        return new_position, self.direction

    
       
    def solution_1(self) -> int:
        set_of_visited_positions = set([self.start_position])
        act_position = self.start_position
        while True:
            try:
                act_position, self.direction = self.get_next_position(act_position)
            except ValueError:
                break
            set_of_visited_positions.add(act_position)
        self.positions_to_check = set_of_visited_positions.difference(set([self.start_position]))
        return len(set_of_visited_positions)

    
    def solution_2(self) -> int:
        result = 0
        self.lst_of_obstacles = set()
        for obstacle in tqdm(self.positions_to_check):
            self.lab_map[obstacle[0]] = self.lab_map[obstacle[0]][:obstacle[1]] + '#' + self.lab_map[obstacle[0]][obstacle[1]+1:]
            set_of_visited_positions = set([self.start_position])
            act_position = self.start_position
            self.direction = Solution.directions[0]
            while True:
                try:
                    act_position, self.direction = self.get_next_position(act_position)
                except ValueError:
                    break
                if (self.direction, act_position) in set_of_visited_positions:
                    result += 1
                    self.lst_of_obstacles.add(obstacle)
                    break
                set_of_visited_positions.add((self.direction, act_position))
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
