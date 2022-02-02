# Katarzyna Adamczyk
# Solution to day 15 task 2 of Advent of Code 2021

# check on L - offset down, offset left, offset right, offset up
def checkonl(data, result, x, y):
    # moze w ogole zrobic na numpy
    # i robic tutaj wycinek 20x20, ktory powiekszac o kolejne linie
    # naucze sie w ten sposob numpy i moze zrobie zadanie
    if x < len(data[y]) - 1:
        tmp = []
        for i in range(max(0, y - 20), y):
            act = result[i][x] + data[i][x+1]
            for j in range(i + 1, y+1):
                act += data[j][x+1]
            tmp.append(act)
        if x < len(data[y]) - 2:
            for i in range(max(0, y - 20), y):
                act = result[i][x] + data[i][x+1] + data[i][x+2]
                for j in range(i + 1, min(y+1, len(data))):
                    act += data[j][x+2]
                act += data[min(y, len(data) - 1)][x+1]
            tmp.append(act)
        return (min(tmp)) if len(tmp) > 0 else -1 
    else:
        return -1  

def findpath(data): # searching for the path only down and right and omitting the large values to the right or to the left
    result = []
    tmp = [0]
    for x in range(1, len(data[0])):
        actx = checkonl(data, tmp, x, 0)
        if actx > 0:
            tmp.append(min(tmp[x-1], actx) + data[0][x])
        else:
            tmp.append(tmp[x-1] + data[0][x])
    result.append(tmp)
    for y in range(1, len(data)):
        #print(f'y = {y} out of {len(data)-1}')
        acty = checkonl(data, result, 0, y)
        if acty > 0:
            tmp = [min(result[y-1][0], acty) + data[y][0]]
        else:
            tmp = [data[y][0] + result[y-1][0]]
        for x in range(1, len(data[y])):
            acty = checkonl(data, result, x, y)
            
            if acty > 0:
                tmp.append(min(tmp[x-1], result[y-1][x], acty) + data[y][x])
            else:
                tmp.append(min(tmp[x-1], result[y-1][x]) + data[y][x])
        result.append(tmp)
    return result[-1][-1]


def preparemap(data, num):
    # make data table [5 x len(data)][len(data[0])]
    xlen = len(data[0])
    ylen = len(data)
    for i in range(ylen, num * ylen):
        tmp = []
        for x in range(len(data[0])):
            tmp.append((data[i - ylen][x] + (2 if data[i - ylen][x] == 9 else 1)) % 10)
        data.append(tmp)
    # make data table [5 x len(data)][5 x len(data[0])]
    for y in range(num * ylen):
        for x in range(xlen, num * xlen):
            data[y].append((data[y][x - xlen] + (2 if data[y][x - xlen] == 9 else 1)) % 10)
    return data

def solution1(filename):
    with open(filename, 'r') as myfile:
        data = [] 
        for line in myfile:
            tmp = [int(x) for x in line.strip()]
            data.append(tmp)
            
        return findpath(data)


def solution2(filename):
    with open(filename, 'r') as myfile:
        data = [] 
        for line in myfile:
            tmp = [int(x) for x in line.strip()]
            data.append(tmp)
        data = preparemap(data, 5)
        return findpath(data)

def main():
    print(f'Result for test data for task 1 is {solution1("Day_15/testdata.txt")} (should be 40)')
    print(f'Result for data 15 for task 1 is {solution1("Day_15/data15.txt")} (should be 487)')
    print(f'Result for test data for task 2 is {solution2("Day_15/testdata.txt")} (should be 315)')
    print(f'Result for data 15 for task 2 is {solution2("Day_15/data15.txt")} (should be 2821)')
    
if __name__ == '__main__':
    main()