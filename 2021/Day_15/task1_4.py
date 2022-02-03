# Katarzyna Adamczyk
# Solution to day 15 task 1 of Advent of Code 2021


def checkonx(data, result, x, y):
    if y < len(data) - 1:
        tmp = []
        for i in range(max(0, x - 8), min(x, len(data[y]))):
            act = result[i] + data[y+1][i]
            for j in range(i + 1, min(x+1, len(data[y]))):
                act += data[y+1][j]
            tmp.append(act)
        return (min(tmp)) if len(tmp) > 0 else -1 
    else:
        return -1    

def checkony(data, result, x, y):
    if x < len(data[y]) - 1:
        tmp = []
        for i in range(max(0, y - 8), y):
            act = result[i][x] + data[i][x+1]
            for j in range(i + 1, y+1):
                act += data[j][x+1]
            tmp.append(act)
        return (min(tmp)) if len(tmp) > 0 else -1 
    else:
        return -1  

def findpath(data): # searching for the path only down and right and omitting the large values to the right or to the left
    result = []
    tmp = [0]
    for x in range(1, len(data[0])):
        actx = checkonx(data, tmp, x, 0)
        if actx > 0:
            tmp.append(min(tmp[x-1], actx) + data[0][x])
        else:
            tmp.append(tmp[x-1] + data[0][x])
    result.append(tmp)
    for y in range(1, len(data)):
        acty = checkony(data, result, 0, y)
        if acty > 0:
            tmp = [min(result[y-1][0], acty) + data[y][0]]
        else:
            tmp = [data[y][0] + result[y-1][0]]
        for x in range(1, len(data[y])):
            acty = checkony(data, result, x, y)
            actx = checkonx(data, tmp, x, y)
            
            if actx > 0 and acty > 0:
                tmp.append(min(tmp[x-1], result[y-1][x], actx, acty) + data[y][x])
            elif actx > 0:
                tmp.append(min(tmp[x-1], result[y-1][x], actx) + data[y][x])
            elif acty > 0:
                tmp.append(min(tmp[x-1], result[y-1][x], acty) + data[y][x])
            else:
                tmp.append(min(tmp[x-1], result[y-1][x]) + data[y][x])
        result.append(tmp)
  #  print(result)
    return result[-1][-1]

def solution(filename):
    with open(filename, 'r') as myfile:
        data = [] 
        for line in myfile:
            tmp = [int(x) for x in line.strip()]
            data.append(tmp)
            
        return findpath(data)

def main():
    print(f'Result for test data for task 1 is {solution("Day_15/testdata.txt")}')
    print(f'Result for data 15 for task 1 is {solution("Day_15/data15.txt")}')

if __name__ == '__main__':
    main()