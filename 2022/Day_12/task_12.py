'''
Advent of Code 
2022 day 12
my solution to tasks from day 12

First, I introduced get_map function that returns prepared map (changed: S -> a, E -> z), starting point and ending point.
solution 1 - implemented A* algorithm. Put start point to a priority queue with priority 0. Add starting point to visited points. Then while queue is not empty get first element 
from queue. If it is ending point -> return its priority. Otherwise get all compatible points that are not visited and add them to queue with priority + 1. When the loop ends without
getting to the ending point return len(map) ** 2. 
solution 2 - get all possible starting points (points marked as a on the map). Then for each point count solution_1 and return minimum of all counted values.

'''

from queue import PriorityQueue

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
            return act_priority
        for point in get_new_points(my_map, act_pos):
            if point not in visited_points:
                visited_points.add(point)
                queue_of_positions.put((act_priority + 1, point))
    return len(my_map) ** 2

def get_all_starting_points(my_map):
    for y, row in enumerate(my_map):
        for x, char in enumerate(row):
            if char == 'a':
                yield (y, x)


def solution_2(my_map, ending_point):
    steps = [solution_1(my_map, point, ending_point) for point in get_all_starting_points(my_map)]
    return min(steps)

def main():
    test_map, test_start, test_stop = get_map('2022/Day_12/test.txt')
    print('test 1:', solution_1(test_map, test_start, test_stop))
    task_map, task_start, task_stop = get_map('2022/Day_12/task.txt')
    print('Solution 1:', solution_1(task_map, task_start, task_stop))
    print('test 2:', solution_2(test_map, test_stop))
    print('Solution 2:', solution_2(task_map, task_stop))

if __name__ == '__main__':
    main()
    