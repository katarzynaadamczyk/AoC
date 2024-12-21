'''
Advent of Code 
2024 day 21
my solution to tasks

task 1 - 

task 2 - 


'''

import time
import heapq
from tqdm import tqdm
from sys import maxsize
from collections import Counter

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
        self.min_sequences = {(key, key): set(['A']) for key in set(self.numeric_keypad.keys()).union(set(self.directional_keypad.keys()))} 
        print(self.min_sequences)



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
        set_of_resulting_sequences = set()
        # len(act_pos_to_get_there), act_position, act_sequence_to_get_there (><^VA), 
        # act_pos_sequence (A321)
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

    
    
    @time_it
    def solution_1(self) -> int:
        '''
        get result for task 1
        '''
        start_pos = 'A'
        result = 0
        for sequence in tqdm(self.sequences):
            # numeric keypad transform to moves of first robot
            start_pos = 'A'
            seq_int = int(sequence[:-1])
            possible_sequences = set([''])
            for char in sequence:
                new_possible_sequences = set()
                for new_seq in self.get_min_paths_to_get_char(start_pos, char, self.numeric_keypad):
                    for seq in possible_sequences:
                        new_possible_sequences.add(seq + new_seq)
                possible_sequences = new_possible_sequences
                start_pos = char
            # robot moves to transform (as 2 more robots so range 2)
            for _ in range(2):
                new_robot_possible_sequences = set()
                for sequence in [seq for seq in possible_sequences if len(seq) == min([len(x) for x in possible_sequences])]:
                    start_pos = 'A'
                    robot_possible_sequences = set([''])
                    for char in sequence:
                        new_possible_sequences = set([''])
                        for new_seq in self.get_min_paths_to_get_char(start_pos, char, self.directional_keypad):
                            for seq in robot_possible_sequences:
                                new_possible_sequences.add(seq + new_seq)
                        new_possible_sequences.remove('')
                        robot_possible_sequences = new_possible_sequences
                        start_pos = char
                    new_robot_possible_sequences = new_robot_possible_sequences.union(robot_possible_sequences)
                possible_sequences = new_robot_possible_sequences
       #     print(seq_int, min([len(x) for x in possible_sequences]))

            result += seq_int * min([len(x) for x in possible_sequences])
        return result
    

    @time_it
    def solution_2(self) -> int:
        '''
        get result for task 2
        '''
        return 0
    


    

def main():

    print('TEST 1')
    sol = Solution('2024/Day_21/test.txt')
    print('TEST 1')
    print(sol.get_min_paths_to_get_char('A', 'A', sol.directional_keypad))
    print('test 1:', sol.solution_1(), 'should equal ?')
 #   print('test 1:', sol.solution_2(), 'should equal ?')
    print('SOLUTION')
    sol = Solution('2024/Day_21/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
 #   print('Solution 2:', sol.solution_2()) 
   


if __name__ == '__main__':
    main()
