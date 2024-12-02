'''
Advent of Code 
2024 day 1
my solution to tasks
task 1 - heapify both lists and then pick up always smallest one and adding to result their difference
task 2 - create Counter of list 2 and move through list 1 to multiply value by number of counts from Counter, add those values


'''
import heapq
from collections import Counter

class Solution:

    def __init__(self, filename) -> None:
        self.list_1, self.list_2 = [], []
        self.get_data(filename)
        self.list_2_counter = Counter(self.list_2)
        self.list_1_2 = self.list_1.copy()

    def get_data(self, filename):
        with open(filename, 'r') as myfile:
            for line in myfile:
                line = line.strip().split()
                self.list_1.append(int(line[0]))
                self.list_2.append(int(line[-1]))

    def solution_1(self) -> int:
        heapq.heapify(self.list_1)
        heapq.heapify(self.list_2)
        result = 0
        while self.list_1 and self.list_2:
            result += abs(heapq.heappop(self.list_1) - heapq.heappop(self.list_2))
        return result
    
    
    def solution_2(self) -> int:
        result = 0
        for num in self.list_1_2:
            result += num * self.list_2_counter[num]
        return result
    

def main():

    print('TASK 1')
    sol = Solution('2024/Day_1/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 11')
    print('test 1:', sol.solution_2(), 'should equal 31')
    sol = Solution('2024/Day_1/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2())
   


if __name__ == '__main__':
    main()
