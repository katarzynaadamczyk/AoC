'''
Advent of Code 
2022 day 23
my solution to tasks from day 23


solution 1 - 
solution 2 - 

'''


class Elf:
    
    directions = ['N', 'S', '']
    
    def __init__(self, x, y) -> None:
        self.position = (x, y)
        self.direction = 'N'
            
    def get_position(self):
        return self.position
        
    def __repr__(self):
        return 'Elf on pos: ' + str(self.position)
    
    def __str__(self):
        return 'Elf on pos: ' + str(self.position)
    
class Board:
    
    def __init__(self, elves_positions) -> None:
        self.Elves = [Elf(position) for position in elves_positions]

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


  
def main():
    test_results, test_monkey_operations = get_monkey_shouts('2022/Day_21/test.txt') # , test_monkey_dependance
    print('test 1:', solution_1(test_results, test_monkey_operations, 'root'))
    task_results, task_monkey_operations = get_monkey_shouts('2022/Day_21/task.txt') # , task_monkey_dependance
    print('Solution 1:', solution_1(task_results, task_monkey_operations, 'root'))
 #   print('test 2:', solution_2(test_results, test_monkey_operations, 'root', 'humn'))
 #   print('Solution 2:', solution_2(task_results, task_monkey_operations, 'root', 'humn'))
    
    
if __name__ == '__main__':
    main()
    