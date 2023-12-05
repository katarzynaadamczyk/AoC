'''
Advent of Code 
2023 day 5
my solution to task 1 & 2

solution 1 - 
solution 2 - 

'''

from sys import maxsize

def get_seeds(line):
    line = line[line.find(':') + 1:].strip().split()
    seeds = []
    for seed in line:
        seeds.append(int(seed))
    return seeds

def get_ranges(line): 
    line = line.split()
    nums = [int(x) for x in line]
    return nums

def get_data(filename):
    with open(filename, 'r') as myfile:
        line = myfile.readline()
        seeds = get_seeds(line)
        myfile.readline()
        line = myfile.readline()
        transitions = []
        while line:
            new_list = []
            line = myfile.readline()
            while line and line != '\n':
                new_list.append(get_ranges(line)) 
                line = myfile.readline()    
            transitions.append(new_list)
            line = myfile.readline()
      

    return seeds, transitions

def transform_seed(seed, ranges):
    for seed_1, seed_2, val in ranges:
        if seed_2 <= seed < seed_2 + val:
            return seed_1 + seed - seed_2
    return seed

def solution_1(filename):
    seeds, transitions = get_data(filename)
    locations = []
    for seed in seeds:
        transformed_seed = seed
        for ranges in transitions:
            transformed_seed = transform_seed(transformed_seed, ranges)
        locations.append(transformed_seed)
    return min(locations)

def solution_2(filename):
    seeds, transitions = get_data(filename)
    print(len(seeds) // 2)
    act_min_location = maxsize
    for seed, val in zip(seeds[::2], seeds[1::2]):
        print(seed, val)
        for new_seed in range(seed, seed + val):
            transformed_seed = new_seed
            for ranges in transitions:
                transformed_seed = transform_seed(transformed_seed, ranges)
            if act_min_location > transformed_seed:
                act_min_location = transformed_seed
    return act_min_location

def main():
    print('test 1:', solution_1('2023/Day_5/test.txt'))
    print('Solution 1:', solution_1('2023/Day_5/task.txt'))
    
    print('test 2:', solution_2('2023/Day_5/test.txt'))
    print('Solution 2:', solution_2('2023/Day_5/task.txt'))

if __name__ == '__main__':
    main()
