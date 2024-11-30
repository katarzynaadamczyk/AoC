'''
Advent of Code 
2015 day 17
my solution to task 1
task 1 - 


'''
import heapq

class Solution:

    def __init__(self, filename) -> None:
        self.containers = []
        self.get_data(filename)
        self.no_of_containers = len(self.containers)

    def get_data(self, filename):
        with open(filename, 'r') as myfile:
            for line in myfile:
                self.containers.append(int(line.strip()))

    def solution_1(self, total: int=150) -> int:
        no_of_combinations = 0
        queue = []
        heapq.heappush(queue, (1, []))
        heapq.heappush(queue, (1, [self.containers[0]]))
        while queue:
            act_i, act_comb = heapq.heappop(queue)
            if sum(act_comb) == total:
                no_of_combinations += 1
                continue
            if sum(act_comb) > total or act_i == self.no_of_containers:
                continue
            heapq.heappush(queue, (act_i + 1, act_comb.copy() + [self.containers[act_i]]))
            heapq.heappush(queue, (act_i + 1, act_comb.copy()))

        return no_of_combinations
    
    


def main():

    print('TASK 1')
    sol = Solution('2015/Day_17/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(25), 'should equal 4')
   # print('test 1:', sol.solution_2())
    sol = Solution('2015/Day_17/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1(150))
 #   print('Solution 2:', sol.solution_2())
   


if __name__ == '__main__':
    main()
