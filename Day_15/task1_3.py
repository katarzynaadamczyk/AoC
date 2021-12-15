# Katarzyna Adamczyk
# Solution to day 15 task 1 of Advent of Code 2021

def findpath(data): # searching for the path only down and right for now looking for solution to search also up and left
    result = []
    tmp = [0]
    for x in range(1, len(data[0])):
        if x > 2:
            tmp.append(min(tmp[x-1], tmp[x-2] + data[1][x-2] + data[1][x-1] + data[1][x]) + data[0][x])
        else:
            tmp.append(tmp[x-1] + data[0][x])
    result.append(tmp)
    for y in range(1, len(data)):
        if y > 2:
            tmp = [min(result[y-1][0], result[y-2][0] + data[y-2][1] + data[y-1][1] + data[y][1]) + data[y][0]]
        else:
            tmp = [data[y][0] + result[y-1][0]]
        for x in range(1, len(data[y])):
            if x > 2 and y > 2 and (x < len(data[y]) - 1) and (y < len(data) - 1):
                tmp.append(min(tmp[x-1], result[y-1][x], tmp[x-2] + data[y+1][x-2] + data[y+1][x-1] + data[y+1][x], result[y-2][x] + data[y-2][x+1] + data[y-1][x+1] + data[y][x+1]) + data[y][x])
            elif x > 2 and y < len(data) - 1:
                tmp.append(min(tmp[x-1], result[y-1][x], tmp[x-2] + data[y+1][x-2] + data[y+1][x-1] + data[y+1][x]) + data[y][x])
            elif y > 2 and x < len(data) - 1:
                tmp.append(min(tmp[x-1], result[y-1][x], result[y-2][x] + data[y-2][x+1] + data[y-1][x+1] + data[y][x+1]) + data[y][x])
            else:
                tmp.append(min(tmp[x-1], result[y-1][x]) + data[y][x])
        result.append(tmp)
    return result

def solution(filename):
    with open(filename, 'r') as myfile:
        data = [] 
        for line in myfile:
            tmp = [int(x) for x in line.strip()]
            data.append(tmp)
        result = findpath(data) # search for 4 x 9 or 5 x 9 and it will be completed I suppose
        return result[-1][-1]

def main():
    print(f'Result for test data for task 1 is {solution("Day_15/testdata.txt")}')
    print(f'Result for data 15 for task 1 is {solution("Day_15/data15.txt")}')

if __name__ == '__main__':
    main()