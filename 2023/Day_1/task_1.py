'''
Advent of Code 
2023 day 1
my solution to task 1 

solution 1 - 
solution 2 - 

'''
import re

def solution_1(filename):
    data = []
    with open(filename, 'r') as myfile:
        for line in myfile:
            tmp = re.findall('\d', line)
            data.append(int(tmp[0] + tmp[-1]))   
    return sum(data)

def main():
    print('test 1:', solution_1('2023/Day_1/test.txt'))
    print('Solution 1:', solution_1('2023/Day_1/task_1.txt'))
    
   # print('test 2:', solution_2('2022/Day_1/test_1.txt'))
   # print('Solution 2:', solution_2('2022/Day_1/task_1.txt'))

if __name__ == '__main__':
    main()