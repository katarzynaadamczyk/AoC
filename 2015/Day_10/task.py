'''
Advent of Code 
2015 day 9
my solution to task 1
task 1 - dijskra's algorithm using priority queue with len(track) and act_track_val as priorities
task 2 - dijskra's algorithm using priority queue with len(track) and -1 * act_track_val as priorities

'''

import re
from queue import PriorityQueue
from itertools import combinations

class Solution:


    def __init__(self, line) -> None:
        self.data = line

    def solution_1(self, iterations=40):
        new_data = self.data
        for _ in range(iterations):
            act_new_data = ''
            char_prev = new_data[0]
            act_count = 0
            for char in new_data:
                if char == char_prev:
                    act_count += 1
                else:
                    act_new_data += str(act_count) + char_prev
                    char_prev = char
                    act_count = 1
            else:
                act_new_data += str(act_count) + char_prev
                char_prev = char
                act_count = 1
            new_data = act_new_data
        return len(new_data)



    


def main():
    print('TASK 1')
    sol = Solution('1')
    print('TEST 1')
    print('test 1:', sol.solution_1(40))
 #   print('test 1:', sol.solution_2())
    sol = Solution('1113122113')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_1(50))


if __name__ == '__main__':
    main()
