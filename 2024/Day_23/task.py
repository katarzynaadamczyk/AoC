'''
Advent of Code 
2024 day 21
my solution to tasks

task 1 - 

task 2 - 


'''

import time
from collections import defaultdict, Counter

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
        self.computer_connections = defaultdict(set)
        self.get_data(filename)
      


    def get_data(self, filename):
        '''
        parse data
        '''
        with open(filename, 'r') as myfile:
            for line in myfile:
                dash = line.find('-')
                self.computer_connections[line[:dash]].add(line[dash+1:].strip())
                self.computer_connections[line[dash+1:].strip()].add(line[:dash])

    
    
    @time_it
    def solution_1(self) -> int:
        '''
        get result for task 1
        '''
        result = set()
        computers_with_t = set(filter(lambda x: x.startswith('t'), self.computer_connections.keys()))
        for computer in computers_with_t:
            for computer_2 in self.computer_connections[computer]:
                i = self.computer_connections[computer].intersection(self.computer_connections[computer_2])
                for computer_3 in i:
                    result.add(tuple(sorted([computer, computer_2, computer_3])))
        return len(result)
    

    @time_it
    def solution_2(self) -> int:
        '''
        get result for task 2
        '''
        # add each computer to its LAN
        computer_lans = []
        for key, value in self.computer_connections.items():
            computer_lans.append(tuple(sorted(value.union(set([key])))))
        # 
        lans_dict = defaultdict(int)
        for lan in computer_lans:
            for i in range(len(lan)):
                lans_dict[lan[:i] + lan[i+1:]] += 1
        result = max(lans_dict.items(), key=lambda x: x[1])
        return ','.join(result[0])
    


    

def main():

    print('TEST 1')
    sol = Solution('2024/Day_23/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal ?')
    print('test 1:', sol.solution_2(), 'should equal ?')
    print('SOLUTION')
    sol = Solution('2024/Day_23/task.txt')
   # print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2()) 
   


if __name__ == '__main__':
    main()
