'''
Advent of Code 
2024 day 8
my solution to tasks
task 1 - calculate manhattan distance and add it to first and substract it from the second location to get two antinodes locations
for each antinode if they are in the map, if so add to results set
task 2 - add antennas locations to antinodes location set, then keep adding / substracting to location1/location2 until gone off the map
(while in the map add to results set) 


'''

from tqdm import tqdm
from itertools import combinations

class Solution:

    def __init__(self, filename) -> None:
        self.antennas_locations = {}
        self.get_data(filename)
        self.min_x, self.min_y = 0, 0

    def get_data(self, filename):
        with open(filename, 'r') as myfile:
            for y, line in enumerate(myfile):
                self.max_x = len(line.strip()) - 1
                self.max_y = y
                for x, char in enumerate(line.strip()):
                    if char != '.':
                        self.antennas_locations.setdefault(char, set())
                        self.antennas_locations[char].add((y, x))
    
    def get_difference(self, location1, location2):
        return (location1[0] - location2[0], location1[1] - location2[1])
    
    def get_new_locations(self, location1, location2):
        diff = self.get_difference(location1, location2)
        return (location1[0] + diff[0], location1[1] + diff[1]), (location2[0] - diff[0], location2[1] - diff[1])

    
    def solution_1(self) -> int:
        results = set()
        for locations in tqdm(self.antennas_locations.values()):
            for location1, location2 in combinations(locations, 2):
                antinodes = self.get_new_locations(location1, location2)
                for antinode in antinodes:
                    if self.min_y <= antinode[0] <= self.max_y and self.min_x <= antinode[1] <= self.max_x:
                        results.add(antinode)

        return len(results)
    


    
    def solution_2(self) -> int:
        results = set()
        for locations in tqdm(self.antennas_locations.values()):
            for location1, location2 in combinations(locations, 2):
                diff = self.get_difference(location1, location2)
                results.add(location1)
                results.add(location2)
                for location, func in zip([location1, location2], [lambda x, y: x + y, lambda x, y: x - y]):
                    antinode = (func(location[0], diff[0]), func(location[1], diff[1]))
                    while self.min_y <= antinode[0] <= self.max_y and self.min_x <= antinode[1] <= self.max_x:
                        results.add(antinode)
                        antinode = (func(antinode[0], diff[0]), func(antinode[1], diff[1]))
        return len(results)



    

def main():

    print('TASK 1')
    sol = Solution('2024/Day_8/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 14')
    print('test 1:', sol.solution_2(), 'should equal 34')
    sol = Solution('2024/Day_8/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2())
   


if __name__ == '__main__':
    main()
