'''
Advent of Code 
2024 day 4
my solution to tasks
task 1 - 


'''
from collections import defaultdict
import re

class Solution:

    def __init__(self, filename) -> None:
        self.table = []
        self.get_data(filename)
        self.table_size = len(self.table)

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
            line = ''.join([self.table[y][i] for y in range(self.table_size)])
            result += self.get_result_for_line(line, word)
            result += self.get_result_for_line(line[::-1], word)
        return result
    
    def search_diagonal(self, word):
        result = 0

        diagonal1 = defaultdict(list) # For the top right to bottom left
        diagonal2 = defaultdict(list) # For the top left to bottom right
        for i in range(self.table_size):
            for j in range(self.table_size):
                diagonal1[i-j].append(self.table[i][j])
                diagonal2[i+j].append(self.table[i][j])
        for diagonal in [diagonal1, diagonal2]:
            for values in diagonal.values():
                line = ''.join(values)
                result += self.get_result_for_line(line, word)
                result += self.get_result_for_line(line[::-1], word)

        return result

    def get_result_for_x_y(self, word, word_len, x, y):
        result = 0
        word1 = ''.join([self.table[y + s][x + s] for s in range(word_len)])
        word2 = ''.join([self.table[y + s][x + word_len - 1 - s] for s in range(word_len)])
        if word1 == word or word1[::-1] == word:
            result += 1
        if word2 == word or word2[::-1] == word:
            result += 1
        return result


    def search_diagonal_2(self, word):
        word_len, result = len(word), 0
        for y in range(self.table_size - word_len + 1):
            for x in range(self.table_size - word_len + 1):
                result += self.get_result_for_x_y(word, word_len, x, y)
        return result


    def solution_1(self, word='XMAS') -> int:
        result = self.search_vertical(word)
        result += self.search_horizontal(word)
        result += self.search_diagonal(word)
        return result

    def solution_1_2(self, word='XMAS') -> int:
        result = self.search_vertical(word)
        result += self.search_horizontal(word)
        result += self.search_diagonal_2(word)
        return result
    
    def solution_2(self) -> int:
        result = 0
        MS_set = set(['M', 'S'])
        for y in range(1, self.table_size -1):
            for x in range(1, self.table_size -1):
                if self.table[y][x] == 'A':
                    one_set = set([self.table[y-1][x-1], self.table[y+1][x+1]])
                    two_set = set([self.table[y-1][x+1], self.table[y+1][x-1]])
                    if one_set == MS_set and two_set == MS_set:
                        result += 1
        return result

    def solution_2_2(self, word='MAS') -> int:
        result = 0
        word_len = len(word)
        for y in range(0, self.table_size - word_len + 1):
            for x in range(0, self.table_size - word_len + 1):
                if self.get_result_for_x_y(word, word_len, x, y) == 2:
                    result += 1
        return result

    

def main():

    print('TASK 1')
    sol = Solution('2024/Day_4/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 18')
    print('test 1:', sol.solution_1_2(), 'should equal 18')
    print('test 1:', sol.solution_2(), 'should equal 9')
    print('test 1:', sol.solution_2_2(), 'should equal 9')
    sol = Solution('2024/Day_4/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 1:', sol.solution_1_2())
    print('Solution 2:', sol.solution_2()) # 1945 too low
    print('Solution 2:', sol.solution_2_2()) 
   


if __name__ == '__main__':
    main()
