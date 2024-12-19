'''
Advent of Code 
2024 day 20
my solution to tasks


task 1 - 

task 2 - 

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




    
    
    @time_it
    def solution_1(self) -> int:
        '''
        get result for task 1
        '''
        result = 0
        return result
    

    @time_it
    def solution_2(self) -> int:
        '''
        get result for task 2
        '''
        result = 0
        return result
    


    

def main():

    print('TEST 1')
    sol = Solution('2024/Day_20/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal ?')
   # print('test 1:', sol.solution_2(), 'should equal ?')
    print('SOLUTION')
    sol = Solution('2024/Day_20/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    #print('Solution 2:', sol.solution_2()) 
   


if __name__ == '__main__':
    main()
