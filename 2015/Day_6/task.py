'''
Advent of Code 
2015 day 3
my solution to tasks from day 3

solution 1 - follow the instructions and keep turning on and off given lights. The clue is to correctly parse the input data. And to use numpy array.
solution 2 - as above only the instructions say to increase / decrease lights and not to fall below 0.

'''

import numpy as np

def turn_lights_1(lights, min_vals, max_vals, set_):
    for x in range(min_vals[0], max_vals[0] + 1):
        for y in range(min_vals[1], max_vals[1] + 1):
            lights[x][y] = set_
    return lights

def toggle_lights_1(lights, min_vals, max_vals):
    for x in range(min_vals[0], max_vals[0] + 1):
        for y in range(min_vals[1], max_vals[1] + 1):
            lights[x][y] = not lights[x][y]
    return lights

def solution_1(filename):
    lights = np.zeros((1000, 1000), bool)
    get_nums = lambda vals: [int(x) for x in vals.split(',')]
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line.strip()
            line = line.replace('turn off', 'turn_off').replace('turn on', 'turn_on')
            line = line.split()
            line[1], line[3] = get_nums(line[1]), get_nums(line[3])
            if line[0] == 'toggle':
                lights = toggle_lights_1(lights, line[1], line[3])
            elif line[0] == 'turn_on':
                lights = turn_lights_1(lights, line[1], line[3], True)
            elif line[0] == 'turn_off':
                lights = turn_lights_1(lights, line[1], line[3], False)
                
    return sum([sum(x) for x in lights])


def turn_lights_2(lights, min_vals, max_vals, set_):
    for x in range(min_vals[0], max_vals[0] + 1):
        for y in range(min_vals[1], max_vals[1] + 1):
            lights[x][y] += set_
    return lights

def turn_off_lights_2(lights, min_vals, max_vals, set_):
    for x in range(min_vals[0], max_vals[0] + 1):
        for y in range(min_vals[1], max_vals[1] + 1):
            lights[x][y] += set_
            if lights[x][y] < 0:
                lights[x][y] = 0
    return lights

def solution_2(filename):
    lights = np.zeros((1000, 1000), int)
    get_nums = lambda vals: [int(x) for x in vals.split(',')]
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line.strip()
            line = line.replace('turn off', 'turn_off').replace('turn on', 'turn_on')
            line = line.split()
            line[1], line[3] = get_nums(line[1]), get_nums(line[3])
            if line[0] == 'toggle':
                lights = turn_lights_2(lights, line[1], line[3], 2)
            elif line[0] == 'turn_on':
                lights = turn_lights_2(lights, line[1], line[3], 1)
            elif line[0] == 'turn_off':
                lights = turn_off_lights_2(lights, line[1], line[3], -1)
                
    return sum([sum(x) for x in lights])

def main():
    print(f'Result for data for task 1 is {solution_1("2015/Day_6/data.txt")}')
    print(f'Result for data for task 2 is {solution_2("2015/Day_6/data.txt")}')
    
    
    
if __name__ == '__main__':
    main()