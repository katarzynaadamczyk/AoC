'''
Advent of Code 
2023 day 3
my solution to task 1 & 2

solution 1 - 
solution 2 - 

'''

def import_map(filename):
    act_map = []
    with open(filename, 'r') as myfile:
        for line in myfile:
            act_map.append(line.strip())
    return act_map

def check(engine_map, x, y):
    for y_check in range(max(0, y - 1), min(len(engine_map), y + 2)):
        if not (engine_map[y_check][x].isdigit() or engine_map[y_check][x] == '.'):
            return True
    return False

def solution_1(filename):
    engine_map = import_map(filename)
    max_x, max_y = len(engine_map[0]), len(engine_map)
    act_num, act_sum, add = '', 0, False
    for act_y in range(max_y):
        for act_x in range(max_x):
            if engine_map[act_y][act_x].isdigit():
                act_num += engine_map[act_y][act_x]
                if len(act_num) == 1:
                    if act_x > 0:
                        add = check(engine_map, act_x - 1, act_y)
                if not add:
                    add = check(engine_map, act_x, act_y)
            elif len(act_num) > 0:
                if not add:
                    if act_x < max_x - 1:
                        add = check(engine_map, act_x, act_y)
                if add:
                    act_sum += int(act_num)
                    add = False
                act_num = ''
    return act_sum

def solution_2(filename):
    powers_sum = 0
    return powers_sum

def main():
    print('test 1:', solution_1('2023/Day_3/test_1.txt'))
    print('Solution 1:', solution_1('2023/Day_3/task.txt'))
    
   # print('test 2:', solution_2('2023/Day_2/test_1.txt'))
  #  print('Solution 2:', solution_2('2023/Day_2/task_1.txt'))

if __name__ == '__main__':
    main()
