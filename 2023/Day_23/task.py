'''
Advent of Code 
2023 day 23
my solution to task 1 & 2 

solution 1 - 

solution 2 - 

'''


class Solution:

    def __init__(self, filename) -> None:
        self.get_data(filename)


    def get_data(self, filename):
        self.hill_map = []
        with open(filename, 'r') as myfile:
            for line in myfile:
                self.hill_map.append(line.strip())
        self.start_point = (0, 1)
        self.end_point = (len(self.hill_map) - 1, len(self.hill_map[-1]) - 2)



    def solution_1(self):
        return (self.start_point, self.end_point)
    
    def solution_2(self):
        return 0
        



def main():
    print('TASK 1')
    sol = Solution('2023/Day_23/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1())
  #  print('test 2:', sol.solution_2())
    sol = Solution('2023/Day_23/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
   # print('Solution 2:', sol.solution_2())


if __name__ == '__main__':
    main()
