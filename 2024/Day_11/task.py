'''
Advent of Code 
2024 day 11
my solution to tasks

task 1 - brute force solution - for each blink create new list of stones based on previous list following rules described in task
task 2 - optimized solution using Counter from collections - for each blink create new Counter of stones based on previous one


'''

from tqdm import tqdm
from collections import Counter

class Solution:

    def __init__(self, filename) -> None:
        self.line_of_stones = []
        self.get_data(filename)

    def get_data(self, filename):
        with open(filename, 'r') as myfile:
            for line in myfile:
                self.line_of_stones = [int(x) for x in line.strip().split()]
    
    def get_next_stone(self, stone):
        if stone == 0:
            return [1]
        len_of_stone = len(str(stone))
        if len_of_stone % 2 == 0:
            stone_str = str(stone)
            return [int(stone_str[:len_of_stone//2]), int(stone_str[len_of_stone//2:])]
        return [stone * 2024]
    

    def solution_1(self, n=25) -> int:
        act_line_of_stones = self.line_of_stones
        for _ in tqdm(range(n)):
            new_line_of_stones = []
            for stone in act_line_of_stones:
                new_line_of_stones += self.get_next_stone(stone)
            act_line_of_stones = new_line_of_stones
        return len(act_line_of_stones)
    


    
    def solution_2(self, n=75) -> int:
        act_line_of_stones = Counter(self.line_of_stones)
        for _ in tqdm(range(n)):
            new_line_of_stones = Counter()
            for stone in act_line_of_stones.keys():
                for new_stone in self.get_next_stone(stone):
                    new_line_of_stones[new_stone] += act_line_of_stones[stone]
            act_line_of_stones = new_line_of_stones
        return act_line_of_stones.total()



    

def main():

    print('TASK 1')
    sol = Solution('2024/Day_11/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 55312')
    print('test 1:', sol.solution_2(25), 'should equal 55312')
    sol = Solution('2024/Day_11/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2())
   


if __name__ == '__main__':
    main()
