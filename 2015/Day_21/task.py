'''
Advent of Code 
2015 day 21
my solution to tasks

task 1&2 - using class for players and a bruteforce approach - checking each combination and finding min/max value afterwards


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
Ring = namedtuple('Ring', ['damage', 'armor', 'cost'])
rings = (Ring(1, 0, 25), Ring(2, 0, 50), Ring(3, 0, 100), 
         Ring(0, 1, 20), Ring(0, 2, 40), Ring(0, 3, 80))

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
        self.boss_hitpoints = int(lines[2].strip())
        self.boss_damage = int(lines[4].strip())
        self.boss_armor = int(lines[6].strip())
        self.boss = Player(self.boss_hitpoints, self.boss_damage, self.boss_armor)

    def _is_player_winner(self, player: Player) -> bool:
        return player.get_turns_to_lose(self.boss) >= self.boss.get_turns_to_lose(player)                                      
    
    def _check_with_rings(self, damage: int, armor: int, cost: int, results: set[int], win: bool=True):
        for i, (ring_damage, ring_armor, ring_cost) in enumerate(rings):
            player = Player(damage = damage + ring_damage, armor = armor + ring_armor)
            if (win and self._is_player_winner(player)) or (not win and not self._is_player_winner(player)):
                results.add(cost + ring_cost)
            for ring_2_damage, ring_2_armor, ring_2_cost in rings[i+1:]:
                player = Player(damage = damage + ring_damage + ring_2_damage, armor = armor + ring_armor + ring_2_armor)
                if (win and self._is_player_winner(player)) or (not win and not self._is_player_winner(player)):
                    results.add(cost + ring_cost + ring_2_cost)

    @time_it
    def solution_1(self) -> int:
        '''
        get result for task 1
        '''
        results = set()
        for damage, cost in damage_gains_vs_costs.items():
            # case 1 - player only owns weapon
            player = Player(damage=damage)
            if self._is_player_winner(player):
                results.add(cost)
            # case 2 - weapon + ring(s)
            self._check_with_rings(damage, 0, cost, results)
            for armor, armor_cost in armor_gains_vs_costs.items():
                # case 3 - weapon + armor
                player = Player(damage=damage, armor=armor)
                if self._is_player_winner(player):
                    results.add(cost + armor_cost)
                # weapon + armor + ring(s)
                self._check_with_rings(damage, armor, cost + armor_cost, results)


        return min(results) if results else -1


    @time_it
    def solution_2(self) -> int:
        '''
        get result for task 2
        '''
        results = set()
        for damage, cost in damage_gains_vs_costs.items():
            # case 1 - player only owns weapon
            player = Player(damage=damage)
            if not self._is_player_winner(player):
                results.add(cost)
            # case 2 - weapon + ring(s)
            self._check_with_rings(damage, 0, cost, results, False)
            for armor, armor_cost in armor_gains_vs_costs.items():
                # case 3 - weapon + armor
                player = Player(damage=damage, armor=armor)
                if not self._is_player_winner(player):
                    results.add(cost + armor_cost)
                # weapon + armor + ring(s)
                self._check_with_rings(damage, armor, cost + armor_cost, results, False)


        return max(results) if results else -1


def main():
    print('TEST 1')
    sol = Solution('2015/Day_21/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 4')
    print('test 2:', sol.solution_2(), 'should equal 17')
    print('SOLUTION')
    sol = Solution('2015/Day_21/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2())
   


if __name__ == '__main__':
    main()
