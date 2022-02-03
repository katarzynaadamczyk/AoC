# Katarzyna Adamczyk
# Solution to day 15 task 1&2 of Advent of Code 2021
# still working on

def findpath(data): # searching for the path only down and right for now looking for solution to search also up and left
    if len(data) == len(data[0]):
        result = [[0]]
        for x in range(1, len(data)):
            result[0].append(result[0][x-1] + data[0][x])
            result.append([result[-1][0] + data[x][0]])

        for i in range(1, len(data)):
            tmpxright = [result[i][0]]
            tmpydown = [result[0][i]]
            for j in range(1, len(data)):
                tmpxright.append(min(tmpxright[-1], result[i-1][j]) + data[i][j])
                tmpydown.append(min(tmpydown[-1], result[j][i-1]) + data[j][i])
           # print(i)
           ## print(tmpxright)
           # print(tmpydown)
            result[i].insert(1, min(tmpxright[-2], result[i-1][j]) + data[i][j])
            result[-1].append(min(tmpydown[-2], result[-1][i-1]) + data[j][i])
            
            for j in range(len(data) - 2, i, -1):
                result[i].insert(i + 1, min(tmpxright[j+1], tmpxright[j-1], result[i-1][j]) + data[i][j])
                result[j].append(min(tmpydown[j+1], tmpydown[j-1], result[j][i-1]) + data[j][i])
                
                
            if i < len(data) - 1:
                result[i].insert(i + 1, min(tmpxright[i+1], tmpxright[i-1], result[i-1][i], tmpydown[i+1]) + data[i][i])
            else:
                result[i].insert(i + 1, min(tmpxright[i-1], result[i-1][i]) + data[i][i])
            
            if i < len(data) - 1:
                for j in range(i, 0, -1):
                    for k in range(i, 0, -1):
                        result[j][k] = min(result[j+1][k], result[j-1][k], result[j][k+1], result[j][k-1]) + data[j][k]
            else:
                pass
           # print(result)
        return result[-1][-1]
    return -1

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
      #  print(data)
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
    print(f'Result for data 15 for task 2 is {solution2("Day_15/data15.txt")}')

if __name__ == '__main__':
    main()