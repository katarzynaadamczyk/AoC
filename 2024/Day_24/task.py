'''
Advent of Code 
2024 day 21
my solution to tasks

task 1 - 

task 2 - 


'''

import time

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
    

    def __init__(self, func='', next_nodes=None, value=-1):
        '''
        initialize TreeNode
        '''
        self.func = func
        self.next_nodes = next_nodes
        self.value = value

    def update_next_nodes(self, nodes):
        if self.next_nodes is not None:
            self.next_nodes = [nodes[node] for node in self.next_nodes]

    def get_value(self):
        if self.value == -1:    
            self.value = TreeNode.actions[self.func](*[node.get_value() for node in self.next_nodes])
        return self.value
    


class Solution:

    def __init__(self, filename) -> None:
        '''
        initialize Solution
        '''
        self.nodes = {} # str: TreeNode
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
                    self.nodes.setdefault(line[:i], TreeNode(value=int(line[i+1:].strip())))
                else:
                    line = [x.strip() for x in line.strip().split()]
                    self.nodes.setdefault(line[-1], TreeNode(func=line[1], next_nodes=[line[0], line[2]]))

    def get_values(self, start_char='z'):
        z_names = sorted(filter(lambda x: x.startswith(start_char), self.nodes_values.keys()), reverse=True)
        z_values = ''.join([str(self.nodes_values[x]) for x in z_names])
        print(z_values)
        print(int(z_values, base=2))
        return z_values


    
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
    def solution_2(self) -> int:
        '''
        get result for task 2
        '''
        result = 0
        self.get_values('x')
        
        self.get_values('y')
        
        self.get_values('z')
        # TODO
        return 0
    


    

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
    print('Solution 2:', sol.solution_2()) 
   


if __name__ == '__main__':
    main()
