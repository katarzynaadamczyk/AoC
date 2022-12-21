'''
Advent of Code 
2022 day 21
my solution to tasks from day 21


solution 1 - 
solution 2 - 

'''

values = 'values'
operation_sign = 'operation'

class MonkeyShout:
    
    operations = {
              '+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '*': lambda x, y: x * y,
              '/': lambda x, y: x // y,
              '=': lambda x, y: x == y
              }
    
    def __init__(self, results, monkey_operations, name) -> None:
        self.name = name
        if name in monkey_operations.keys():
            self.value = None
            self.left = MonkeyShout(results, monkey_operations, monkey_operations[name][values][0])
            self.right = MonkeyShout(results, monkey_operations, monkey_operations[name][values][1])
            self.operation = monkey_operations[name][operation_sign]
        elif name in results.keys():
            self.value = results[name]
            
    def get_value(self):
        if hasattr(self, 'left'):
            return MonkeyShout.operations[self.operation](self.left.get_value(), self.right.get_value())
        else:
            return self.value
    
    def has_name_below(self, name):
        if self.name == name:
                return True
        if hasattr(self, 'left'):
            return self.left.has_name_below(name) or self.right.has_name_below(name)
        else:
            return False
        
    
    def __repr__(self):
        return self.name + ', left: ' + self.left.name + ', right: ' + self.right.name

    def __str__(self):
        return self.name + ', val: ' + str(self.get_value())

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
    return results, monkey_operations #, monkey_dependance






def solution_1(results, monkey_operations, name):
    root = MonkeyShout(results, monkey_operations, name)
    return root.get_value()

def solution_2(results, monkey_operations, name_1, name_2):
    monkey_operations[name_1][operation_sign] = '='
    results[name_2] = 512580000000
    root = MonkeyShout(results, monkey_operations, name_1)
    print(root.get_value())
    print(root.left.has_name_below(name_2))
    print(root.right.has_name_below(name_2))
    print(MonkeyShout(results, monkey_operations, name_2).get_value())
    
    print(root.get_value())
    print(root.left.get_value())
    print(root.right.get_value())
   # while MonkeyShout(results, monkey_operations, name_1).get_value() != 1:
   #     results[name_2] += 1
    return results[name_2]

  
def main():
   # test_results, test_monkey_operations = get_monkey_shouts('2022/Day_21/test.txt') # , test_monkey_dependance
   # print('test 1:', solution_1(test_results, test_monkey_operations, 'root'))
    task_results, task_monkey_operations = get_monkey_shouts('2022/Day_21/task.txt') # , task_monkey_dependance
    print('Solution 1:', solution_1(task_results, task_monkey_operations, 'root'))
  #  print('test 2:', solution_2(task_results, task_monkey_operations, 'root', 'humn'))
    print('Solution 2:', solution_2(task_results, task_monkey_operations, 'root', 'humn'))
    
    
if __name__ == '__main__':
    main()
    