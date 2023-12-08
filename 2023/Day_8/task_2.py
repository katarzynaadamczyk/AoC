'''
Advent of Code 
2023 day 8
my solution to task 1 & 2

solution 1 - 
solution 2 - 
'''
from re import findall

class Node:
    def __init__(self, name, right, left) -> None:
        self.name = name
        self.moves = {'L': right, 'R': left}
    
    def get_next(self, move):
        return self.moves[move]
    
    def get_name(self):
        return self.name
    
    def update_nodes(self, lst_of_nodes):
        for node in lst_of_nodes:
            if type(self.moves['R']) == str and node.get_name() == self.moves['R']:
                self.moves['R'] = node
            if type(self.moves['L']) == str and node.get_name() == self.moves['L']:
                self.moves['L'] = node
            if type(self.moves['L']) != str and type(self.moves['R']) != str:
                break

class Solution:
    def __init__(self, filename, start_node) -> None:
        self.get_data(filename, start_node)

    def get_data(self, filename, end_char):
        self.roots, self.moves = [], ''
        self.nodes = {}
        with open(filename, 'r') as myfile:
            self.moves = myfile.readline().strip()
            self.moves_len = len(self.moves)
            myfile.readline()
            line = myfile.readline()
            while line:
                name, right, left = findall(r'\w+', line)
                new_node = Node(name, right, left)
                if name.endswith(end_char):
                    self.roots.append(new_node)
                self.nodes[name] = new_node
                line = myfile.readline()
        

    def solution(self, end_char):
        i = 0
        nodes = self.roots
        all_in_end_char = False
        while not all_in_end_char:
            new_nodes = []
            for node in nodes:
                new_nodes.append(self.nodes[node.get_next(self.moves[i % self.moves_len])])
            all_in_end_char = True
            for node in new_nodes:
                if not node.get_name().endswith(end_char):
                    all_in_end_char = False
                    break
            i += 1
            nodes = new_nodes
        return i 


def main():
    sol = Solution('2023/Day_8/test_3.txt', 'A')
    print('test 1:', sol.solution('Z'))
    sol = Solution('2023/Day_8/task.txt', 'A')
    print('Solution 1:', sol.solution('Z'))


if __name__ == '__main__':
    main()
