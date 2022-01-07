# Katarzyna Adamczyk
# Solution to day 22 task 1 of Advent of Code 2021

from itertools import product

# not finished 
# I want to check if the next cube is in the previous ones and in such a way add them to result

def checkifincube(data, cube):
    if ((data[0] >= cube[0] and data[1] <= cube[1]) and (data[2] >= cube[2] and data[3] <= cube[3]) and (data[4] >= cube[4] and data[5] <= cube[5])):
        return True
    return False


def countlightson(data, cubeson, cubesoff):
    cubes = ((data[1] + 1 - data[0]) * (data[3] + 1 - data[2]) * (data[5] + 1 - data[4]))
    cubeson.append(data)
    return cubes

def countlightsoff(data, cubeson, cubesoff):
    cubes = ((data[1] + 1 - data[0]) * (data[3] + 1 - data[2]) * (data[5] + 1 - data[4]))
    cubesoff.append(data)
    return cubes
    


def solution1(filename):
    with open(filename, 'r') as myfile:
        
        cubeson = []
        cubesoff = []
        actresult = 0
        for line in myfile:    
            type = line[0:line.find(' ')]
            line = line[line.find(' ')::].strip()
            data = []
            for somerange in line.split(','):
                data.append(int(somerange[somerange.find('=')+1:somerange.find('.')]))
                data.append(int(somerange[somerange.rfind('.')+1::]))
            if data[0] >= -50 and data[0] <= 50:    
                if type == 'on':
                    actresult += countlightson(data, cubeson, cubesoff)
                else:
                    actresult -= countlightsoff(data, cubeson, cubesoff)
            else:
                break   
            
        return actresult


def solution2(filename):
    with open(filename, 'r') as myfile:
        
        cubeson = []
        cubesoff = []
        actresult = 0
        for line in myfile:    
            type = line[0:line.find(' ')]
            line = line[line.find(' ')::].strip()
            data = []
            for somerange in line.split(','):
                data.append(int(somerange[somerange.find('=')+1:somerange.find('.')]))
                data.append(int(somerange[somerange.rfind('.')+1::]))  
            if type == 'on':
                actresult += countlightson(data, cubeson, cubesoff)
            else:
                actresult -= countlightsoff(data, cubeson, cubesoff) 
        
        return actresult
        

def main():
    print(f'Result for test data for task 1 is {solution1("Day_22/testdata.txt")}')
    print(f'Result for data 22 for task 1 is {solution1("Day_22/data22.txt")}')
    
    print(f'Result for test data for task 2 is {solution2("Day_22/testdata.txt")}')
    print(f'Result for test data for task 2 is {solution2("Day_22/testdata2.txt")}')
    print(f'Result for data 20 for task 2 is {solution2("Day_22/data22.txt")}')

if __name__ == '__main__':
    main()