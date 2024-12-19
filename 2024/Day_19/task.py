'''
Advent of Code 
2024 day 19
my solution to tasks


task 1 - recurrent algorithm with memoization

task 2 - I got really stuck trying to make 2D DP table, I asked GPT for help, 
it is an easy 1D DP approach 

'''

import time

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
        self.towels = set()
        self.sequences = []
        self.get_data(filename)
        



    def get_data(self, filename):
        '''
        parse data
        '''
        with open(filename, 'r') as myfile:
            get_towels = True
            for line in myfile:
                if line == '\n':
                    get_towels = False
                    continue
                if get_towels:
                    self.towels = self.towels.union(line.strip().split(', '))
                else:
                    self.sequences.append(line.strip())


    def get_valid_towels(self, sequence):
        '''
        returning set of possible towels to get the sequence
        '''
        valid_towels = set()
        for towel in self.towels:
            if towel in sequence:
                valid_towels.add(towel)
        return valid_towels

    
    def is_valid_sequence(self, sequence, valid_towels):
        '''
        recurrent function determining if sequence can be divided into towels
        '''
        if valid_towels == set():
            return False
        if sequence == '' or sequence in valid_towels:
            return True
        if sequence in self.values_for_sequences.keys():
            return self.values_for_sequences[sequence]
        for towel in valid_towels:
            if towel in sequence:
                towel_index = sequence.find(towel)
                result = self.is_valid_sequence(sequence[:towel_index], valid_towels) and \
                    self.is_valid_sequence(sequence[towel_index + len(towel):], valid_towels)
                self.values_for_sequences[sequence] = result
                if result:
                    return result
        return False


    def get_number_of_sequences(self, sequence, valid_towels):
        '''
        function determining how many different stocks of towel are possible to get desired sequence
        DP 
        '''
        n = len(sequence)
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: there's 1 way to form an empty sequence
    
        # Iterate through the sequence
        for i in range(1, n + 1):
            for towel in valid_towels:
                len_towel = len(towel)
                if i >= len_towel and sequence[i - len_towel:i] == towel:
                    dp[i] += dp[i - len_towel]
    
        return dp[n]
    
    
    @time_it
    def solution_1(self) -> int:
        '''
        get result for task 1
        '''
        result = 0
        self.values_for_sequences = {}
        for sequence in self.sequences:
            if self.is_valid_sequence(sequence, self.get_valid_towels(sequence)):
                result += 1
        return result
    

    @time_it
    def solution_2(self) -> int:
        '''
        get result for task 2
        '''
        result = 0
        self.number_for_sequences = {x: 1 for x in self.towels}
        self.number_for_sequences[''] = 1
        for sequence in self.sequences:
            result += self.get_number_of_sequences(sequence, self.get_valid_towels(sequence))
        return result
    


    

def main():

    print('TEST 1')
    sol = Solution('2024/Day_19/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal ?')
    print('test 1:', sol.solution_2(), 'should equal ?')
    print('SOLUTION')
    sol = Solution('2024/Day_19/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2()) 
   


if __name__ == '__main__':
    main()
