'''
Advent of Code 
2022 day 12
my solution to tasks from day 12

solution 1 - 
solution 2 - 

'''

from queue import PriorityQueue
from copy import deepcopy

def get_map(filename):
    my_map, starting_point, ending_point, y = [], (0, 0), (0, 0), 0
    with open(filename, 'r') as myfile:
        for line in myfile:
            if 'S' in line:
                starting_point = (y, line.find('S'))
                line = line.replace('S', 'a')
            if 'E' in line:
                ending_point = (y, line.find('E'))
                line = line.replace('E', 'z')
            my_map.append(line.strip())
            y += 1
    return my_map, starting_point, ending_point

def check_difference(my_map, point_1, point_2):
    if ord(my_map[point_2[0]][point_2[1]]) - ord(my_map[point_1[0]][point_1[1]]) < 2:
        return True
    return False


def get_new_points(my_map, act_point):
    if act_point[0] > 0 and check_difference(my_map, act_point, (act_point[0] - 1, act_point[1])):
        yield (act_point[0] - 1, act_point[1])
    if act_point[1] > 0 and check_difference(my_map, act_point, (act_point[0], act_point[1] - 1)):
        yield (act_point[0], act_point[1] - 1)
    if act_point[0] < len(my_map) - 1 and check_difference(my_map, act_point, (act_point[0] + 1, act_point[1])):
        yield (act_point[0] + 1, act_point[1])
    if act_point[1] < len(my_map[act_point[0]]) - 1 and check_difference(my_map, act_point, (act_point[0], act_point[1] + 1)):
        yield (act_point[0], act_point[1] + 1)
    

def solution_1(my_map, starting_point, ending_point):
    queue_of_positions, visited_points = PriorityQueue(), set()
    visited_points.add(starting_point)
    queue_of_positions.put((0, starting_point))
    act_pos = None
    while not queue_of_positions.empty():
        act_priority, act_pos = queue_of_positions.get()
        if act_pos == ending_point:
            break
        for point in get_new_points(my_map, act_pos):
            if point not in visited_points:
                visited_points.add(point)
                queue_of_positions.put((act_priority + 1, point))
    return act_priority



def main():
    test_map, test_start, test_stop = get_map('2022/Day_12/test.txt')
    print('test 1:', solution_1(test_map, test_start, test_stop))
    task_map, task_start, task_stop = get_map('2022/Day_12/task.txt')
    print('Solution 1:', solution_1(task_map, task_start, task_stop))
    # print('test 2:', solution_2(test_monkeys, 10000))
    # print('Solution 2:', solution_2(test_monkeys, 10000))

if __name__ == '__main__':
    main()
    