'''
Advent of Code 
2022 day 1
my solution to task 1 

solution 1 - make a list of sum of calories for each elf. Find its maximum.
solution 2 - make a list of sum of calories for each elf. Sort the list in descending order and get the sum of first three elements.

'''

def solution_1(filename):
    data = []
    with open(filename, 'r') as myfile:
        tmp = []
        for line in myfile:
            line = line.strip()
            if len(line) > 0:
                tmp.append(int(line))
            else:
                data.append(tmp)
                tmp = []    
    return max([sum(x) for x in data])

def solution_2(filename):
    data = []
    with open(filename, 'r') as myfile:
        tmp = []
        for line in myfile:
            line = line.strip()
            if len(line) > 0:
                tmp.append(int(line))
            else:
                data.append(tmp)
                tmp = []    
    sorted_elves = sorted([sum(x) for x in data], reverse=True)
    print(sorted_elves)
    return sum(sorted_elves[0:3])
    
def main():
    print('test 1:', solution_1('2022/Day_1/test_1.txt'))
    print('Solution 1:', solution_1('2022/Day_1/task_1.txt'))
    
    print('test 2:', solution_2('2022/Day_1/test_1.txt'))
    print('Solution 2:', solution_2('2022/Day_1/task_1.txt'))

if __name__ == '__main__':
    main()

