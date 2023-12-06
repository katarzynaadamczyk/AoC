'''
Advent of Code 
2023 day 6
my solution to task 1 & 2

solution 1 - search for min number of ms of holding the button that gives distance greater than actual record for each of races, 
then search backwards to get max number of ms, then append their difference + 1 to list, at the end return result of multiplication of the list
solution 2 - as above just for one record
'''

from re import findall
from functools import reduce

def get_nums(line):
    return [int(x) for x in findall(r'\d+', line)]

def get_data(filename):
    with open(filename, 'r') as myfile:
        times = myfile.readline()
        distances = myfile.readline()
    return get_nums(times), get_nums(distances)

def get_nums_2(line):
    return int(reduce(lambda x, y: x + y, findall(r'\d+', line)))

def get_data_2(filename):
    with open(filename, 'r') as myfile:
        times = myfile.readline()
        distances = myfile.readline()
    return get_nums_2(times), get_nums_2(distances)

def get_no_of_possible_ways(time, distance):
    min_i, max_i = 0, time
    while (time - min_i) * min_i <= distance:
        min_i += 1
    while (time - max_i) * max_i <= distance:
        max_i -= 1
    return max_i - min_i + 1

def solution_1(filename):
    times, distances = get_data(filename)
    no_of_ways = []
    for time, distance in zip(times, distances):
        no_of_ways.append(get_no_of_possible_ways(time, distance))
    return reduce(lambda x, y: x * y, no_of_ways)

def solution_2(filename):
    time, distance = get_data_2(filename)
    return get_no_of_possible_ways(time, distance)

def main():
    print('test 1:', solution_1('2023/Day_6/test.txt'))
    print('Solution 1:', solution_1('2023/Day_6/task.txt'))
    
    print('test 2:', solution_2('2023/Day_6/test.txt'))
    print('Solution 2:', solution_2('2023/Day_6/task.txt'))

if __name__ == '__main__':
    main()
