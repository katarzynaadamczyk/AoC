'''
Advent of Code 
2023 day 19
my solution to task 2 

solution 1 - with use of copy, deepcopy to copy the points (ending and starting values for each parameter) and as well with use of queue follow the
workflow to find all possible combinations. First point has all parameters set to min = 1, max = 4000. Then it goes with the workflow and divides 
itself into smaller pieces. At the end use reduce to count the possibilities for each point.

'''
from queue import Queue
from functools import reduce
from copy import deepcopy, copy

class Solution:

    @staticmethod
    def greater(param, value, point):
        if point[param][Solution.MAX] < value:
            return (None, point)
        if point[param][Solution.MIN] > value:
            return (point, None)
        point_1 = deepcopy(point)
        point_2 = deepcopy(point)
        point_2[param][Solution.MAX] = value
        point_1[param][Solution.MIN] = value + 1
        return (point_1, point_2)
    
    @staticmethod
    def lower(param, value, point):
        if point[param][Solution.MIN] > value:
            return (None, point)
        if point[param][Solution.MAX] < value:
            return (point, None)
        point_1 = deepcopy(point)
        point_2 = deepcopy(point)
        point_2[param][Solution.MIN] = value
        point_1[param][Solution.MAX] = value - 1
        return (point_1, point_2)
    

    ACCEPTED = 'A'
    REJECTED = 'R'

    ACC_REJ = 'AR'

    TEST = {'>': greater,
            '<': lower}

    PARAM = 'param'
    TEST_NAME = 'test'
    TEST_VALUE = 'val'
    TEST_PASS = 'ok'
    TEST_FAIL = 'nok'

    MIN = 'min'
    MAX = 'max'


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
        
    def get_new_point_workflow_pairs(self, workflow_name, point):
        pairs = []
        result = self.nodes[workflow_name]
        while type(result) != str:
            pass_point, point = Solution.TEST[result[Solution.TEST_NAME]](result[Solution.PARAM], result[Solution.TEST_VALUE], point)
            if pass_point is not None:
                pairs.append((pass_point, result[Solution.TEST_PASS]))
            result = result[Solution.TEST_FAIL]
        if point is not None:
            pairs.append((point, result))
        return pairs
    
    def consider_workflow(self, point):
        act_val = 'in'
        point_workflow_queue = Queue()
        point_workflow_queue.put((point, act_val))
        reached_A_points = []
        while not point_workflow_queue.empty():
            act_point, act_name = point_workflow_queue.get()
            if act_name == Solution.ACCEPTED:
                reached_A_points.append(act_point)
                continue
            if act_name == Solution.REJECTED:
                continue
            for new_point, new_workflow in self.get_new_point_workflow_pairs(act_name, act_point):
                point_workflow_queue.put((new_point, new_workflow))
        return reached_A_points

    
    def count_result(self, accepted):
        result = 0
        for point in accepted:
            tmp = []
            for param in point.keys():
                tmp.append(point[param][Solution.MAX] - point[param][Solution.MIN] + 1)
            result += reduce(lambda x, y: x * y, tmp)
        return result

    def solution_1(self):
        min_max_dict = {Solution.MIN: 1, Solution.MAX: 4000}
        point = {param: copy(min_max_dict) for param in 'xmas'}
        accepted = self.consider_workflow(point)
      #  print(accepted)
        return self.count_result(accepted)


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
