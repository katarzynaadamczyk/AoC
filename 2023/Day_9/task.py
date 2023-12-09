'''
Advent of Code 
2023 day 9
my solution to task 1 & 2

solution 1 - for each line: 1 - create a list of last number for each prediction based on given line until prediction is full of 0's. 
2 - sum all lasts numbers to get the result.

solution 2 - for each line: 1 - create a list of first number for each prediction based on given line until prediction is full of 0's.
2 - count previous predictions, 3 - add to results last received prediction, 4 - return sum of results

'''
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
            # 1
            while line.count(0) != len(line):
                firsts.append(line[0])
                line = [x_1 - x_0 for x_0, x_1 in zip(line[:-1], line[1:])]
            new_first = [0]
            # 2
            for first in firsts[::-1]:
                new_first.append(first - new_first[-1])
            # 3
            results.append(new_first[-1])
        # 4
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
