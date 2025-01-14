'''
Advent of Code 
2024 day 21
my solution to tasks

task 1 - done 100% by myself, prepared a TreeNode for each operation and processed it

task 2 - as I tried to do it by myself I invented a way that there is a need to check if nodes contain appropriate
values as function and node, but my solution failed to work as there was some bug in the code
I found a working solution on reddit (https://www.reddit.com/r/adventofcode/comments/1hl698z/comment/m3kt1je/) and updated it 


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


class Solution:

    def __init__(self, filename) -> None:
        '''
        initialize Solution
        '''
        self.nodes = {} # str: TreeNode
        self.operations = {} # (result: {'func': func, 'nodes': (node1, node2)})
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
                    self.operations.setdefault(line[-1], {'func': line[1], 'nodes': (line[0], line[2])})


    def get_values(self, start_char='z'):
        '''
        get number for start_char starting wires
        '''
        z_names = sorted(filter(lambda x: x.startswith(start_char), self.nodes_values.keys()), reverse=True)
        z_values = ''.join([str(self.nodes_values[x]) for x in z_names])
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
        go through all inputs and outputs and check if logic is correct
        add to results wires will see what happens
        '''
        # set to store wrong wires
        results = set()
        highest_z = 'z' + str(max([int(x[1:]) for x in self.nodes.keys() if x[0] == 'z']))
        for res, func_node_dict in self.operations.items():
            if res[0] == "z" and func_node_dict['func'] != "XOR" and res != highest_z:
                results.add(res)
            if (func_node_dict['func'] == "XOR" and res[0] not in ["x", "y", "z"] \
                and func_node_dict['nodes'][0][0] not in ["x", "y", "z"] and func_node_dict['nodes'][1][0] not in ["x", "y", "z"]):
                results.add(res)
            if func_node_dict['func'] == "AND" and "x00" not in func_node_dict['nodes']:
                for sub_func_node_dict in filter(lambda x: res in x['nodes'], self.operations.values()):
                    if sub_func_node_dict['func'] != "OR":
                        results.add(res)
            if func_node_dict['func'] == "XOR":
                for sub_func_node_dict in filter(lambda x: res in x['nodes'], self.operations.values()):
                    if sub_func_node_dict['func'] == "OR":
                        results.add(res)
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
    print('Solution 2:', sol.solution_2())
   


if __name__ == '__main__':
    main()
