'''
Advent of Code 
2022 day 21
my solution to tasks from day 21


solution 1 - 
solution 2 - 

'''
from queue import Queue

operations = {
              '+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '*': lambda x, y: x * y,
              '/': lambda x, y: x // y
              }

values = 'values'
operation_sign = 'operation'

def get_monkey_shouts(filename):
    results, monkey_operations, monkey_dependance = {}, {}, {}
    with open(filename, 'r') as myfile:
        for line in myfile:
            monkey, operation = line.strip().split(': ')
            operation = operation.split()
            if len(operation) == 1:
                results.setdefault(monkey, int(operation[0]))
            else:
                monkey_dict = {values: (operation[0], operation[2]),
                               operation_sign: operation[1]}
                monkey_operations.setdefault(monkey, monkey_dict)
                monkey_dependance.setdefault(operation[0], set())
                monkey_dependance.setdefault(operation[2], set())
                monkey_dependance[operation[0]].add(monkey)
                monkey_dependance[operation[2]].add(monkey)
    print(results)
    print(monkey_operations)
    print(monkey_dependance)
    
    return results, monkey_operations, monkey_dependance





def solution_1(results, monkey_operations, monkey_dependance):
    
    return 0

  
def main():
    test_results, test_monkey_operations, test_monkey_dependance = get_monkey_shouts('2022/Day_21/test.txt')
    print('test 1:', solution_1(test_results, test_monkey_operations, test_monkey_dependance))
    task_results, task_monkey_operations, task_monkey_dependance = get_monkey_shouts('2022/Day_21/task.txt')
  #  print('Solution 1:', solution_1(task_results, task_monkey_operations, task_monkey_dependance))
  #  print('test 2:', solution_2(test_valves, test_start_valve, 26))
   # print('Solution 2:', solution_2(task_valves, task_start_valve, 26))
    
    
if __name__ == '__main__':
    main()
    