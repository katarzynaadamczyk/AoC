'''
Advent of Code 
2015 day 21
my solution to tasks

task 1 - using class for players


'''
from dataclasses import dataclass
from collections import namedtuple
import time

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        print(f'time taken by {func.__name__} is {round(time.time()-start, 4)}')

        return result
    return wrapper

@dataclass
class Player:
    hitpoints: int = 100
    damage: int = 0
    armor: int = 0

    def get_turns_to_lose(self, other) -> int:
        damage_per_turn = max(other.damage - self.armor, 1)
        return self.hitpoints // damage_per_turn + (1 if self.hitpoints % damage_per_turn else 0)


armor_gains_vs_costs = {1: 13, 2: 31, 3: 53, 4: 75, 5: 102}
damage_gains_vs_costs = {4: 8, 5: 10, 6: 25, 7: 40, 8: 74}
Ring = namedtuple('Ring', ['damage', 'armor'])
rings = {Ring(1, 0): 25, Ring(2, 0): 50, Ring(3, 0): 100, 
         Ring(0, 1): 20, Ring(0, 2): 40, Ring(0, 3): 80}

class Solution:
    def __init__(self, filename: str, initial_player_hitpoints: int = 100) -> None:
        '''
        initialize Solution
        '''
        self.initial_player_hitpoints = initial_player_hitpoints
        self.get_data(filename)

    def get_data(self, filename):
        '''
        parse data
        '''
        with open(filename, 'r') as my_file:
            contents = my_file.read()
        lines = contents.split()
        self.boss_hitpoints = int(lines[0].split(":")[1].strip())
        self.boss_damage = int(lines[1].split(":")[1].strip())
        self.boss_armor = int(lines[2].split(":")[1].strip())                                       

    @time_it
    def solution_1(self, steps: int) -> int:
        '''
        get result for task 1
        '''
        result = 0
        return result


    @time_it
    def solution_2(self, steps: int) -> int:
        '''
        get result for task 2
        '''
        result = 0
        return result


def main():
    print('TEST 1')
    sol = Solution('2015/Day_21/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(4), 'should equal 4')
    print('test 2:', sol.solution_2(5), 'should equal 17')
    print('SOLUTION')
    sol = Solution('2015/Day_21/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1(100))
    print('Solution 2:', sol.solution_2(100))
   


if __name__ == '__main__':
    main()
