# Katarzyna Adamczyk
# Solution to day 22 task 1 of Advent of Code 2021

from itertools import product

def lightenordarken(data, cubesset):
 
    for x in range(data[0], data[1] + 1):
        for y in range(data[2], data[3] + 1):
            for z in range(data[4], data[5] + 1):
                cubesset.add((x, y, z))
    
    return cubesset

def solution1(filename):
    with open(filename, 'r') as myfile:
        
        setcubeson = set()
        setcubesoff = set()
        for line in myfile:    
            type = line[0:line.find(' ')]
            line = line[line.find(' ')::].strip()
            data = []
            for somerange in line.split(','):
                data.append(int(somerange[somerange.find('=')+1:somerange.find('.')]))
                data.append(int(somerange[somerange.rfind('.')+1::]))
            if data[0] >= -50 and data[0] <= 50:    
                if type == 'on':
                    setcubeson = lightenordarken(data, setcubeson)
                else:
                    setcubesoff = lightenordarken(data, setcubesoff)
                    setcubeson = setcubeson.difference(setcubesoff) 
                    setcubesoff = set()
            else:
                break   
        
        return len(setcubeson)


def solution2(filename):
    with open(filename, 'r') as myfile:
        
        setcubeson = set()
        setcubesoff = set()
        for line in myfile: 
            if len(line) > 3:   
                type = line[0:line.find(' ')]
                line = line[line.find(' ')::].strip()
                data = []
                print(line.split(','))
                for somerange in line.split(','):
                    data.append(int(somerange[somerange.find('=')+1:somerange.find('.')]))
                    data.append(int(somerange[somerange.rfind('.')+1::]))
                if type == 'on':
                    setcubeson = lightenordarken(data, setcubeson)
                else:
                    setcubesoff = lightenordarken(data, setcubesoff)
                    setcubeson = setcubeson.difference(setcubesoff) 
                    setcubesoff = set()
        
        return len(setcubeson)

def main():
    print(f'Result for test data for task 1 is {solution1("Day_22/testdata.txt")}')
    print(f'Result for data 22 for task 1 is {solution1("Day_22/data22.txt")}')
    
    print(f'Result for test data for task 2 is {solution2("Day_22/testdata.txt")}')
    print(f'Result for data 20 for task 2 is {solution2("Day_22/data22.txt")}')
    

if __name__ == '__main__':
    main()