'''
Advent of Code 
2015 day 7
my solution to task 1 & 2

solution 1 & 2 - create a set of ready-to-go values, and a dict of values/dict of params and function to calculate the value.
Then make calculations until the required parameter can be found in set of calculated values.

'''

functions = {'AND': lambda a, b: a & b,
             'OR': lambda a, b: a | b,
             'LSHIFT': lambda a, b: a << b,
             'RSHIFT': lambda a, b: a >> b,
             'NOT': lambda a: ~ a,
             'EMPTY': lambda a: a}

def solution_1(filename, val_to_get):
    act_values = set()
    act_tasks = dict()
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line.strip().split()
            if len(line) == 3 and line[0].isdigit():
                act_values.add(line[-1])
                act_tasks.setdefault(line[-1], int(line[0]))
            else:
                act_val = line[-1]
                line = line[:-2]
                for i, val in enumerate(line):
                    if val.isdigit():
                        line[i] = int(val)
                        act_values.add(line[i])
                        act_tasks[line[i]] = line[i]
                if len(line) == 1:
                    act_tasks.setdefault(act_val, {'PARAMS': (line[0],), 'FUNC': 'EMPTY'})
                elif len(line) == 2:
                    act_tasks.setdefault(act_val, {'PARAMS': (line[1],), 'FUNC': line[0]})
                elif len(line) == 3:
                    act_tasks.setdefault(act_val, {'PARAMS': (line[0], line[2]), 'FUNC': line[1]})
    while val_to_get not in act_values:
        vals_to_change = {}
        for key, act_dict in act_tasks.items():
            if type(act_dict) == int:
                continue
            can_do = True
            for param in act_dict['PARAMS']:
                if param not in act_values:
                    can_do = False
                    break
            if can_do:
                if len(act_dict['PARAMS']) == 1:
                    vals_to_change[key] = functions[act_dict['FUNC']](act_tasks[act_dict['PARAMS'][0]])
                elif len(act_dict['PARAMS']) == 2:
                    vals_to_change[key] = functions[act_dict['FUNC']](act_tasks[act_dict['PARAMS'][0]], act_tasks[act_dict['PARAMS'][1]])
                
        for key, val in vals_to_change.items():
            act_tasks[key] = val
            act_values.add(key)
    return act_tasks.get(val_to_get, 0)

def main():
    print('test 1:', solution_1('2015/Day_7/test.txt', 'g'))
    print('Solution 1:', solution_1('2015/Day_7/task.txt', 'a'))
    
    print('Solution 2:', solution_1('2015/Day_7/task_2.txt', 'a'))

if __name__ == '__main__':
    main()
