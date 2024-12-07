'''
Advent of Code 
2024 day 7
my solution to tasks
solutions with _2 at the end are brute force - using itertools.product
solution without _2 are my first idea to heapify a list and check all possible operations for each instruction
task 1 - my idea: for each instruction heapify and empty list and add first item of it to it, then iterate until list is over BUT 
if act_value exceeds target value or act_i exceeds max_i then neglect next values, if i == max_i and act_value == target value 
add it to results and move to next list
brute force: for each list act_value = list[0], then iterate over itertools.product(possible_function, repeat=(len(list) - 1)) 
in each iteration calculate target value, if it is equal to target then add it to results and move to next list
task 2 - same but one more operation 


'''

from tqdm import tqdm
import heapq
from itertools import product

class Solution:

    def __init__(self, filename) -> None:
        self.instructions = {}
        self.get_data(filename)
        self.operations = {lambda x, y: x + y, lambda x, y: x * y}
        self.operations_2 = {lambda x, y: x + y, lambda x, y: x * y, lambda x, y: int(str(x) + str(y))}
        #print(self.instructions)

    def get_data(self, filename):
        with open(filename, 'r') as myfile:
            for line in myfile:
                key = int(line[:line.find(':')])
                line = line[line.find(':')+1:]
                self.instructions.setdefault(key, [int(x) for x in line.strip().split()])

   
       
    def solution_1(self) -> int:
        results = set()
        for value, lstofnums in tqdm(self.instructions.items()):
            act_i, act_value, i_max = 0, lstofnums[0], len(lstofnums) - 1
            vals_heap = []
            heapq.heapify(vals_heap)
            heapq.heappush(vals_heap, (act_i, act_value))
            while vals_heap:
                act_i, act_value = heapq.heappop(vals_heap)
                if act_value == value and act_i == i_max:
                        results.add(value)
                        break
                if act_value > value or act_i >= i_max:
                    continue 
                act_i += 1
                for func in self.operations:
                    new_value = func(act_value, lstofnums[act_i])
                    heapq.heappush(vals_heap, (act_i, new_value))

        return len(results), sum(results)
    
    def solution_1_2(self) -> int:
        results = set()
        for value, lstofnums in tqdm(self.instructions.items()):
            for funcs in product(self.operations, repeat=len(lstofnums) - 1):
                act_val = lstofnums[0]
                for func, val in zip(funcs, lstofnums[1:]):
                    act_val = func(act_val, val)
                if act_val == value:
                    results.add(value)
                    break
        return len(results), sum(results)


    
    def solution_2(self) -> int:
        results = set()
        for value, lstofnums in tqdm(self.instructions.items()):
            for funcs in product(self.operations_2, repeat=len(lstofnums) - 1):
                act_val = lstofnums[0]
                for func, val in zip(funcs, lstofnums[1:]):
                    act_val = func(act_val, val)
                if act_val == value:
                    results.add(value)
                    break
        return len(results), sum(results)

    def solution_2_2(self) -> int:
        results = set()
        for value, lstofnums in tqdm(self.instructions.items()):
            act_i, act_value, i_max = 0, lstofnums[0], len(lstofnums) - 1
            vals_heap = []
            heapq.heapify(vals_heap)
            heapq.heappush(vals_heap, (act_i, act_value))
            while vals_heap:
                act_i, act_value = heapq.heappop(vals_heap)
                if act_value == value and act_i == i_max:
                        results.add(value)
                        break
                if act_value > value or act_i >= i_max:
                    continue 
                act_i += 1
                for func in self.operations_2:
                    new_value = func(act_value, lstofnums[act_i])
                    heapq.heappush(vals_heap, (act_i, new_value))

        return len(results), sum(results)



    

def main():

    print('TASK 1')
    sol = Solution('2024/Day_7/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1_2(), 'should equal ?')
    print('test 1:', sol.solution_2(), 'should equal ?')
    sol = Solution('2024/Day_7/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 1:', sol.solution_1_2())
    print('Solution 2:', sol.solution_2())
    print('Solution 2:', sol.solution_2_2())
   


if __name__ == '__main__':
    main()
