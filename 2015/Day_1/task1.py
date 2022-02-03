# Katarzyna Adamczyk
# Solution to day 25 task 1 of Advent of Code 2015

from math import floor


def getdata(filename):
    with open(filename, 'r') as myfile:
        return myfile.readline().strip()

def countfloors(data):
    floor = 0
    for char in data:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
    return floor

def solution1(filename):
    data = getdata(filename)
        
    return countfloors(data)
    
def main():
    print(f'Result for test data for task 1 is {solution1("2015/Day_1/testdata.txt")}')
    print(f'Result for data 25 for task 1 is {solution1("2015/Day_1/data1.txt")}')
    

if __name__ == '__main__':
    main()