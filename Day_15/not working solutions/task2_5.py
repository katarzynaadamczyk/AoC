# Katarzyna Adamczyk
# Solution to day 15 task 1&2 of Advent of Code 2021

def actualizeresult(result, data, x, y):
  #  print(x, y)
  #  print(result)
    if y > 0:
        for i in range(x+1, len(data[y])):
            result[y][i] = min(result[y][i-1], result[y-1][i]) + data[y][i]
    else:
        for i in range(x+1, len(data[y])):
            result[y][i] = result[y][i-1] + data[y][i]
    
    for i in range(y+1, len(data)):
        if x > 0:
            for j in range(x, len(data[i])):
                result[i][j] = min(result[i][j-1], result[i-1][j]) + data[i][j]
        else:
            for j in range(x, len(data[i])):
                result[i][j] = result[i-1][j] + data[i][j]
   # print(result)
    return result

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
        
    
    changesmade = 0
    
    for i in range(len(data) - 1):
        print(f'y = {i} out of {len(data) - 1}')
        for j in range(len(data[i]) - 2, -1, -1):
            tmp = min(result[i+1][j], result[i][j+1]) + data[i][j]
            if tmp < result[i][j]:
                result[i][j] = tmp
                changesmade += 1
                result = actualizeresult(result, data, j, i + 1)
    print(changesmade)
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
    #print(f'Result for test data for task 1 is {solution1("Day_15/testdata.txt")}')
    #print(f'Result for data 15 for task 1 is {solution1("Day_15/data15.txt")}')
    #print(f'Result for test data for task 2 is {solution2("Day_15/testdata.txt")}')
    print(f'Result for data 15 for task 2 is {solution2("Day_15/data15.txt")}')

if __name__ == '__main__':
    main()