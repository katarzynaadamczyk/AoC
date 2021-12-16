# Katarzyna Adamczyk
# Solution to day 15 task 2 of Advent of Code 2021

def findpathontheright(startvalue, x, y, xrange, yfinal, data):
    result = []
    if x < (len(data[y]) - 1):
        tmp = [startvalue + data[y][x+1]]
        for i in range(x+2, min(x+xrange, len(data[y]))):
            tmp.append(tmp[-1] + data[y][i])
        result.append(tmp)
        for i in range(y+1, min(yfinal + 1, len(data))):
            tmp = [result[-1][-1] + data[y+1][min(x+xrange, len(data[y+1]))-1]]
            for j in range(min(x+xrange, len(data[y+1]))-2, x, -1):
                tmp.insert(0, min(tmp[0], result[-1][j-x-1]) + data[i][j])
            result.append(tmp)
        print(result)
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
            print(z)
            for j in range(x+1, min(xfinal + 1, len(data[i]))):
                print(result[z][-1], result[z+1][j-x])
                result[z].append(min(result[z][-1], result[z+1][j-x]) + data[i][j])
            z -= 1
        print(data)
        print(result)
        return result[0][-1]
    return -1
            
    

'''

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
'''

def findpath(data): # searching for the path only down and right and omitting the large values to the right or to the left
    result = []
    tmp = [0]
    for x in range(1, len(data[0])):
       # actx = min([findpathdown() for i in range(2, 8)]) # min z [findpath] for range (2, 8) findpathdown(startvalue, x, y, xfinal, yrange, data):
       # if actx > 0:
       #     tmp.append(min(tmp[x-1], actx) + data[0][x])
       # else:
        tmp.append(tmp[x-1] + data[0][x])
    result.append(tmp)
    for y in range(1, len(data)):
       # acty = checkony(data, result, 0, y) # min z [findpath] for range (2, 8)
       # if acty > 0:
       #     tmp = [min(result[y-1][0], acty) + data[y][0]]
       # else:
        tmp = [data[y][0] + result[y-1][0]]
        for x in range(1, len(data[y])):
            # TODO
            acty = min([findpathontheright() for i in range(2, 8)]) # min z [findpath] for range (2, 8) min z [findpath] for range (2, 8) findpathdown(startvalue, x, y, xfinal, yrange, data):
            actx = min([findpathdown() for i in range(2, 8)]) # min z [findpath] for range (2, 8)
            
            if actx > 0 and acty > 0:
                tmp.append(min(tmp[x-1], result[y-1][x], actx, acty) + data[y][x])
            elif actx > 0:
                tmp.append(min(tmp[x-1], result[y-1][x], actx) + data[y][x])
            elif acty > 0:
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

            

def solution(filename):
    with open(filename, 'r') as myfile:
        data = [] 
        for line in myfile:
            tmp = [int(x) for x in line.strip()]
            data.append(tmp)
        # data = preparemap(data, 5)
        print(findpathontheright(10, 2, 3, 5, 7, data))
        print(findpathdown(10, 2, 3, 5, 7, data))
        return findpath(data)

def main():
    print(f'Result for test data for task 1 is {solution("Day_15/testdata.txt")}')
   # print(f'Result for data 15 for task 1 is {solution("Day_15/data15.txt")}')

if __name__ == '__main__':
    main()