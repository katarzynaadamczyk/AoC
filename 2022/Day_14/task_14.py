'''
Advent of Code 
2022 day 14
my solution to tasks from day 14


solution 1 - 
solution 2 - 


'''

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



def solution_1(walls, sand_start):
    sands, act_sand_pos = set(), sand_start
    y_max = max(walls, key=lambda coord: (coord[1], coord[0]))[1]
    print(y_max)
    return 0

   

        

def main():
    test_walls, sand_test_start = get_walls('2022/Day_14/test.txt')
    print('test 1:', solution_1(test_walls, sand_test_start))
    task_walls, sand_task_start = get_walls('2022/Day_14/task.txt')
    print('Solution 1:', solution_1(task_walls, sand_task_start))
  #  print('test 2:', solution_2(test_packets))
   # print('Solution 2:', solution_2(task_packets))

if __name__ == '__main__':
    main()
    