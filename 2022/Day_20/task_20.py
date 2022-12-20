'''
Advent of Code 
2022 day 20
my solution to tasks from day 20


solution 1 - 
solution 2 - 

'''


def get_file(filename):
    file = []
    with open(filename, 'r') as myfile:
        for line in myfile:
            file.append((int(line.strip()), False))
    return file


def get_first_non_moved_element_index(file):
    for index, item in enumerate(file): #[previous_index:]):
        if item[1] == False:
            return index #+ previous_index
    return -1

def get_new_index(act_index, add, file_len):
    new_index = (act_index + add % file_len) % file_len
 #   if new_index > file_len:
   #     new_index = add - (file_len - act_index)
    return new_index

def get_coordinate_index(zero_index, x, file_len):
    return (zero_index + x) % file_len

def solution_1(file):
    index, file_len = 0, len(file)
    while 0 <= index < file_len:
        tmp = (file[index][0], True)
        new_index = get_new_index(index, file[index][0], file_len - 1)
        file.pop(index)
        #if new_index == 0:
        #    file.append(tmp)
        #else:
        file.insert(new_index, tmp)
        index = get_first_non_moved_element_index(file)
    file = [item[0] for item in file]
    grove_coordinates_indexes = [get_coordinate_index(file.index(0), x, file_len) for x in [1000, 2000, 3000]]
    print(grove_coordinates_indexes)
    print([file[index] for index in grove_coordinates_indexes])
    return sum([file[index] for index in grove_coordinates_indexes])

  
def main():
    test_file = get_file('2022/Day_20/test.txt')
    print('test 1:', solution_1(test_file))
    task_file = get_file('2022/Day_20/task.txt')
    print('Solution 1:', solution_1(task_file))
  #  print('test 2:', solution_2(test_valves, test_start_valve, 26))
   # print('Solution 2:', solution_2(task_valves, task_start_valve, 26))
    
    
if __name__ == '__main__':
    main()
    