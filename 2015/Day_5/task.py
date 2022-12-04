'''
Advent of Code 
2015 day 3
my solution to tasks from day 3

solution 1 - 
solution 2 - 

'''
import re

def solution_1(filename):
    nice_count = 0
    doubled_str = [x * 2 for x in 'abcdefghijklmnopqrstuvwxyz']
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line.strip()
            vowel_count = 0
            for vowel in 'aeiou':
                vowel_count += line.count(vowel)
            if vowel_count < 3:
                continue
            check = False
            for wrong_str in ['ab', 'cd', 'pq', 'xy']:
                if wrong_str in line:
                    check = True
                    break
            if check:
                continue
            for doubled in doubled_str:
                if doubled in line:
                    check = True
                    break
            if check:
                nice_count += 1
            
                
    return nice_count


def main():
    print(f'Result for data for test 1 is {solution_1("2015/Day_5/test.txt")}')
    print(f'Result for data for task 1 is {solution_1("2015/Day_5/data.txt")}')
    
    
    
if __name__ == '__main__':
    main()