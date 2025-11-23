'''
Advent of Code 
2015 day 18
my solution to tasks

task 1 - brute force on lists & tuples (for adding to set and counting the number of distinct tuples)
task 2 -> reverse engineering:
            1. create a dict of tuples changing to unique molecule
            2. loop over molecule to find all possible changes and change them to single molecule until len(molecule) == 1 && molecule == init_molecule (e)
            3. return value of changes made in such a way
            good idea in general, but needed to find a pattern in input data -> abandoned this task, went an easy way and opened reddit 
            solution is in solution_2_3 function -> found a pattern and calculated the result 
    
'''
import time
from collections import defaultdict
from copy import copy
import heapq

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f'time taken by {func.__name__} is {round(time.time()-start, 4)}')

        return result
    return wrapper


class Solution:
    def __init__(self, filename) -> None:
        '''
        initialize Solution
        '''
        self.num_of_presents = self.get_data(filename)

    def get_data(self, filename):
        '''
        parse data
        '''
        with open(filename, 'r') as my_file:
            return int(my_file.read().strip())            

    @time_it
    def solution_1(self, present_value: int = 10, internal_limit: int = 1_000_000, max_visit_for_elf: int | None = None) -> int:
        '''
        get result for task 1
        '''
        result = set()
        houses = [address * present_value for address in range(internal_limit + 1)]
        for elf in range(1, internal_limit):
            elf_bound = min(elf * (max_visit_for_elf + 1), internal_limit) if max_visit_for_elf else internal_limit
            for address in range(elf * 2, elf_bound, elf):
                houses[address] += elf * present_value
                if houses[address] > self.num_of_presents:
                    result.add(address)
        return min(result)


def main():
    print('TEST 1')
    sol = Solution('2015/Day_20/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1(10))
    print('Solution 2:', sol.solution_1(present_value=11, max_visit_for_elf=50))
   


if __name__ == '__main__':
    main()
