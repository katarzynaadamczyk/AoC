'''
Advent of Code 
2022 day 18
my solution to tasks from day 18


solution 1 - 
solution 2 - idea from https://www.reddit.com/r/adventofcode/comments/zufpxd/day_18_python_cant_find_the_bug_in_my_code_got/

'''

import numpy as np
from queue import Queue


class EmptyCube:
    def __init__(self) -> None:
        pass
    

class Cube(EmptyCube):
    def __init__(self) -> None:
        pass
    
class Steam(EmptyCube):
    def __init__(self, position, steam_array, steam_and_cube_array) -> None:
        self.position = list(position)
        self.steam_array = steam_array
        self.steam_and_cube_array = steam_and_cube_array
        self.touching_cubes_count = self.count_touching_cubes()
        self.steam_array.append(self)
        self.steam_and_cube_array[self.position[0]][self.position[1]][self.position[2]] = self
    
    def get_touching_cubes(self):
        return self.touching_cubes_count
    
    def touching_cubes_generator(self):
        for shift in [-1, 1]:
            for i in range(3):
                if 0 <= self.position[i] + shift < self.steam_and_cube_array.shape[i]:
                    yield self.position[:i] + [self.position[i] + shift] + self.position[i + 1:]
    
    def count_touching_cubes(self):
        act_count = 0
        for x, y, z in self.touching_cubes_generator():
            if type(self.steam_and_cube_array[x][y][z]) == Cube:
                act_count += 1
        return act_count
    
    def propagate(self):
        for x, y, z in self.touching_cubes_generator():
            if type(self.steam_and_cube_array[x][y][z]) == int:
                yield Steam((x, y, z), self.steam_array, self.steam_and_cube_array)

def get_cubes(filename):
    cubes = []
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line.strip().split(',')
            cubes.append(tuple([int(x) for x in line]))
    return cubes


def shift_cubes(cubes, shift):
    new_cubes = set()
    for cube in cubes:
        new_cube = tuple([m + s for m, s in zip(cube, shift)])
        new_cubes.add(new_cube)
    del cubes
    return new_cubes


def move_steam(cubes_steam_array):
    steam_array = []
    start_steam = Steam((0, 0, 0), steam_array, cubes_steam_array)
    steam_moves_queue = Queue()
    steam_moves_queue.put(start_steam)
    while not steam_moves_queue.empty():
        act_steam = steam_moves_queue.get()
        for steam in act_steam.propagate():
            steam_moves_queue.put(steam)
    return steam_array


def solution_2(cubes):
    # prepare for numpy array
    mins, maxes = [], []
    for i in range(3):
        mins.append(min(cubes, key=lambda cube: cube[i])[i] - 1)
        maxes.append(max(cubes, key=lambda cube: cube[i])[i] + 1)
    shift = [0 - val for val in mins]
    if sum(shift) != 0:
        cubes = shift_cubes(cubes, shift)
        mins = [m + s for m, s in zip(mins, shift)]
        maxes = [m + s for m, s in zip(maxes, shift)]
    cubes_steam_array = np.zeros([m + 1 for m in maxes], EmptyCube)
    for x, y, z in cubes:
        new_cube = Cube()
        cubes_steam_array[x][y][z] = new_cube
    steam_array = move_steam(cubes_steam_array)
    return sum([steam.get_touching_cubes() for steam in steam_array])
  
def main():
    test_cubes = get_cubes('2022/Day_18/test.txt')
    print('test 2:', solution_2(test_cubes))
    task_cubes = get_cubes('2022/Day_18/task.txt')
    print('Solution 2:', solution_2(task_cubes))
    
    
if __name__ == '__main__':
    main()
    