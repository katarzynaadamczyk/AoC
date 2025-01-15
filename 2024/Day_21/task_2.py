'''
Advent of Code 
2024 day 21
my solution to tasks

task 1 - faster solution than in task.py
works on Counters of (start, stop) : count
it solves part 2 as well


'''

import time
import heapq
from tqdm import tqdm
from sys import maxsize
from collections import Counter, defaultdict
from copy import copy
from itertools import product

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
        self.sequences = []
        self.get_data(filename)
        self.numeric_keypad = {
                                 '0': {'>': 'A', '^': '2'},
                                 '1': {'>': '2', '^': '4'},
                                 '2': {'<': '1', '>': '3', '^': '5', 'v': '0'},
                                 '3': {'<': '2', '^': '6', 'v': 'A'},
                                 '4': {'>': '5', '^': '7', 'v': '1'},
                                 '5': {'<': '4', '>': '6', '^': '8', 'v': '2'},
                                 '6': {'<': '5', 'v': '3', '^': '9'},
                                 '7': {'v': '4', '>': '8'},
                                 '8': {'<': '7', '>': '9', 'v': '5'},
                                 '9': {'<': '8', 'v': '6'},
                                 'A': {'^': '3', '<': '0'}
                               }

        self.directional_keypad = {
                                    '^': {'>': 'A', 'v': 'v'},
                                    'v': {'>': '>', '<': '<', '^': '^'},
                                    '>': {'^': 'A', '<': 'v'},
                                    '<': {'>': 'v'},
                                    'A': {'<': '^', 'v': '>'}
                                  }
        # (start, stop): set_of_min_sequences
        self.min_sequences = defaultdict(set)
        for key in set(self.numeric_keypad.keys()).union(set(self.directional_keypad.keys())):
            self.min_sequences[(key, key)].add('A')
        self.get_sequences_for_directional_keypad()
        self.min_sequences_counters = defaultdict(list)
        self.transform_min_sequence_to_counter()
        print(self.min_sequences_counters)


    def get_data(self, filename):
        '''
        parse data
        '''
        with open(filename, 'r') as myfile:
            for line in myfile:
                self.sequences.append(line.strip())


    def get_min_paths_to_get_char(self, start_position, char, keypad):
        '''
        get all min sequences to get to char
        '''
        if (start_position, char) in self.min_sequences.keys():
            return self.min_sequences[(start_position, char)]
        # len(act_pos_to_get_there), act_position, act_sequence_to_get_there (><^VA), 
        # act_pos_sequence (A321)
        set_of_resulting_sequences = set()
        stack = [(0, start_position, '', start_position)] # len(act_pos_to_get_there), act_position, act_sequence_to_get_there (><^VA), act_pos_sequence
        heapq.heapify(stack)
        min_sequence_len = maxsize
        while stack:
            path_len, act_position, act_sequence, pos_sequence = heapq.heappop(stack)
            if act_position == char:
                if path_len > min_sequence_len:
                    break
                min_sequence_len = path_len
                set_of_resulting_sequences.add(act_sequence + 'A')
                continue
            for direction, new_position in keypad[act_position].items():
                if new_position not in pos_sequence:
                    heapq.heappush(stack, (path_len + 1, new_position, act_sequence + direction, pos_sequence + new_position))
        self.min_sequences[(start_position, char)] = set_of_resulting_sequences
        return set_of_resulting_sequences
    

    def get_sequences_for_number(self, number):
        '''
        get all possible sequences for one number
        sequences meaning strings to click on directional keypad of second robot to get what we want for first robot
        (the one that inputs to the numeric keypad)
        '''
        start_pos = 'A'
        for char in number:
            self.get_min_paths_to_get_char(start_pos, char, self.numeric_keypad)
            start_pos = char
    

    def get_sequences_for_directional_keypad(self):
        '''
        get all min sequences for directional keypad
        '''
        for key1, key2 in product(self.directional_keypad.keys(), repeat=2):
            self.get_min_paths_to_get_char(key1, key2, keypad=self.directional_keypad)
            if len(self.min_sequences[(key1, key2)]) > 1:
                # eliminate unnecessary sequences manually
                if {'>^>A', '>>^A'} == self.min_sequences[(key1, key2)]:
                    self.min_sequences[(key1, key2)] = {'>>^A'}
                elif {'v<<A', '<v<A'} == self.min_sequences[(key1, key2)]:
                    self.min_sequences[(key1, key2)] = {'v<<A'}
    

    def transform_sequence(self, sequence):
        '''
        transform sequence (str) into Counter of pairs (start, stop): count in sequence
        '''
        return Counter([(sequence[i], sequence[i + 1]) for i in range(len(sequence) - 1)])
    

    def transform_min_sequence_to_counter(self):
        '''
        transform set of min sequences from min_sequences
        to list of Counters - (start, stop) : count
        for each new (start, stop) tuple
        '''
        for key_tuple, sequences in self.min_sequences.items():
            if self.min_sequences_counters[key_tuple] == []:
                for sequence in sequences:
                    self.min_sequences_counters[key_tuple].append(self.transform_sequence('A' + sequence))
    

    def add_multiplied_counter_to_counter(self, c_main):
        '''
        needed for moving robot
        '''
        c = [Counter()]
        for key_main, value_main in c_main.items():
            results = []
            for c_1 in c:
                for c_2 in self.min_sequences_counters[key_main]:
                    new_c = copy(c_1)
                    for key_second, value_second in c_2.items():
                        new_c[key_second] += value_main * value_second
                    results.append(new_c)
            c = results
        return c
    
    
    @time_it
    def solution_1(self, num_of_robots=2) -> int:
        '''
        get result for task 1
        '''
        result = 0
        self.possible_sequences = dict()
        for sequence in self.sequences:
            seq_int = int(sequence[:-1])
            # numeric keypad transform to moves of first robot with numeric keypad
            self.get_sequences_for_number(sequence)
            self.transform_min_sequence_to_counter()
            act_sequence_counters = [Counter()]
            for start, stop in zip('A' + sequence[:-1], sequence):
                new_sequence_counters = []
                for c in act_sequence_counters:
                    for c_2 in self.min_sequences_counters[(start, stop)]:
                        new_sequence_counters.append(c + c_2)
                min_value = min([x.total() for x in new_sequence_counters])
                act_sequence_counters = [x for x in new_sequence_counters if x.total() == min_value]
            # robot moves to transform (as 2 more robots so range 2)
            for _ in range(num_of_robots):
                robot_sequences = []
                for c_main in act_sequence_counters:
                    robot_sequences += self.add_multiplied_counter_to_counter(c_main)
                min_value = min([x.total() for x in robot_sequences])
                act_sequence_counters = [x for x in robot_sequences if x.total() == min_value]
            print(seq_int, min_value) # to know where we are 
            result += seq_int * min_value
        return result
    

    @time_it
    def solution_2(self) -> int:
        '''
        get result for task 2
        done good results in solution 1, no need to do another in solution_2

        '''
        return 0
    


    

def main():

    print('TEST 1')
    sol = Solution('2024/Day_21/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(2), 'should equal ?')
 #   print('test 1:', sol.solution_2(), 'should equal ?')
    print('SOLUTION')
    sol = Solution('2024/Day_21/task.txt')
  #  print('SOLUTION')
    print('Solution 1:', sol.solution_1(2))
    print('Solution 2:', sol.solution_1(25)) 
   


if __name__ == '__main__':
    main()
