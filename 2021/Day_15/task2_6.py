# Katarzyna Adamczyk
# Solution to day 15 task 1&2 of Advent of Code 2021
# still working on

def findpath(data): # searching for the path only down and right for now looking for solution to search also up and left
    result = []
    tmp = [0]
    for x in range(1, len(data[0])):
        tmp.append(tmp[x-1] + data[0][x])
    result.append(tmp)
    for y in range(1, len(data)):
        tmp = [data[y][0] + result[y-1][0]]
        for x in range(1, len(data[y])):
            tmp.append(min(tmp[x-1], result[y-1][x]) + data[y][x])
        result.append(tmp)
    
   # print(result)
    y = 0
    ypom = None
   # for y in range(len(data)):
    while y < len(data):
        changesmade = 0
        if y <= 0:
            y = 0
            tmp = min(result[y+1][-1], result[y][-2]) + data[y][-1]
            if tmp < result[y][-1]:
                result[y][-1] = tmp
                changesmade += 1
              #  print(y, -1)
            for x in range(len(data[y]) - 2, 0, -1):
                tmp = min(result[y+1][x], result[y][x+1], result[y][x-1]) + data[y][x]
                if tmp < result[y][x]:
                    result[y][x] = tmp
                    changesmade += 1
                #    print(y, x)
        elif y == len(data) - 1:
            tmp = min(result[y-1][0], result[y][1]) + data[y][0]
            if tmp < result[y][0]:
                result[y][-1] = tmp
                #changesmade += 1
              #  print(y, 0)
            for x in range(1, len(data[y]) - 1):
                tmp = min(result[y-1][x], result[y][x+1], result[y][x-1]) + data[y][x]
                if tmp < result[y][x]:
                    result[y][x] = tmp
                    changesmade += 1
                #    print(y, x)
            tmp = min(result[-1][-2], result[-2][-1]) + data[-1][-1]
            if result[-1][-1] > tmp:
                result[-1][-1] = tmp
                break
        else:
            tmp = min(result[y-1][-1], result[y+1][-1], result[y][-2]) + data[y][-1]
            if tmp < result[y][-1]:
                result[y][-1] = tmp
                changesmade += 1
                if ypom and ypom < y:
                    ypom = y
              #  print(y, -1)
            for x in range(len(data[y]) - 2, 0, -1):
                tmp = min(result[y+1][x], result[y][x+1], result[y][x-1], result[y-1][x]) + data[y][x]
                if tmp < result[y][x]:
                    result[y][x] = tmp
                    changesmade += 1
                    if ypom and ypom < y:
                        ypom = y
                 #   print(y, x)
            tmp = min(result[y-1][0], result[y+1][0], result[y][1]) + data[y][0]
            if tmp < result[y][0]:
                changesmade += 1
                if ypom and ypom < y:
                    ypom = y
              #  print(y, 0)
                result[y][0] = tmp
        print(f'changesmade: {changesmade}, y = {y}')
        if changesmade > 0:
           y -= 1
        else:
            if ypom is not None:
                y = ypom + 1
            else:
                y += 1
    #print(result)
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
    print(f'Result for test data for task 1 is {solution1("Day_15/testdata.txt")}')
    print(f'Result for data 15 for task 1 is {solution1("Day_15/data15.txt")}')
    #print(f'Result for test data for task 2 is {solution2("Day_15/testdata.txt")}')
    #print(f'Result for data 15 for task 2 is {solution2("Day_15/data15.txt")}')

if __name__ == '__main__':
    main()