# Katarzyna Adamczyk
# Solution to day 25 task 1&2 of Advent of Code 2015

from math import prod
from re import X


def getdata(filename):
    with open(filename, 'r') as myfile:
        data = []
        for line in myfile:
            data.append([int(x) for x in line.strip().split('x')])
        return data

def countpaper(data):
    result = 0
    for box in data:
        tmp = []
        for i in range(len(box) - 1):
            for j in range(i + 1, len(box)):
                tmp.append(box[i] * box[j])
        result += 2 * sum(tmp) + min(tmp)
    return result

def countribbon(data):
    return sum([2 * (sum(x) - max(x)) + prod(x) for x in data])

def solution1(filename):
    data = getdata(filename)
        
    return countpaper(data)

def solution2(filename):
    data = getdata(filename)
        
    return countribbon(data)
    
def main():
    print(f'Result for test data for task 1 is {solution1("2015/Day_2/testdata.txt")}')
    print(f'Result for data 25 for task 1 is {solution1("2015/Day_2/data2.txt")}')
    
    
    print(f'Result for test data for task 1 is {solution2("2015/Day_2/testdata.txt")}')
    print(f'Result for data 25 for task 1 is {solution2("2015/Day_2/data2.txt")}')
    

if __name__ == '__main__':
    main()