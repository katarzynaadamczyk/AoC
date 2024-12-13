'''
Advent of Code 
2024 day 14
my solution to tasks


task 1 -        

'''

from tqdm import tqdm

class Solution:

    def __init__(self, filename) -> None:
        self.data = []
        self.get_data(filename)
        

    def get_data(self, filename):
        with open(filename, 'r') as myfile:
            for line in myfile:
                self.data.append(line.strip())
   
    
    
    
    def solution_1(self) -> int:
        result = 0
        return result
    

    
    def solution_2(self) -> int:
        result = 0
        return result

    

def main():

    print('TASK 1')
    sol = Solution('2024/Day_14/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal ?')
    print('test 1:', sol.solution_2(), 'should equal ?')
    sol = Solution('2024/Day_14/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1()) 
    print('Solution 2:', sol.solution_2()) 
   


if __name__ == '__main__':
    main()
