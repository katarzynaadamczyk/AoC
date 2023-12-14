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
            y_min = -1
            for y_max in sorted([y_cube for y_cube, x_cube in self.cube_rocks if x_cube == x]):
                round_rocks_count = len([y_round for y_round, x_round in self.round_rocks if x_round == x and y_min < y_round < y_max])
                for new_y in range(y_min + 1, round_rocks_count + y_min + 1):
                    new_rocks_set.add((new_y, x))
                y_min = y_max 
        del self.round_rocks
        self.round_rocks = new_rocks_set

    def move_south(self):
        new_rocks_set = set()
        for x in range(self.max_x):
            y_min = self.max_y
            for y_max in sorted([y_cube for y_cube, x_cube in self.cube_rocks if x_cube == x], reverse=True):
                round_rocks_count = len([y_round for y_round, x_round in self.round_rocks if x_round == x and y_min > y_round > y_max])
                for new_y in range(1, round_rocks_count + 1):
                    new_rocks_set.add((y_min - new_y, x))
                y_min = y_max
        del self.round_rocks
        self.round_rocks = new_rocks_set

    def move_west(self):
        new_rocks_set = set()
        for y in range(self.max_y):
            x_min = -1
            for x_max in sorted([x_cube for y_cube, x_cube in self.cube_rocks if y_cube == y]):
                round_rocks_count = len([x_round for y_round, x_round in self.round_rocks if y_round == y and x_min < x_round < x_max])
                for new_x in range(x_min + 1, round_rocks_count + x_min + 1):
                    new_rocks_set.add((y, new_x))
                x_min = x_max
        del self.round_rocks
        self.round_rocks = new_rocks_set

    # TO DO
    def move_east(self):
        new_rocks_set = set()
        for y in range(self.max_y):
            x_min = self.max_x
            for x_max in sorted([x_cube for y_cube, x_cube in self.cube_rocks if y_cube == y], reverse=True):
                round_rocks_count = len([x_round for y_round, x_round in self.round_rocks if y_round == y and x_min > x_round > x_max])
                for new_x in range(1, round_rocks_count + 1):
                    new_rocks_set.add((y, x_min - new_x))
                x_min = x_max
        del self.round_rocks
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
    
    
    def get_next_val(self, val, i, results):
        results_len = len(results)
        if i < results_len:
            if val in results[i:]:
                return results.index(val, i)
        return -1
    

    def check_lists(self, list_1, list_2):
        if len(list_1) != len(list_2):
            return False
        for val_1, val_2 in zip(list_1, list_2):
            if val_1 != val_2:
                return False
        return True


    def solution_2(self, cycles=1000000000, test_range=100, min_start=10):
        results = []
        for i in range(test_range):
            self.spin_cycle()
            if i % 10 == 0:
                print(i)
            results.append(self.get_result())
        first_val = results[min_start]
        next_first_vals_index = self.get_next_val(first_val, min_start + 1, results)
        if next_first_vals_index - min_start < 10:
            next_first_vals_index = self.get_next_val(first_val, next_first_vals_index + 1, results)
        while not self.check_lists(results[min_start:next_first_vals_index], results[next_first_vals_index:2 * next_first_vals_index - min_start]):
            next_first_vals_index = self.get_next_val(first_val, next_first_vals_index + 1, results)
        print(next_first_vals_index - min_start)
        print(results)
        return results[next_first_vals_index + (cycles - 1 - next_first_vals_index) % (next_first_vals_index - min_start)]


def main():
    sol = Solution('2023/Day_14/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1())
    print('test 2:', sol.solution_2())
    sol = Solution('2023/Day_14/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2(test_range=200, min_start=50))


if __name__ == '__main__':
    main()
