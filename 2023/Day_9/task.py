'''
Advent of Code 
2023 day 9
my solution to task 1 & 2

solution 1 - 

'''
from re import findall

class Solution:
    def __init__(self, filename) -> None:
        self.get_data(filename)

    def get_data(self, filename):
        self.data = []
        with open(filename, 'r') as myfile:
            for line in myfile:
                self.data.append([int(x) for x in line.strip().split()])        

    def solution_1(self):
        lasts = []
        for line in self.data:
            while line.count(0) != len(line):
                lasts.append(line[-1])
                line = [x_1 - x_0 for x_0, x_1 in zip(line[:-1], line[1:])]
        return sum(lasts) 
    
    def solution_2(self):
        results = []
        for line in self.data:
            firsts = []
            while line.count(0) != len(line):
                firsts.append(line[0])
                line = [x_1 - x_0 for x_0, x_1 in zip(line[:-1], line[1:])]
            new_first = [0]
            for first in firsts[::-1]:
                new_first.append(first - new_first[-1])
            results.append(new_first[-1])
        return sum(results) 


def main():
    sol = Solution('2023/Day_9/test.txt')
    print('test 1:', sol.solution_1())
    print('test 2:', sol.solution_2())
    sol = Solution('2023/Day_9/task.txt')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2())


if __name__ == '__main__':
    main()
