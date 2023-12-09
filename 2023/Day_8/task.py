'''
Advent of Code 
2023 day 8
my solution to task 1 
First upload the data: first line to the moves. All the rest -> create Node and add it to the dict of nodes, 
if the node name is 'AAA' then it is root

solution 1 - just follow the task directions until the road takes us to the goal which is 'ZZZ' -> in each step take next direction, 
than change actual node to the corresponding next-node until this next node name is 'ZZZ'.  

'''
from re import findall

class Node:
    def __init__(self, name, right, left) -> None:
        self.name = name
        self.moves = {'R': right, 'L': left}
    
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

    def get_data(self, filename, start_node):
        self.root, self.moves = None, ''
        self.nodes = {}
        with open(filename, 'r') as myfile:
            self.moves = myfile.readline().strip()
            self.moves_len = len(self.moves)
            myfile.readline()
            line = myfile.readline()
            while line:
                name, left, right = findall(r'\w+', line)
                new_node = Node(name, right, left)
                if name == start_node:
                    self.root = new_node
                self.nodes[name] = new_node
                line = myfile.readline()
        

    def solution(self, end_name):
        i = 0
        act_node = self.root
        while act_node.get_name() != end_name:
            act_node = self.nodes[act_node.get_next(self.moves[i % self.moves_len])]
            i += 1
        return i 


def main():
    sol = Solution('2023/Day_8/test_1.txt', 'AAA')
    print('test 1:', sol.solution('ZZZ'))
    sol = Solution('2023/Day_8/test_2.txt', 'AAA')
    print('test 2:', sol.solution('ZZZ'))
    sol = Solution('2023/Day_8/task.txt', 'AAA')
    print('Solution 1:', sol.solution('ZZZ'))


if __name__ == '__main__':
    main()
