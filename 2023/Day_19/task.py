'''
Advent of Code 
2023 day 19
my solution to task 1 

solution 1 - just for each part follow the process as described in the task. To do so, I created a dict of workflows, keys are names, items are dicts :). 
For each part check their final answer -> make tests until it gets to either R or A. If it ends at A then add it to result. 
At the end sum all the data for each point and sum them together.

'''
from queue import Queue

class Solution:

    ACCEPTED = 'A'
    REJECTED = 'R'

    ACC_REJ = 'AR'

    TEST = {'>': lambda point, param, val: point[param] > val,
            '<': lambda point, param, val: point[param] < val}

    PARAM = 'param'
    TEST_NAME = 'test'
    TEST_VALUE = 'val'
    TEST_PASS = 'ok'
    TEST_FAIL = 'nok'

    def __init__(self, filename) -> None:
        self.get_data(filename)


    def get_data(self, filename):
        self.nodes, self.points = {}, {}
        with open(filename, 'r') as myfile:
            line = myfile.readline()
            while line and line != '\n':
                line = line.strip()
                node_name = line[:line.find('{')]
                line = line[line.find('{') + 1:-1]
                new_node = self.process_test(line)
                self.nodes[node_name] = new_node
                line = myfile.readline()
            line = myfile.readline()
            i = 0
            while line:
                line = line.strip()[1:-1]
                line = line.split(',')
                line = [param.split('=') for param in line]
                line = {x: int(y) for x, y in line}
                self.points.setdefault(i, line)
                i += 1
                line = myfile.readline()


    def process_test(self, tests):
        if ',' in tests:
            first_part = dict()
            comma_i = tests.find(',')
            if '>' in tests[:comma_i]:
                sign = '>'
            else:
                sign = '<'
            test_end_i = tests.find(':')
            sign_i = tests.find(sign)
            first_part[Solution.PARAM] = tests[:sign_i]
            first_part[Solution.TEST_NAME] = sign
            first_part[Solution.TEST_VALUE] = int(tests[sign_i+1:test_end_i])
            first_part[Solution.TEST_PASS] = tests[test_end_i + 1:comma_i]
            first_part[Solution.TEST_FAIL] = self.process_test(tests[comma_i+1:])
            return first_part
        else:
            return tests
    
    def consider_workflow(self, name, point):
        result = self.nodes[name]
        while type(result) != str:
            if Solution.TEST[result[Solution.TEST_NAME]](point, result[Solution.PARAM], result[Solution.TEST_VALUE]):
                result = result[Solution.TEST_PASS]
            else:
                result = result[Solution.TEST_FAIL]
        return result

        
    def get_value(self, point):
        act_val = 'in'
        while act_val not in Solution.ACC_REJ:
            act_val = self.consider_workflow(act_val, point)
        return act_val

    def solution_1(self):
        accepted = []
        for i, point in self.points.items():
            act_val = self.get_value(point)
            if act_val == Solution.ACCEPTED:
                accepted.append(i)
        print(accepted)
        return sum([sum(self.points[x].values()) for x in accepted])


def main():
    print('TASK 1')
    sol = Solution('2023/Day_19/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1())
    sol = Solution('2023/Day_19/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())


if __name__ == '__main__':
    main()
