'''
Advent of Code 
2023 day 14
my solution to task 1 & 2

solution 1 - 

solution 2 - 

'''


class Solution:

    
    def __init__(self, filename, round_char='O', cube_char='#') -> None:
        self.get_data(filename)
        self.cube_rocks = self.get_rocks(cube_char)
        self.round_rocks = self.get_rocks(round_char)
        self.add_rocks_at_edges()

    def get_data(self, filename):
        self.data = []
        with open(filename, 'r') as myfile:
            for line in myfile:
                self.data.append(line.strip())
        self.min_x, self.max_x = 0, len(self.data[0])
        self.min_y, self.max_y = 0, len(self.data)

    def get_rocks(self, char):
        rocks_set = set()
        for y, line in enumerate(self.data):
            for x, val in enumerate(line):
                if val == char:
                    rocks_set.add((y, x))
        return rocks_set
    
    def add_rocks_at_edges(self):
        # add south line of rocks
        for x in range(self.max_x):
            self.cube_rocks.add((self.max_y, x))
        # add north line of rocks
        for x in range(self.max_x):
            self.cube_rocks.add((-1, x))
        # add west line of rocks
        for y in range(self.max_y):
            self.cube_rocks.add((y, -1))
        # add east line of rocks
        for y in range(self.max_y):
            self.cube_rocks.add((y, self.max_x))

    def move_north(self):
        new_rocks_set = set()
        for x in range(self.max_x):
            y_min = 0
            for y_max in sorted([y_cube for y_cube, x_cube in self.cube_rocks if x_cube == x]):
                round_rocks_count = len([y_round for y_round, x_round in self.round_rocks if x_round == x and y_min <= y_round < y_max])
                for new_y in range(y_min, round_rocks_count + y_min):
                    new_rocks_set.add((new_y, x))
                y_min = y_max + 1
        self.round_rocks = new_rocks_set

    # TO DO
    def move_south(self):
        new_rocks_set = set()
        for x in range(self.max_x):
            y_min = 0
            for y_max in sorted([y_cube for y_cube, x_cube in self.cube_rocks if x_cube == x]):
                round_rocks_count = len([y_round for y_round, x_round in self.round_rocks if x_round == x and y_min <= y_round < y_max])
                for new_y in range(y_min, round_rocks_count + y_min):
                    new_rocks_set.add((new_y, x))
                y_min = y_max + 1
        self.round_rocks = new_rocks_set

    # TO DO
    def move_west(self):
        new_rocks_set = set()
        for x in range(self.max_x):
            y_min = 0
            for y_max in sorted([y_cube for y_cube, x_cube in self.cube_rocks if x_cube == x]):
                round_rocks_count = len([y_round for y_round, x_round in self.round_rocks if x_round == x and y_min <= y_round < y_max])
                for new_y in range(y_min, round_rocks_count + y_min):
                    new_rocks_set.add((new_y, x))
                y_min = y_max + 1
        self.round_rocks = new_rocks_set

    # TO DO
    def move_east(self):
        new_rocks_set = set()
        for x in range(self.max_x):
            y_min = 0
            for y_max in sorted([y_cube for y_cube, x_cube in self.cube_rocks if x_cube == x]):
                round_rocks_count = len([y_round for y_round, x_round in self.round_rocks if x_round == x and y_min <= y_round < y_max])
                for new_y in range(y_min, round_rocks_count + y_min):
                    new_rocks_set.add((new_y, x))
                y_min = y_max + 1
        self.round_rocks = new_rocks_set
    
    def spin_cycle(self):
        self.move_north()
        self.move_west()
        self.move_south()
        self.move_east()

    def get_result(self):
        return sum([self.max_y - y for y, _ in self.round_rocks])

    def solution_1(self):
        self.move_north()
        return self.get_result()


def main():
    sol = Solution('2023/Day_14/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1())
    sol = Solution('2023/Day_14/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())


if __name__ == '__main__':
    main()
