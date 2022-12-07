'''
Advent of Code 
2015 day 3
my solution to tasks from day 3

solution 1 - check each word for rules named in task (if count of vowels is >= 3, if none of ['ab', 'cd', 'pq', 'xy'] is in word and if word contains any doubled letter). 
If so, add to actual count of nice words.
solution 2 - check each word for rules named in task (functions check_rule_1 and check_rule_2). If they say True that increase counter of nice words by 1.

'''

import numpy as np

def turn_lights(lights, min_vals, max_vals, set_):
    for x in range(min_vals[0], max_vals[0] + 1):
        for y in range(min_vals[1], max_vals[1] + 1):
            lights[x][y] = set_
    return lights

def toggle_lights(lights, min_vals, max_vals):
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
                lights = toggle_lights(lights, line[1], line[3])
            elif line[0] == 'turn_on':
                lights = turn_lights(lights, line[1], line[3], True)
            elif line[0] == 'turn_off':
                lights = turn_lights(lights, line[1], line[3], False)
                
    return sum([sum(x) for x in lights])


def main():
    print(f'Result for data for task 1 is {solution_1("2015/Day_6/data.txt")}')
    
    
    
if __name__ == '__main__':
    main()