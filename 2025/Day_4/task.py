'''
Advent of Code 
2025 day 4
my solution to tasks (operations on sets)

task 1 - for each paperroll check how many neighbors it has
task 2 - while set for removals is not empty keep adding to this set paperrolls that can be removed

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
    def __init__(self, filename: str) -> None:
        '''
        initialize Solution
        '''
        self.set_of_paperrolls = self.get_data(filename)

    def get_data(self, filename) -> set[tuple[int, ...]]:
        '''
        parse data
        '''
        result = set()
        with open(filename, 'r') as my_file:
            for y, line in enumerate(my_file):
                for x, char in enumerate(line.strip()):
                    if char == '@':
                        result.add((y, x))
        return result

    def _get_no_of_surrounding_papers(self, paper: tuple[int, int]) -> int:
        result = -1
        for y in range(paper[0] - 1, paper[0] + 2):
            for x in range(paper[1] - 1, paper[1] + 2):
                if (y, x) in self.set_of_paperrolls:
                    result += 1
        return result


    @time_it
    def solution_1(self) -> int:
        '''
        get result for task 1
        '''
        result = 0
        for paper in self.set_of_paperrolls:
            if self._get_no_of_surrounding_papers(paper) < 4:
                result += 1

        return result

    @time_it
    def solution_2(self) -> int:
        '''
        get result for task 2
        '''
        
        result = 0
        while True:
            papers_to_be_removed = set()
            for paper in self.set_of_paperrolls:
                if self._get_no_of_surrounding_papers(paper) < 4:
                    papers_to_be_removed.add(paper)
            result += len(papers_to_be_removed)
            self.set_of_paperrolls = self.set_of_paperrolls.difference(papers_to_be_removed)
            if len(papers_to_be_removed) == 0:
                break

        return result


def main():
    print('TEST 1')
    sol = Solution('2025/Day_4/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 13')
    print('test 2:', sol.solution_2(), 'should equal 43')
    print('SOLUTION')
    sol = Solution('2025/Day_4/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2())
   


if __name__ == '__main__':
    main()
