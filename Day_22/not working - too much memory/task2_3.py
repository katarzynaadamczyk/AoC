# Katarzyna Adamczyk
# Solution to day 22 task 1 of Advent of Code 2021

import numpy as np

def findminandmax(cubes):
    minval = cubes[0][1][0]
    maxval = minval
    
    for cube in cubes:
        for val in cube[1]:
            if val < minval:
                minval = val
            if val > maxval:
                maxval = val
    
    return minval, maxval
    

def countlights(cubes):
    minval, maxval = findminandmax(cubes)
    somerange = maxval - minval + 1
    print(somerange)
    reactor = np.zeros((somerange, somerange, somerange), dtype=bool)
    
    for cube in cubes:
        for x in range(cube[1][0], cube[1][1] + 1):
            for y in range(cube[1][2], cube[1][3] + 1):
                for z in range(cube[1][4], cube[1][5] + 1):
                    reactor[x - minval][y - minval][z - minval] = cube[0]
                    
    return sum(sum(sum(reactor)))
    


def solution1(filename):
    with open(filename, 'r') as myfile:
        
        cubes = []
        for line in myfile:    
            type = line[0:line.find(' ')]
            line = line[line.find(' ')::].strip()
            data = []
            for somerange in line.split(','):
                data.append(int(somerange[somerange.find('=')+1:somerange.find('.')]))
                data.append(int(somerange[somerange.rfind('.')+1::]))
            if data[0] >= -50 and data[0] <= 50:    
                cubes.append([1 if type == 'on' else 0, data])
            else:
                break   
        print(cubes[0][1][0])
        
        return countlights(cubes)


def solution2(filename):
    with open(filename, 'r') as myfile:
        
        cubes = []
        for line in myfile:    
            type = line[0:line.find(' ')]
            line = line[line.find(' ')::].strip()
            data = []
            for somerange in line.split(','):
                data.append(int(somerange[somerange.find('=')+1:somerange.find('.')]))
                data.append(int(somerange[somerange.rfind('.')+1::]))  
            cubes.append([1 if type == 'on' else 0, data])
            
        
        return countlights(cubes)
        

def main():
    print(f'Result for test data for task 1 is {solution1("Day_22/testdata.txt")}')
    print(f'Result for data 22 for task 1 is {solution1("Day_22/data22.txt")}')
    
    print(f'Result for test data for task 2 is {solution2("Day_22/testdata.txt")}')
    print(f'Result for test data for task 2 is {solution2("Day_22/testdata2.txt")}')
    print(f'Result for data 20 for task 2 is {solution2("Day_22/data22.txt")}')

if __name__ == '__main__':
    main()