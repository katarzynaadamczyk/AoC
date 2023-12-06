'''
Advent of Code 
2023 day 5
my solution to task 1 & 2

solution 1 - check for each seed if it is within the range, if so do the transition. List of seeds transforms to soils, then to fertilizers, and so on.
At the end we get a list of locations and we need to pick the lowest value.
solution 2 - check for each seed range how it is located versus soil ranges, then versus fertilizer ranges and so on, keep the ranges and transform only them.
Then pick the lowest starting range value from the list - it is the lowest location. Rememeber to sort the ranges before each transformation! :) 

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
    for seed_last, seed_first, val in ranges:
        if seed_first <= seed < seed_first + val:
            return seed_last + seed - seed_first
    return seed

def transform_range(min_seed, val, ranges):
    new_seeds = []
    ranges = sorted(ranges, key=lambda x: x[1])
    for seed_last, seed_first, val_range in ranges:
        if seed_first <= min_seed < seed_first + val_range:
            if seed_first <= min_seed + val < seed_first + val_range:
                new_seeds.append((seed_last + min_seed - seed_first, val))
                val = 0
                break
            else:
                new_seeds.append((seed_last + min_seed - seed_first, val_range - (min_seed - seed_first)))
                val = val - (val_range - (min_seed - seed_first))
                min_seed = seed_first + val_range
                    
        elif seed_first <= min_seed + val < seed_first + val_range:
            new_seeds.append((seed_last, val - (seed_first - min_seed)))
            val = seed_first - min_seed
    
    if val > 0:
        new_seeds.append((min_seed, val))
    return new_seeds

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
    result_min_location = maxsize
    for seed, val in zip(seeds[::2], seeds[1::2]):
        seed_ranges = [(seed, val)]
        for ranges in transitions:
            new_seed_ranges = []
            for min_seed, new_val in seed_ranges:
                new_seed_ranges += transform_range(min_seed, new_val, ranges)
            seed_ranges = new_seed_ranges
        act_min_location = min([x[0] for x in seed_ranges] + [x[0] + x[1] - 1 for x in seed_ranges])
        if act_min_location < result_min_location:
            result_min_location = act_min_location
    return result_min_location

def main():
    print('test 1:', solution_1('2023/Day_5/test.txt'))
    print('Solution 1:', solution_1('2023/Day_5/task.txt'))
    
    print('test 2:', solution_2('2023/Day_5/test.txt'))
    print('Solution 2:', solution_2('2023/Day_5/task.txt'))

if __name__ == '__main__':
    main()
