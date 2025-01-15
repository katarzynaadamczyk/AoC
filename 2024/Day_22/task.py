'''
Advent of Code 
2024 day 22
my solution to tasks

task 1 - a simple for loop in each iteration counting the next num value, returning it and adding to result

task 2 -
for each num: 
    for each sequence of price changes check if sequence was already noted - if so, add bananas to deafultdict and sequence to saw sequences, 
    if not continue
return top value 


'''

import time
from tqdm import tqdm
from collections import defaultdict

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        print(f'time taken by {func.__name__} is {round(time.time()-start, 4)}')

        return result
    return wrapper


class Solution:

    def __init__(self, filename) -> None:
        '''
        initialize Solution
        '''
        self.numbers = []
        self.get_data(filename)
        self.sequences_values = defaultdict(int)
      #  print(self.numbers)


    def get_data(self, filename):
        '''
        parse data
        '''
        with open(filename, 'r') as myfile:
            for line in myfile:
                self.numbers.append(int(line.strip()))

    
    def mix_into_number(self, num, res):
        '''
        get result of mixing
        '''
        return num ^ res
    
    def prune_number(self, num):
        '''
        get result of pruning 
        '''
        return num % 16777216


    def get_new_secret_number(self, num):
        '''
        get new secret number
        '''
        num = self.prune_number(self.mix_into_number(num, num * 64))
        num = self.prune_number(self.mix_into_number(num, num // 32))
        num = self.prune_number(self.mix_into_number(num, num * 2048))
        return num


    def get_iterated_number(self, num, no_of_iterations):
        '''
        calculate number value after no_of_iterations
        '''
        nums = []
        for _ in range(no_of_iterations):
            num = self.get_new_secret_number(num)
        return num
    

    def add_sequences_values(self, num, no_of_iterations=2000):
        '''
        add all possible sequences for num to self.sequences_values deafaultdict
        '''
        sequence = tuple()
        saw_sequences = set()
        for _ in range(4):
            new_num = self.get_new_secret_number(num)
            sequence += (new_num % 10 - num % 10, )
            num = new_num
        self.sequences_values[sequence] += num % 10
        for _ in range(no_of_iterations - 4):
            new_num = self.get_new_secret_number(num)
            sequence = sequence[1:] + (new_num % 10 - num % 10, )
            if sequence not in saw_sequences:
                self.sequences_values[sequence] += new_num % 10
                saw_sequences.add(sequence)
            num = new_num
        

    
    @time_it
    def solution_1(self, no_of_iterations=2000) -> int:
        '''
        get result for task 1
        '''
        result = 0
        for num in tqdm(self.numbers):
            result += self.get_iterated_number(num, no_of_iterations)
        return result
    

    @time_it
    def solution_2(self, no_of_iterations=2000) -> int:
        '''
        get result for task 2
        '''
        for num in tqdm(self.numbers):
            self.add_sequences_values(num, no_of_iterations)
        return max(self.sequences_values.values())
    


    

def main():

    print('TEST 1')
    sol = Solution('2024/Day_22/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal ?')
    print(sol.add_sequences_values(123, 10))
    print('test 1:', sol.solution_2(), 'should equal ?')
    print('SOLUTION')
    sol = Solution('2024/Day_22/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2()) 
   


if __name__ == '__main__':
    main()
