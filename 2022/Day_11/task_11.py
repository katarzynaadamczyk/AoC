'''
Advent of Code 
2022 day 11
my solution to tasks from day 11

First I needed to parse well the input data. Function get_monkeys_info creates a list of monkeys dictionaries with all needed info.
solution 1 - For each monkey add field check_count. Then do required number of times throws from monkey 0 to len(monkeys). In each throw count new worry value (by operation and then division by 3), 
do a test  and append new worry value to chosen by test monkey. After finishing throws by one monkey add to its check_count length of items thrown. Then change the list to 
an empty list. After all the iterations get a list of all monkeys check_count, sort it in reverse order and return the result of multiplication of first two values.
solution 2 - Same as above, but count of the new worry value is done only by operation. The value added to chosen monkey is the result of new worry value modulo scm of each of test values.
scm - smallest common multiplication result (I took all the test values and multiplied them together)

'''

from functools import reduce


operation = 'operation'
test = 'test'
items = 'items'
check_count = 'check_count'
operation_val = 'operation_val'
test_val = 'test_val'

def get_monkeys_info(filename):
    monkeys_info, i = [], 0
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line.replace('old * old', 'old ** 2')
            i += 1
            line = [x.strip(':,') for x in line.strip().split()]
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
        monkeys[i].setdefault(check_count, 0)
    for i in range(no_of_turns):
        for index, monkey in enumerate(monkeys):
            for val in monkey[items]:
                new_val = monkey[operation](val, monkey[operation_val])
                monkeys[monkey[monkey[test](new_val, monkey[test_val])]][items].append(new_val % scm)
            monkeys[index][check_count] += len(monkey[items])
            monkeys[index][items] = []
    lst_of_no_of_checks = sorted([monkey[check_count] for monkey in monkeys], reverse=True)
    return lst_of_no_of_checks[0] * lst_of_no_of_checks[1]


def main():
    test_monkeys = get_monkeys_info('2022/Day_11/test.txt')
    print('test 1:', solution_1(test_monkeys, 20))
    task_monkeys = get_monkeys_info('2022/Day_11/task.txt')
    print('Solution 1:', solution_1(task_monkeys, 20))
    test_monkeys = get_monkeys_info('2022/Day_11/test.txt')
    print('test 2:', solution_2(test_monkeys, 10000))
    task_monkeys = get_monkeys_info('2022/Day_11/task.txt')
    print('Solution 2:', solution_2(task_monkeys, 10000))

if __name__ == '__main__':
    main()
    