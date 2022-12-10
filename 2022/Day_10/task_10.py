'''
Advent of Code 
2022 day 10
my solution to tasks from day 10

solution 1 - 
solution 2 - 

'''
from functools import reduce


functions = {
                'noop': lambda x: [x],
                'addx': lambda x, new_val: functions['noop'](x) + [x + new_val]
            }

def get_program(filename):
    program = [1]
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line.strip().split()
            if len(line) == 2:
                program = program + functions[line[0]](program[-1], int(line[1]))
            else:
                 program = program + functions[line[0]](program[-1])
    return program


def solution_1(program, lst_of_no_of_cycles):
    result = reduce(lambda x, y: x + y, [program[i-1] * i for i in lst_of_no_of_cycles])
    return result


def solution_2(program, no_of_lines, no_of_chars_in_line, len_of_crt):
    screen = []
    for y in range(no_of_lines):
        line = ''
        for x in range(no_of_chars_in_line):
            
            pass
    print(screen)
    return screen

def main():
    test_program = get_program('2022/Day_10/test.txt')
    print('test 1:', solution_1(test_program, [20, 60, 100, 140, 180, 220]))
    task_program = get_program('2022/Day_10/task.txt')
    print('Solution 1:', solution_1(task_program, [20, 60, 100, 140, 180, 220]))

if __name__ == '__main__':
    main()
    