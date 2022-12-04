'''
Advent of Code 
2015 day 3
my solution to tasks from day 3

solution 1 - 
solution 2 - 

'''


def solution_1(filename):
    points = set()
    act_point = (0, 0)
    points.add(act_point)
    where_to_go_dict = {'^': (0, 1), 'v': (0, -1), '>': (1, 0), '<': (-1, 0)}
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line.strip()
            add = lambda x_1, x_2: (x_1[0] + x_2[0], x_1[1] + x_2[1])
            for char in line:
                act_point = add(act_point, where_to_go_dict[char])
                points.add(act_point) 
    return len(points)

def solution_2(filename):
    points = set()
    act_point_santa, act_point_robot = (0, 0), (0, 0)
    points.add(act_point_santa)
    where_to_go_dict = {'^': (0, 1), 'v': (0, -1), '>': (1, 0), '<': (-1, 0)}
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line.strip()
            add = lambda x_1, x_2: (x_1[0] + x_2[0], x_1[1] + x_2[1])
            santa = True
            for char in line:
                if santa:
                    act_point_santa = add(act_point_santa, where_to_go_dict[char])
                    points.add(act_point_santa) 
                    santa = False
                else:
                    santa = True
                    act_point_robot = add(act_point_robot, where_to_go_dict[char])
                    points.add(act_point_robot) 
    return len(points)

def main():
    print(f'Result for test data for task 1 is {solution_1("2015/Day_3/testdata.txt")}')
    print(f'Result for data for task 1 is {solution_1("2015/Day_3/data.txt")}')
    
    
    print(f'Result for test data for task 2 is {solution_2("2015/Day_3/testdata.txt")}')
    print(f'Result for data for task 2 is {solution_2("2015/Day_3/data.txt")}')
    
if __name__ == '__main__':
    main()