'''
Advent of Code 
2024 day 4
my solution to tasks
task 1 - 


'''
from collections import defaultdict

class Solution:

    def __init__(self, filename) -> None:
        self.table = []
        self.get_data(filename)

    def get_data(self, filename):
        with open(filename, 'r') as myfile:
            for line in myfile:
                self.table.append(line.strip())
    
    def get_result_for_line(self, line, word):
        i, max_i = line.find(word), len(line)
        result = 0
        while 0 <= i < max_i:
            result += 1
            i = line.find(word, i + 1)
        return result 

    def search_vertical(self, word):
        result = 0
        for line in self.table:
            result += self.get_result_for_line(line, word)
            result += self.get_result_for_line(line[::-1], word)
        return result
    
    def search_horizontal(self, word):
        result = 0
        for i in range(len(self.table[0])):
            line = ''.join([self.table[y][i] for y in range(len(self.table))])
            result += self.get_result_for_line(line, word)
            result += self.get_result_for_line(line[::-1], word)
        return result
    
    def search_diagonal(self, word):
        result = 0
        matrix_size = len(self.table)

        diagonal1 = defaultdict(list) # For the top right to bottom left
        diagonal2 = defaultdict(list) # For the top left to bottom right
        for i in range(matrix_size):
            for j in range(matrix_size):
                diagonal1[i-j].append(self.table[i][j])
                diagonal2[i+j].append(self.table[i][j])
        for diagonal in [diagonal1, diagonal2]:
            for values in diagonal.values():
                line = ''.join(values)
                result += self.get_result_for_line(line, word)
                result += self.get_result_for_line(line[::-1], word)

        return result


    def solution_1(self, word='XMAS') -> int:
        result = self.search_vertical(word)
        result += self.search_horizontal(word)
        result += self.search_diagonal(word)
        return result

    
    
    
    

def main():

    print('TASK 1')
    sol = Solution('2024/Day_4/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 18')
  #  print('test 1:', sol.solution_2(), 'should equal 48')
    sol = Solution('2024/Day_4/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
  #  print('Solution 2:', sol.solution_2()) 
   


if __name__ == '__main__':
    main()
