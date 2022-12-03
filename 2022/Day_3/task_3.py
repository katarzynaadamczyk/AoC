'''
Advent of Code 
2022 day 3
my solution to tasks from day 3

solution 1 - divide each rucksack in two comparments. Find intersection of set of chars in each compartment and sum all intersections priorities.
solution 2 - get a list of set of chars for each three elves. Find intersection and sum its priorities.

'''

def solution_1(filename):
    act_sum = 0
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line.strip()
            c1, c2 = line[0:len(line)//2], line[len(line)//2:]
            inter = set([char for char in c1]).intersection(set([char for char in c2]))
            for char in inter:
                if char.islower():
                    act_sum += (ord(char) - ord('a') + 1)
                else:
                    act_sum += (ord(char) - ord('A') + 27)
    return act_sum

def solution_2(filename):
    act_sum = 0
    with open(filename, 'r') as myfile:
        tmp = []
        for line in myfile:
            tmp.append(set([char for char in line.strip()]))
            if len(tmp) == 3:
                inter = tmp[0].intersection(tmp[1], tmp[2])
                for char in inter:
                    if char.islower():
                        act_sum += (ord(char) - ord('a') + 1)
                    else:
                        act_sum += (ord(char) - ord('A') + 27)
                tmp = []
    return act_sum

    
def main():
    print('test 1:', solution_1('2022/Day_3/test_3.txt'))
    print('Solution 1:', solution_1('2022/Day_3/task_3.txt'))
    
    print('test 2:', solution_2('2022/Day_3/test_3.txt'))
    print('Solution 2:', solution_2('2022/Day_3/task_3.txt'))

if __name__ == '__main__':
    main()