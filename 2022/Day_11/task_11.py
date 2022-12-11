'''
Advent of Code 
2022 day 11
my solution to tasks from day 1

solution 1 - 
solution 2 - 

'''


def get_monkeys_info(filename):
    monkeys_info, i = [], 0
    with open(filename, 'r') as myfile:
        for line in myfile:
            i += 1
            line = [x.strip(':,') for x in line.strip().split()]
            print(line)
            if i == 1:
                act_monkey = {}
            elif i == 2:
                act_monkey.setdefault('items', [int(x) for x in line[2:]])
            elif i == 3:
                if line[-2] == '+':
                    act_monkey.setdefault('operation', lambda x: (x + int(line[-1])) // 3)
                elif line[-2] == '*':
                    act_monkey.setdefault('operation', lambda x: (x * int(line[-1]) // 3))
            elif i == 4:
                act_monkey.setdefault('test', lambda x: x % int(line[-1]) == 0)
            elif i == 5:
                act_monkey.setdefault(True, int(line[-1]))
            elif i == 6:
                act_monkey.setdefault(False, int(line[-1]))
            elif i == 7:
                monkeys_info.append(act_monkey)
                i = 0
    return monkeys_info


def solution_1(program, lst_of_no_of_cycles):
    return reduce(lambda x, y: x + y, [program[i] * i for i in lst_of_no_of_cycles])


def check_if_crt_is_in_pos(cycle_no, x_val, len_of_crt):
    if cycle_no in range(x_val, x_val + len_of_crt):
        return True
    return False


def solution_2(program, no_of_lines, no_of_chars_in_line, len_of_crt):
    screen, line = [], ''
    for cycle_no in range(1, no_of_lines * no_of_chars_in_line + 1):
        pos_to_check = cycle_no % no_of_chars_in_line if cycle_no % no_of_chars_in_line != 0 else no_of_chars_in_line
        if check_if_crt_is_in_pos(pos_to_check, program[cycle_no], len_of_crt):
            line += '#'
        else:
            line += '.'
        if cycle_no % no_of_chars_in_line == 0:
            screen.append(line)
            line = ''
    return '\n' + '\n'.join(screen)

def main():
    test_monkeys = get_monkeys_info('2022/Day_11/test.txt')
    print(len(test_monkeys))
   # print('test 1:', solution_1(test_program, [20, 60, 100, 140, 180, 220]))
    task_monkeys = get_monkeys_info('2022/Day_11/task.txt')
    print(len(task_monkeys))
   # print('Solution 1:', solution_1(task_program, [20, 60, 100, 140, 180, 220]))
   # print('test 2:', solution_2(test_program, 6, 40, 3))
   # print('Solution 2:', solution_2(task_program, 6, 40, 3))

if __name__ == '__main__':
    main()
    