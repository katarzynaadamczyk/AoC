# Katarzyna Adamczyk
# Solution to day 25 task 1 of Advent of Code 2021


from copy import deepcopy

def print_data(data):
    print()
    for line in data:
        print(''.join(line))
    print()

def moveleft(data):
    moves = 0
    newdata = deepcopy(data)
    for y in range(len(data)):
        for x in range(len(data[y]) - 1):
            if data[y][x + 1] == '.' and data[y][x] == '>':
                newdata[y][x + 1], newdata[y][x] = data[y][x], data[y][x + 1]
                moves += 1
        if data[y][-1] == '>' and data[y][0] == '.':
            newdata[y][0], newdata[y][-1] = data[y][-1], data[y][0]
            moves += 1
    return newdata, moves

def movedown(data):
    moves = 0
    newdata = deepcopy(data)
    for x in range(len(data[0])):
        for y in range(len(data) - 1):
            if data[y][x] == 'v' and data[y + 1][x] == '.':
                newdata[y + 1][x], newdata[y][x] = data[y][x], data[y + 1][x]
                moves += 1
        if data[-1][x] == 'v' and data[0][x] == '.':
            newdata[0][x], newdata[-1][x] = data[-1][x], data[0][x]
            moves += 1
    return newdata, moves

def findfirststepwithnomoves(data):
    stepcount = 0
    while True:
        stepcount += 1
        data, moves = moveleft(data)
        data, newmoves = movedown(data)
        if moves + newmoves == 0:
            break
    print_data(data)
    return stepcount

def solution1(filename):
    with open(filename, 'r') as myfile:
        data = []
        for line in myfile:
            tmp = []
            for char in line.strip():
                tmp.append(char)
            data.append(tmp)
        
        
        return findfirststepwithnomoves(data)




def main():
    print(f'Result for test data for task 1 is {solution1("Day_25/testdata.txt")}')
    print(f'Result for data 25 for task 1 is {solution1("Day_25/data25.txt")}')
    

if __name__ == '__main__':
    main()