'''
Advent of Code 
2022 day 8
my solution to tasks from day 8

solution 1 - 
solution 2 - 

'''

def get_directions(filename):
    head_directions = []
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line.strip().split()
            head_directions.append((line[0], int(line[1])))
    return head_directions

get_new_head_pos = {
                    'L': lambda pos: (pos[0], pos[1] - 1),
                    'R': lambda pos: (pos[0], pos[1] + 1),
                    'U': lambda pos: (pos[0] + 1, pos[1]),
                    'D': lambda pos: (pos[0] - 1, pos[1])
                   }

get_distance = lambda pos_head, pos_tail: (abs(pos_head[0] - pos_tail[0]), abs(pos_head[1] - pos_tail[1]))

def get_new_tail_pos(head_pos, tail_pos):
    distance = get_distance(head_pos, tail_pos)
    if set(distance) == set([2, 0]):
        tail_pos = ((head_pos[0] + tail_pos[0]) // 2, (head_pos[1] + tail_pos[1]) // 2)
    elif distance == (2, 1):
        tail_pos = ((head_pos[0] + tail_pos[0]) // 2, head_pos[1])
    elif distance == (1, 2):
        tail_pos = (head_pos[0], (head_pos[1] + tail_pos[1]) // 2)
    return tail_pos

def solution_1(my_dirs):
    head_pos, tail_pos, set_of_visited_pos = (0, 0), (0, 0), set()
    set_of_visited_pos.add(tail_pos)
    for dir, num in my_dirs:
        for _ in range(num):
            head_pos = get_new_head_pos[dir](head_pos)
            tail_pos = get_new_tail_pos(head_pos, tail_pos)
            set_of_visited_pos.add(tail_pos)
    return len(set_of_visited_pos)


 
def main():
    test_dirs = get_directions('2022/Day_9/test.txt')
    print('test 1:', solution_1(test_dirs))
    task_dirs = get_directions('2022/Day_9/task.txt')
    print('Solution 1:', solution_1(task_dirs))
    

if __name__ == '__main__':
    main()
    