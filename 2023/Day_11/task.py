'''
Advent of Code 
2023 day 11
my solution to task 1 & 2

solution 1 & 2 - first search for empty lines on x axis. Then iterate over y, if galaxy in line then add points changing x if necessary, then add
1 to y, if no galaxy in this y position then add expanding number. When it is done, then combine each pair of galaxies and count their manhattan
distance.

'''
from itertools import combinations

class Solution:

    
    def __init__(self, filename, char, how_many = 2) -> None:
        self.get_data(filename)
        self.galaxies, self._empty_x = [], set()
        for x in range(len(self.data[0])):
            if char not in ''.join([line[x] for line in self.data]):
                self._empty_x.add(x)
        y = 0
        for line in self.data:
            if char in line:
                for x, val in enumerate(line):
                    if val == char:
                        self.galaxies.append((y, x + (how_many - 1) * len([val for val in self._empty_x if val < x])))
                y += 1
            else: 
                y += how_many 
        

    def get_data(self, filename):
        self.data = []
        with open(filename, 'r') as myfile:
            for line in myfile:
                self.data.append(line.strip())

    def manhattan_distance(self, point_1, point_2):
        return abs(point_2[0] - point_1[0]) + abs(point_2[1] - point_1[1])
    

    def solution_1(self):
        results = []
        for point_1, point_2 in combinations(self.galaxies, 2):
            results.append(self.manhattan_distance(point_1, point_2))
        return sum(results)


def main():
    print('TASK 1')
    sol = Solution('2023/Day_11/test.txt', '#')
    print('TEST 1')
    print('solution 1:', sol.solution_1())
    sol = Solution('2023/Day_11/task.txt', '#')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('TASK 2')
    sol = Solution('2023/Day_11/test.txt', '#', 10)
    print('TEST 1 - 10')
    print('solution 1:', sol.solution_1())
    sol = Solution('2023/Day_11/test.txt', '#', 100)
    print('TEST 2 - 100')
    print('solution 1:', sol.solution_1())
    sol = Solution('2023/Day_11/task.txt', '#', 1000000)
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())


if __name__ == '__main__':
    main()
