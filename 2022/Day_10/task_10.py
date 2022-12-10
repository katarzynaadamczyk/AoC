'''
Advent of Code 
2022 day 10
my solution to tasks from day 10

solution 1 - 
solution 2 - 

'''
from functools import reduce


functions = {
                'noop': lambda x: ([x], x),
                'addx': lambda x, new_val: ([x, x], x + new_val)
            }

def get_program(filename):
    program, x = [1], 1
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line.strip().split()
            line, x = functions[line[0]](x) if len(line) == 1 else functions[line[0]](x, int(line[1]))
            program = program + line
    return program


def solution_1(program, lst_of_no_of_cycles):
    result = reduce(lambda x, y: x + y, [program[i] * i for i in lst_of_no_of_cycles])
    return result


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
    test_program = get_program('2022/Day_10/test.txt')
    print('test 1:', solution_1(test_program, [20, 60, 100, 140, 180, 220]))
    task_program = get_program('2022/Day_10/task.txt')
    print('Solution 1:', solution_1(task_program, [20, 60, 100, 140, 180, 220]))
    print('test 2:', solution_2(test_program, 6, 40, 3))
    print('Solution 2:', solution_2(task_program, 6, 40, 3))

if __name__ == '__main__':
    main()
    