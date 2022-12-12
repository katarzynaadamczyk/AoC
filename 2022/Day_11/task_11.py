'''
Advent of Code 
2022 day 11
my solution to tasks from day 11

solution 1 - 
solution 2 - 

'''

from functools import reduce


operation = 'operation'
test = 'test'
items = 'items'
check_count = 'check_count'
check_count_2 = 'check_count_2'
operation_val = 'operation_val'
test_val = 'test_val'

def get_monkeys_info(filename):
    monkeys_info, i = [], 0
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line.replace('old * old', 'old ** 2')
            i += 1
            line = [x.strip(':,') for x in line.strip().split()]
            #print(line)
            if i == 1:
                act_monkey = {}
            elif i == 2:
                act_monkey.setdefault(items, [int(x) for x in line[2:]])
            elif i == 3:
                act_monkey.setdefault(operation_val, int(line[-1]))
                if line[-2] == '+':
                    act_monkey.setdefault(operation, lambda x, y: x + y)
                elif line[-2] == '*':
                    act_monkey.setdefault(operation, lambda x, y: x * y)
                elif line[-2] == '**':
                    act_monkey.setdefault(operation, lambda x, y: x ** y)
            elif i == 4:
                act_monkey.setdefault(test_val, int(line[-1]))
                act_monkey.setdefault(test, lambda x, y: x % y == 0)
            elif i == 5:
                act_monkey.setdefault(True, int(line[-1]))
            elif i == 6:
                act_monkey.setdefault(False, int(line[-1]))
            elif i == 7:
                monkeys_info.append(act_monkey)
                i = 0
    return monkeys_info


def solution_1(monkeys, no_of_turns):
    for i in range(len(monkeys)):
        monkeys[i].setdefault(check_count, 0)
    for _ in range(no_of_turns):
        for index, monkey in enumerate(monkeys):
            for val in monkey[items]:
                new_val = monkey[operation](val, monkey[operation_val]) // 3
                monkeys[monkey[monkey[test](new_val, monkey[test_val])]][items].append(new_val)
            monkeys[index][check_count] += len(monkey[items])
            monkeys[index][items] = []
    lst_of_no_of_checks = sorted([monkey[check_count] for monkey in monkeys], reverse=True)
    return lst_of_no_of_checks[0] * lst_of_no_of_checks[1]

def solution_2(monkeys, no_of_turns):
    set_of_tests = set([monkey[test_val] for monkey in monkeys])
    scm = reduce(lambda x, y: x * y, list(set_of_tests))
    for i in range(len(monkeys)):
        monkeys[i].setdefault(check_count_2, 0)
    for i in range(no_of_turns):
        for index, monkey in enumerate(monkeys):
            for val in monkey[items]:
                new_val = monkey[operation](val, monkey[operation_val])
                new_val_2 = new_val
                while new_val_2 % scm == 0:
                    new_val_2 //= scm
                monkeys[monkey[monkey[test](new_val, monkey[test_val])]][items].append(new_val_2)
            monkeys[index][check_count_2] += len(monkey[items])
            monkeys[index][items] = []
        if i % 1000 == 0:
            print(i)
       # print([monkey[items] for monkey in monkeys])
       # print([monkey[check_count_2] for monkey in monkeys])
    lst_of_no_of_checks = sorted([monkey[check_count_2] for monkey in monkeys], reverse=True)
  #  print(lst_of_no_of_checks)
    return lst_of_no_of_checks[0] * lst_of_no_of_checks[1]


def main():
    test_monkeys = get_monkeys_info('2022/Day_11/test.txt')
    print('test 1:', solution_1(test_monkeys, 20))
    task_monkeys = get_monkeys_info('2022/Day_11/task.txt')
    print('Solution 1:', solution_1(task_monkeys, 20))
    test_monkeys = get_monkeys_info('2022/Day_11/test.txt')
    print('test 2:', solution_2(test_monkeys, 10000))
    task_monkeys = get_monkeys_info('2022/Day_11/task.txt')
    print('Solution 2:', solution_2(test_monkeys, 10000))

if __name__ == '__main__':
    main()
    