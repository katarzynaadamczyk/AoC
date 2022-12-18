'''
Advent of Code 
2022 day 18
my solution to tasks from day 18


solution 1 - 
solution 2 - 

'''


def get_cubes(filename):
    cubes = []
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line.strip().split(',')
            cubes.append(tuple([int(x) for x in line]))
    return cubes


def manhattan_distance(point_1, point_2):
    return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1]) + abs(point_1[2] - point_2[2])


def solution_1(cubes):
    count_touching_cubes = 0
    for index, cube_1 in enumerate(cubes[:-1]):
        for cube_2 in cubes[index + 1:]:
            if manhattan_distance(cube_1, cube_2) == 1:
                count_touching_cubes += 1
    return len(cubes) * 6 - count_touching_cubes * 2

  
def main():
    test_cubes = get_cubes('2022/Day_18/test.txt')
    print('test 1:', solution_1(test_cubes))
    task_cubes = get_cubes('2022/Day_18/task.txt')
    print('Solution 1:', solution_1(task_cubes))
  #  print('test 2:', solution_2(test_valves, test_start_valve, 26))
   # print('Solution 2:', solution_2(task_valves, task_start_valve, 26))
    
    
if __name__ == '__main__':
    main()
    