'''
Advent of Code 
2023 day 13
my solution to task 1 & 2

solution 1 - 

solution 2 - 

'''
from itertools import combinations

class Solution:

    
    def __init__(self, filename) -> None:
        self.get_data(filename)
        

    def get_data(self, filename):
        self.data = []
        with open(filename, 'r') as myfile:
            line = myfile.readline()
            while line:
                new_map = []
                while line and line != '\n':
                    new_map.append(line.strip())
                    line = myfile.readline()
                self.data.append(new_map)
                line = myfile.readline()

    def check_lines(self, line_1, line_2):
        return True if line_1 == line_2 else False

    def check_horizontal(self, act_map):
        max_i = len(act_map)
        for i in range(max_i - 1):
            if self.check_lines(act_map[i], act_map[i + 1]):
                down, up, reflection = 1, 2, True
                while i - down >= 0 and i + up < max_i:
                    if not self.check_lines(act_map[i - down], act_map[i + up]):
                        reflection = False
                        break
                    down += 1
                    up += 1
                if reflection:
                    return i + 1
        return 0
    
    def check_vertical(self, act_map):
        return self.check_horizontal([[act_map[y][x] for y in range(len(act_map))] for x in range(len(act_map[0]))])

    def solution_1(self):
        results = []
        for act_map in self.data:
            results.append(self.check_vertical(act_map) + 100 * self.check_horizontal(act_map))
        return sum(results)
    
    def check_lines_2(self, line_1, line_2):
        diff_count = 0
        for char_1, char_2 in zip(line_1, line_2):
            if char_1 != char_2:
                diff_count += 1
        return diff_count

    
    def check_horizontal_2(self, act_map):
        max_i = len(act_map)
        for i in range(max_i - 1):
            if self.check_lines_2(act_map[i], act_map[i + 1]) <= 1:
                down, up, reflection = 1, 2, self.check_lines_2(act_map[i], act_map[i + 1])
                while i - down >= 0 and i + up < max_i:
                    reflection += self.check_lines_2(act_map[i - down], act_map[i + up])
                    down += 1
                    up += 1
                if reflection == 1:
                    return i + 1
        return 0
    
    def check_vertical_2(self, act_map):
        return self.check_horizontal_2([[act_map[y][x] for y in range(len(act_map))] for x in range(len(act_map[0]))])


    def solution_2(self):
        results = []
        for act_map in self.data:
            results.append(self.check_vertical_2(act_map) + 100 * self.check_horizontal_2(act_map))
        return sum(results)


def main():
    sol = Solution('2023/Day_13/test.txt')
    print('TEST 1')
    print('Test 1:', sol.solution_1())
    print('Test 1:', sol.solution_2())
    sol = Solution('2023/Day_13/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2())


if __name__ == '__main__':
    main()
