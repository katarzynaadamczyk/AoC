'''
Advent of Code 
2022 day 14
my solution to tasks from day 14


solution 1 - 
solution 2 - 


'''

from copy import deepcopy

def get_walls(filename):
    walls = set()
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line.strip().split(' -> ')
            line = list(map(lambda x: tuple([int(a) for a in x.split(',')]), line))
            for coord_1, coord_2 in zip(line[:-1], line[1:]):
                for x in range(min(coord_1[0], coord_2[0]), max(coord_1[0], coord_2[0]) + 1):
                    for y in range(min(coord_1[1], coord_2[1]), max(coord_1[1], coord_2[1]) + 1):
                        walls.add((x, y))
    return walls, (500, 0)


def may_go_down(walls_and_sands, sand_pos):
    if (sand_pos[0], sand_pos[1] + 1) not in walls_and_sands:
        return True
    return False

def may_go_right(walls_and_sands, sand_pos):
    if (sand_pos[0] - 1, sand_pos[1] + 1) not in walls_and_sands:
        return True
    return False

def may_go_left(walls_and_sands, sand_pos):
    if (sand_pos[0] + 1, sand_pos[1] + 1) not in walls_and_sands:
        return True
    return False

def get_new_sand_pos(walls_and_sands, sand_pos):
    if may_go_down(walls_and_sands, sand_pos):
        return (sand_pos[0], sand_pos[1] + 1)
    if may_go_right(walls_and_sands, sand_pos):
        return (sand_pos[0] - 1, sand_pos[1] + 1)
    if may_go_left(walls_and_sands, sand_pos):
        return (sand_pos[0] + 1, sand_pos[1] + 1)
    return sand_pos


def solution_1(walls, sand_start):
    sands, act_sand_pos, new_sand_pos = set(), sand_start, sand_start
    y_max = max(walls, key=lambda coord: (coord[1], coord[0]))[1]
    while new_sand_pos[1] < y_max:
        act_sand_pos = sand_start
        new_sand_pos = get_new_sand_pos(walls.union(sands), act_sand_pos)
        while new_sand_pos != act_sand_pos and new_sand_pos[1] < y_max:
            act_sand_pos = new_sand_pos
            new_sand_pos = get_new_sand_pos(walls.union(sands), act_sand_pos)
        if new_sand_pos[1] < y_max:
            sands.add(new_sand_pos)
    return len(sands)

def solution_1(walls, sand_start):
    sands, act_sand_pos, new_sand_pos = set(), sand_start, sand_start
    y_max = max(walls, key=lambda coord: (coord[1], coord[0]))[1]
    while new_sand_pos[1] < y_max:
        act_sand_pos = sand_start
        new_sand_pos = get_new_sand_pos(walls.union(sands), act_sand_pos)
        while new_sand_pos != act_sand_pos and new_sand_pos[1] < y_max:
            act_sand_pos = new_sand_pos
            new_sand_pos = get_new_sand_pos(walls.union(sands), act_sand_pos)
        if new_sand_pos[1] < y_max:
            sands.add(new_sand_pos)
    return len(sands)


def get_new_sand_pos_2(walls_and_sands, sand_pos, y_max):
    if sand_pos[1] + 1 < y_max:
        if may_go_down(walls_and_sands, sand_pos):
            yield (sand_pos[0], sand_pos[1] + 1)
        if may_go_right(walls_and_sands, sand_pos):
            yield (sand_pos[0] - 1, sand_pos[1] + 1)
        if may_go_left(walls_and_sands, sand_pos):
            yield (sand_pos[0] + 1, sand_pos[1] + 1)


def add_sand_points(walls_and_sands, act_sand_pos, y_max):
    for new_sand_pos in get_new_sand_pos_2(walls_and_sands, act_sand_pos, y_max):
        walls_and_sands.add(new_sand_pos)
        add_sand_points(walls_and_sands, new_sand_pos, y_max)

def solution_2(walls, sand_start):
    sands, act_sand_pos = deepcopy(walls), sand_start
    y_max = max(walls, key=lambda coord: (coord[1], coord[0]))[1] + 2
    sands.add(act_sand_pos)
    add_sand_points(sands, act_sand_pos, y_max)
    return len(sands) - len(walls)


# old version, working but slow (supposedly working) did not check as it will take too much time

def get_new_sand_pos_2_2(walls_and_sands, sand_pos, y_max):
    if sand_pos[1] + 1 < y_max:
        if may_go_down(walls_and_sands, sand_pos):
            return (sand_pos[0], sand_pos[1] + 1)
        if may_go_right(walls_and_sands, sand_pos):
            return (sand_pos[0] - 1, sand_pos[1] + 1)
        if may_go_left(walls_and_sands, sand_pos):
            return (sand_pos[0] + 1, sand_pos[1] + 1)
    return sand_pos 


def solution_2_2(walls, sand_start):
    sands, act_sand_pos, new_sand_pos = set(), sand_start, sand_start
    y_max = max(walls, key=lambda coord: (coord[1], coord[0]))[1] + 2
    while act_sand_pos not in sands:
        new_sand_pos = get_new_sand_pos_2_2(walls.union(sands), act_sand_pos, y_max)
        while new_sand_pos != act_sand_pos:
            act_sand_pos = new_sand_pos
            new_sand_pos = get_new_sand_pos_2_2(walls.union(sands), act_sand_pos, y_max)
        sands.add(new_sand_pos)
        act_sand_pos = sand_start
    return len(sands)
    

        

def main():
    test_walls, sand_test_start = get_walls('2022/Day_14/test.txt')
    print('test 1:', solution_1(test_walls, sand_test_start))
    task_walls, sand_task_start = get_walls('2022/Day_14/task.txt')
    print('Solution 1:', solution_1(task_walls, sand_task_start))
    print('test 2:', solution_2(test_walls, sand_test_start))
    print('Solution 2:', solution_2(task_walls, sand_task_start))
    
    
if __name__ == '__main__':
    main()
    