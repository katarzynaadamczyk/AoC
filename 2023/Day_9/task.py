'''
Advent of Code 
2023 day 9
my solution to task 1 

solution 1 - 

'''
from re import findall

class Solution:
    def __init__(self, filename, start_node) -> None:
        self.get_data(filename, start_node)

    def get_data(self, filename, start_node):
        self.root, self.moves = None, ''
        self.nodes = {}
        with open(filename, 'r') as myfile:
            self.moves = myfile.readline().strip()
            self.moves_len = len(self.moves)
            myfile.readline()
            line = myfile.readline()
            while line:
                line = myfile.readline()
        

    def solution(self, end_name):
        i = 0
        act_node = self.root
        while act_node.get_name() != end_name:
            act_node = self.nodes[act_node.get_next(self.moves[i % self.moves_len])]
            i += 1
        return i 


def main():
    sol = Solution('2023/Day_9/test.txt', 'AAA')
    print('test 1:', sol.solution('ZZZ'))
    sol = Solution('2023/Day_9/task.txt', 'AAA')
    print('Solution 1:', sol.solution('ZZZ'))


if __name__ == '__main__':
    main()
