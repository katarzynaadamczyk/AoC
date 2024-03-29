'''
Advent of Code 
2023 day 8
my solution to task 2

First upload the data: first line to the moves. All the rest -> create Node and add it to the dict of nodes, 
if the node name ends in 'A' then add it to the root list

solution 2 - search for first reaching of the goal for each of the roots and then count their lcm (least common multiply) -> it is the answer

'''
from re import findall
from math import lcm

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
        nodes_len = len(nodes)
        times = dict()
        while len(times) < nodes_len:
            new_nodes = []
            for node in nodes:
                act_node = self.nodes[node.get_next(self.moves[i % self.moves_len])]
                new_nodes.append(act_node)
                if act_node.get_name().endswith(end_char):
                    times.setdefault(act_node.get_name(), i + 1)
            i += 1
            nodes = new_nodes
        return lcm(*times.values())

    def printouts(self):
        print('moves_len:', self.moves_len)
        print('roots_len:', len(self.roots))
        print('roots:', [node.get_name() for node in self.roots])

def main():
    sol = Solution('2023/Day_8/test_3.txt', 'A')
    sol.printouts()
    print('test 1:', sol.solution('Z'))
    sol = Solution('2023/Day_8/task.txt', 'A')
    sol.printouts()
    print('Solution 1:', sol.solution('Z'))


if __name__ == '__main__':
    main()
