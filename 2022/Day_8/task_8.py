'''
Advent of Code 
2022 day 8
my solution to tasks from day 8

solution 1 - 
solution 2 - 

'''

def get_map(filename):
    my_map = []
    with open(filename, 'r') as myfile:
        for line in myfile:
            tmp = []
            line = line.strip()
            for char in line:
                tmp.append(int(char))
            my_map.append(tmp)
    return my_map


def get_max_up(my_map, x, y):
    return max([my_map[i][x] for i in range(0, y)])


def get_max_down(my_map, x, y):
    return max([my_map[i][x] for i in range(y + 1, len(my_map))])


def get_max_left(my_map, x, y):
    return max([my_map[y][i] for i in range(0, x)])


def get_max_right(my_map, x, y):
    return max([my_map[y][i] for i in range(x + 1, len(my_map[y]))])

def solution_1(my_map):
    visible_tree_counter = len(my_map) * 2 + (len(my_map[0]) - 2) * 2
    for y, row in enumerate(my_map[1:-1]):
        for x, tree in enumerate(row[1:-1]):
            if tree > min(get_max_up(my_map, x + 1, y + 1), get_max_down(my_map, x + 1, y + 1), get_max_left(my_map, x + 1, y + 1), get_max_right(my_map, x + 1, y + 1)):
                visible_tree_counter += 1
    return visible_tree_counter

def scenic_score_up(my_map, x, y, tree):
    trees = 0
    for i in range(y - 1, -1, -1):
        trees += 1
        if my_map[i][x] >= tree:
            break
    return trees if trees > 0 else 1

def scenic_score_down(my_map, x, y, tree):
    trees = 0
    for i in range(y + 1, len(my_map)):
        trees += 1
        if my_map[i][x] >= tree:
            break
    return trees if trees > 0 else 1

def scenic_score_left(my_map, x, y, tree):
    trees = 0
    for i in range(x - 1, -1, -1):
        trees += 1
        if my_map[y][i] >= tree:
            break
    return trees if trees > 0 else 1

def scenic_score_right(my_map, x, y, tree):
    trees = 0
    for i in range(x + 1, len(my_map[y])):
        trees += 1
        if my_map[y][i] >= tree:
            break
    return trees if trees > 0 else 1

def solution_2(my_map):
    max_scenic_score = 0
    for y, row in enumerate(my_map):
        for x, tree in enumerate(row):
            act_scenic_score = scenic_score_up(my_map, x, y, tree) * scenic_score_down(my_map, x, y, tree) * scenic_score_left(my_map, x, y, tree) * scenic_score_right(my_map, x, y, tree)
            if act_scenic_score > max_scenic_score:
                max_scenic_score = act_scenic_score
    return max_scenic_score
 
def main():
    test_map = get_map('2022/Day_8/test.txt')
    print('test 1:', solution_1(test_map))
    task_map = get_map('2022/Day_8/task.txt')
    print('Solution 1:', solution_1(task_map))
    print('test 2:', solution_2(test_map))
    print('Solution 2:', solution_2(task_map))
    

if __name__ == '__main__':
    main()
    