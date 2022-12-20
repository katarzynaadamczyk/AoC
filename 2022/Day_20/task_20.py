'''
Advent of Code 
2022 day 20
my solution to tasks from day 20


solution 1 - 
solution 2 - 

'''
from copy import copy

def get_file(filename):
    file, index = [], 0
    with open(filename, 'r') as myfile:
        for line in myfile:
            file.append((int(line.strip()), index))
            index += 1
    return file


def get_new_index(act_index, add, file_len):
    return (act_index + add) % file_len

def get_actual_position(file):
    for item in sorted(file, key=lambda item: item[1]):
        yield item

def rotate_file(file):
    index, file_len = 0, len(file)
    for item in get_actual_position(file):
        index = file.index(item)
        new_index = get_new_index(index, item[0], file_len - 1)
        file.pop(index)
        file.insert(new_index, item)
    return file


def solution_1(file):
    file = rotate_file(file)
    file = [item[0] for item in file]
    grove_coordinates_indexes = [get_new_index(file.index(0), x, len(file)) for x in [1000, 2000, 3000]]
    return sum([file[index] for index in grove_coordinates_indexes])

def solution_2(file, decryption_key, iterations):
    new_file = [(item[0] * decryption_key, item[1]) for item in file]
    for _ in range(iterations):
        new_file = rotate_file(new_file)
    new_file = [item[0] for item in new_file]
    zero_index = new_file.index(0)
    grove_coordinates_indexes = [get_new_index(zero_index, x, len(new_file)) for x in [1000, 2000, 3000]]
    print([new_file[index] for index in grove_coordinates_indexes])
    return sum([new_file[index] for index in grove_coordinates_indexes])


  
def main():
    test_file = get_file('2022/Day_20/test.txt')
    print('test 1:', solution_1(copy(test_file)))
    task_file = get_file('2022/Day_20/task.txt')
    print('Solution 1:', solution_1(task_file))
    test_file = get_file('2022/Day_20/test.txt')
    task_file = get_file('2022/Day_20/task.txt')
    print('test 2:', solution_2(copy(test_file), 811589153, 10))
    print('Solution 2:', solution_2(copy(task_file), 811589153, 10))
    
    
if __name__ == '__main__':
    main()
    