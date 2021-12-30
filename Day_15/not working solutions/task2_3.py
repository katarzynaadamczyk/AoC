# Katarzyna Adamczyk
# Solution to day 15 task 2 of Advent of Code 2021

def findpathontheright(startvalue, x, y, xrange, yfinal, data):
    result = []
    if x < (len(data[y]) - 1):
        tmp = [startvalue + data[y][x+1]]
        for i in range(x+2, min(x+xrange, len(data[y]))):
            tmp.append(tmp[-1] + data[y][i])
        result.append(tmp)
        for i in range(min(y+1, len(data) - 1), min(yfinal + 1, len(data))):
           # print(i+1, min(x+xrange, len(data[i]))-1)
            tmp = [result[-1][-1] + data[i][min(x+xrange, len(data[i]))-1]]
            for j in range(min(x+xrange, len(data[y+1]))-2, x, -1):
                tmp.insert(0, min(tmp[0], result[-1][j-x-1]) + data[i][j])
            result.append(tmp)
       # print(data)
      #  print(x, y, xrange, yfinal)
       # print(result)
        return result[-1][-1]
    return -1

def findpathdown(startvalue, x, y, xfinal, yrange, data):
    result = []
    if y < (len(data) - 1):
        
        result = [[startvalue + data[y+1][x]]]
        for i in range(y+2, min(y+yrange, len(data))):
            result.append([result[-1][-1] + data[i][x]])
        for i in range(x + 1, min(xfinal + 1, len(data[y]))):
            result[-1].append(result[-1][-1] + data[min(y+yrange, len(data))-1][i])
        z = len(result) - 2
        for i in range(min(y+yrange, len(data)) - 2, y, -1): 
       #     print(z)
            for j in range(x+1, min(xfinal + 1, len(data[i]))):
        #        print(result[z][-1], result[z+1][j-x])
                result[z].append(min(result[z][-1], result[z+1][j-x]) + data[i][j])
            z -= 1
     #   print(data)
     ##   print(result)
      #  print(x, y, xfinal, yrange)
        return result[0][-1]
    return -1
            
def check(data, result, tmp, x, y):
    tmp2 = []
    for i in range(max(0, x - len(data[y]) // 2), max(x - 1, 0)):
      #  print('down')
        act = findpathdown(tmp[i], i, y, x, 8, data)
        if act > 0:
            tmp2.append(act)
    for i in range(max(0, len(data) // 2), max(y-1, 0)):
     #   print('right')
        act = findpathontheright(result[i][x], x, i, 20, y, data)
        if act > 0:
            tmp2.append(act)
    return min(tmp2) if len(tmp2) > 0 else -1

def findpath(data): # searching for the path only down and right and omitting the large values to the right or to the left
    result = []
    tmp = [0]
    for x in range(1, len(data[0])):
        print(f'in first for x, {x} ')
        act = check(data, result, tmp, x, 0)
        if act > 0:
            tmp.append(min(tmp[x-1], act) + data[0][x])
        else:
            tmp.append(tmp[x-1] + data[0][x])
    result.append(tmp)
    for y in range(1, len(data)):
        print(f'y = {y} out of {len(data) - 1}')
        act = check(data, result, tmp, 0, y)
        if act > 0:
            tmp = [min(result[y-1][0], act) + data[y][0]]
        else:
            tmp = [data[y][0] + result[y-1][0]]
        for x in range(1, len(data[y])):
            act = check(data, result, tmp, x, y)
            
            if act > 0 :
                tmp.append(min(tmp[x-1], result[y-1][x], act) + data[y][x])
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

            

def solution(filename):
    with open(filename, 'r') as myfile:
        data = [] 
        for line in myfile:
            tmp = [int(x) for x in line.strip()]
            data.append(tmp)
        data = preparemap(data, 5)
        #data[0][0] = 0
        return findpath(data)

def main():
    print(f'Result for test data for task 1 is {solution("Day_15/testdata.txt")}')
    print(f'Result for data 15 for task 1 is {solution("Day_15/data15.txt")}')

if __name__ == '__main__':
    main()