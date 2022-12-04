'''
Advent of Code 
2015 day 4
my solution to tasks from day 4

solution 1 & 2- iterate until you find the correct number. in each iteration get the actual md5 hash and check whether it starts with 5 or 6 zeros.

'''

import hashlib

def solution_1(input):
    i = 1
    while True:
        result = hashlib.md5((input + str(i)).encode())
        if result.hexdigest().startswith('00000'):
            return i
        i += 1

def solution_2(input):
    i = 1
    while True:
        result = hashlib.md5((input + str(i)).encode())
        if result.hexdigest().startswith('000000'):
            return i
        i += 1

def main():
    print(f'Result for test data for task 1 is {solution_1("abcdef")}')
    print(f'Result for data for task 1 is {solution_1("yzbqklnj")}')
    print(f'Result for data for task 2 is {solution_2("yzbqklnj")}')
    
    
if __name__ == '__main__':
    main()