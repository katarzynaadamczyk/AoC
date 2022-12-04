'''
Advent of Code 
2022 day 4
my solution to tasks from day 4

solution 1 - 
solution 2 - 

'''

def solution_1(filename):
    overlap_count = 0
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line.strip()
            x = lambda elf: [int(elem) for elem in elf.split('-')]
            elf_1, elf_2 = [x(elf) for elf in line.split(',')]
            if (elf_1[0] <= elf_2[0] and elf_1[1] >= elf_2[1]) or (elf_1[0] >= elf_2[0] and elf_1[1] <= elf_2[1]):
                overlap_count += 1 
    return overlap_count

def solution_2(filename):
    overlap_count = 0
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line.strip()
            x = lambda elf: [int(elem) for elem in elf.split('-')]
            elf_1, elf_2 = [x(elf) for elf in line.split(',')]
            if elf_2[0] <= elf_1[0] <= elf_2[1] or elf_2[0] <= elf_1[1] <= elf_2[1] or elf_1[0] <= elf_2[0] <= elf_1[1] or elf_1[0] <= elf_2[1] <= elf_1[1]:
                overlap_count += 1 
    return overlap_count

    
def main():
    print('test 1:', solution_1('2022/Day_4/test_4.txt'))
    print('Solution 1:', solution_1('2022/Day_4/task_4.txt'))
    
    print('test 2:', solution_2('2022/Day_4/test_4.txt'))
    print('Solution 2:', solution_2('2022/Day_4/task_4.txt'))
    

if __name__ == '__main__':
    main()