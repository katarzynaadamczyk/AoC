'''
Advent of Code 
2024 day 21
my solution to tasks

task 1 - 

task 2 - 


'''
from collections import Counter, defaultdict
import time
import re

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        print(f'time taken by {func.__name__} is {round(time.time()-start, 4)}')

        return result
    return wrapper


class TreeNode:
    actions = {'XOR': lambda a, b: 1 if a != b else 0,
               'AND': lambda a, b: 1 if a == 1 == b else 0,
               'OR': lambda a, b: 1 if a == 1 or b == 1 else 0}
    

    def __init__(self, name, func='', next_nodes=None, value=-1):
        '''
        initialize TreeNode
        '''
        self.name = name
        self.func = func
        self.next_nodes = next_nodes
        self.value = value

    def update_next_nodes(self, nodes):
        if self.next_nodes is not None:
            self.next_nodes = [nodes[node] for node in self.next_nodes]

    def get_value(self):
        if self.next_nodes is not None:    
            self.value = TreeNode.actions[self.func](*[node.get_value() for node in self.next_nodes])
        return self.value
    
    def get_next_nodes(self):
        '''
        return next_nodes if existing, empty list otherwise
        '''
        if self.next_nodes is None:
            return []
        return self.next_nodes
    
    def __repr__(self):
        '''
        needed for printing for task 2 but may be useless
        '''
        return str({self.name: self.value if self.next_nodes is None else ' '.join([self.next_nodes[0].name, self.func, 
                                                                                    self.next_nodes[-1].name])})
    
    def get_all_below_nodes(self):
        '''
        return list of all nodes below actual node
        seemed to be needed for task 2, but may be unnecessary
        '''
        if self.next_nodes is None:
            return []
        lst = [node.name for node in self.get_next_nodes()]
        for node in self.next_nodes:
            lst += node.get_all_below_nodes()
        return lst


class Solution:

    def __init__(self, filename) -> None:
        '''
        initialize Solution
        '''
        self.nodes = {} # str: TreeNode
        self.before_nodes = {} # str: {func: str, nodes: set}
        self.and_node_counter = defaultdict(int) # str: int
        self.xor_node_counter = defaultdict(int) # str: int
        self.or_node_counter = defaultdict(int) # str: int
        self.get_data(filename)
        # update Next TreeNodes in each TreeNode
        for node in self.nodes.values():
            node.update_next_nodes(self.nodes)

    def get_data(self, filename):
        '''
        parse data
        '''
        with open(filename, 'r') as myfile:
            valued_nodes = True
            for line in myfile:
                if line == '\n':
                    valued_nodes = False
                    continue
                if valued_nodes:
                    i = line.find(':')
                    self.nodes.setdefault(line[:i], TreeNode(name=line[:i], value=int(line[i+1:].strip())))
                else:
                    line = [x.strip() for x in line.strip().split()]
                    self.nodes.setdefault(line[-1], TreeNode(name=line[-1], func=line[1], next_nodes=[line[0], line[2]]))
                    if line[1] == 'AND':
                        self.and_node_counter[line[0]] += 1
                        self.and_node_counter[line[2]] += 1
                    elif line[1] == 'XOR':
                        self.xor_node_counter[line[0]] += 1
                        self.xor_node_counter[line[2]] += 1
                    else:
                        self.or_node_counter[line[0]] += 1
                        self.or_node_counter[line[2]] += 1


    def get_values(self, start_char='z'):
        '''
        get number for start_char starting wires
        '''
        z_names = sorted(filter(lambda x: x.startswith(start_char), self.nodes_values.keys()), reverse=True)
        z_values = ''.join([str(self.nodes_values[x]) for x in z_names])
        return z_values
    

    def get_wrong_z_wires(self):
        '''
        get wrong z wires results
        probably not necessary function
        '''
        rest = 0
        z_names = [z[1:] for z in sorted(filter(lambda x: x.startswith('z'), self.nodes_values.keys()), reverse=False)]
        wrong_z_names = []
        for i in z_names[:-1]:
            sum_nums = sum([rest, self.nodes_values['x' + i], self.nodes_values['y' + i]])
            if not sum_nums % 2 == self.nodes_values['z' + i]:
                wrong_z_names.append('z' + i)
            rest = 1 if sum_nums >= 2 else 0
        if rest != self.nodes_values['z' + z_names[-1]]:
            wrong_z_names.append('z' + z_names[-1])
        return wrong_z_names

    
    @time_it
    def solution_1(self) -> int:
        '''
        get result for task 1
        '''
        self.nodes_values = {}
        for name, node in self.nodes.items():
            self.nodes_values.setdefault(name, node.get_value())
        z_values = self.get_values()
        return int(z_values, base=2)
    

    @time_it
    def solution_2_v1_for_tests(self) -> int:
        '''
        get result for task 2
        first attempt to understand task - probably not necessary
        '''
        wrong_results_of_z_wires = self.get_wrong_z_wires()
        
        print(len(self.nodes))
        nodes_to_check = []
        nodes_to_check_sets = {}
        for node_name in wrong_results_of_z_wires:
            nodes = self.nodes[node_name].get_all_below_nodes()
            nodes_to_check += nodes
            nodes_to_check_sets[node_name] = set(nodes)
    # print(set(nodes_to_check))
        c = Counter(nodes_to_check)
        for node, count in c.items():
            print(self.nodes[node], count)
        print({x: len(v) for x, v in nodes_to_check_sets.items()})
        
        # TODO
        return 0
    

    @time_it
    def solution_2(self) -> int:
        '''
        get result for task 2
        go through all inputs and outputs and check if logic is correct
        add to results wires will see what happens
        '''
        results = set()
        # first check if first two results are correct
        print(self.and_node_counter)
        print(self.or_node_counter)
        print(self.xor_node_counter)
                        
        return ','.join(sorted(results))


def main():
    print('TEST 1')
    sol = Solution('2024/Day_24/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal ?')
  #  print('test 2:', sol.solution_2(), 'should equal ?')
    print('TEST 2')
    sol = Solution('2024/Day_24/test_2.txt')
    print('TEST 2')
    print('test 2:', sol.solution_1(), 'should equal ?')
    print('SOLUTION')
    sol = Solution('2024/Day_24/task.txt')
   # print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2_v1_for_tests())
    print('Solution 2:', sol.solution_2())
   


if __name__ == '__main__':
    main()
