'''
Advent of Code 
2015 day 9
my solution to task 1
task 1 - 

'''


class Solution:


    def __init__(self, filename) -> None:
        self.get_data(filename)

    def get_data_replace(self, filename):
        with open(filename, 'r') as myfile:
            for line in myfile:
                pass

    def solution_1(self):
        return 
    


def main():
    print('TASK 1')
    sol = Solution('2015/Day_9/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1())
  #  print('test 1:', sol.solution_2())
    sol = Solution('2015/Day_9/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
   # print('Solution 2:', sol.solution_2())


if __name__ == '__main__':
    main()
