'''
Advent of Code 
2024 day 25
my solution to tasks

task 1 - set key and locks as sets of points for each #
then loop over all keys and all locks to find if they itersect
if no add to result

done all tasks from AoC 2024! :)


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
        self.keys = [] # lst of sets
        self.locks = [] # lst of sets
        self.get_data(filename)

    def get_data(self, filename):
        '''
        parse data
        '''
        with open(filename, 'r') as myfile:
            tmp = myfile.read().split('\n\n')
            for chunk in tmp:
                chunk = chunk.split('\n')
                key_lock = set()
                for y, line in enumerate(chunk[1:-1]):
                    for x, char in enumerate(line):
                        if char == '#':
                            key_lock.add((y, x))
                if '#' in chunk[0]:
                    self.locks.append(key_lock)
                else:
                    self.keys.append(key_lock)

    

    @time_it
    def solution_1(self) -> int:
        '''
        get result for task 1
        '''
        result = 0
        for lock in self.locks:
            for key in self.keys:
                if len(lock.intersection(key)) == 0:
                    result += 1
        return result


    @time_it
    def solution_2(self) -> int:
        '''
        get result for task 2
        '''
        
        results = 0
        return results


def main():
    print('TEST 1')
    sol = Solution('2024/Day_25/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal ?')
  #  print('test 2:', sol.solution_2(), 'should equal ?')
    print('SOLUTION')
    sol = Solution('2024/Day_25/task.txt')
   # print('SOLUTION')
    print('Solution 1:', sol.solution_1())
   # print('Solution 2:', sol.solution_2())
   


if __name__ == '__main__':
    main()
