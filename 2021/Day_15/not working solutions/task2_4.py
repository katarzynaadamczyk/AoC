# Katarzyna Adamczyk
# Solution to day 15 task 1&2 of Advent of Code 2021

def findpath(data): # searching for the path only down and right for now looking for solution to search also up and left
    result1 = [[0]] # down, right
    result2 = [[0]] # down, left
    result3 = [[0]] # up, right
    result4 = [[0]] # up, left
    for x in range(1, len(data[0])):
        result1[0].append(result1[0][-1] + data[0][x]) # prepared result1
        result2[0].append(result2[0][-1] + data[0][x])
        result4[0].append(result4[0][-1] + data[0][x])
        
    for y in range(1, len(data)):
        result1.append([data[y][0] + result1[y-1][0]])
        result3.append([data[y][0] + result1[y-1][0]])
        result4.append([data[y][0] + result1[y-1][0]])
        result2.append([data[y][-1] + result2[y-1][-1]]) 
        result4[y].append(data[y][-1] + result4[y-1][-1])
        for x in range(1, len(data[y])):
            result1[y].append(min(result1[y][-1], result1[y-1][x]) + data[y][x])
    # done result1, prepared result2
    
    result4[-1] = [result4[-1][0]]
    for x in range(1, len(data[0])):
        result4[-1].append(result4[-1][-1] + data[-1][x])
    
    for x in range(1, len(data[0])):
        result3[-1].append(result3[-1][-1] + data[-1][x])
    # prepared result3
    
    for y in range(1, len(data)):
        for x in range(len(data[0]) - 2, -1, -1):
            result2[y].insert(0, data[y][x] + min(result2[y-1][x], result2[y][-1]))
    # done result2
    
 
    for y in range(len(data) - 2, -1, -1):
        for x in range(1, len(data[0])):
            result3[y].append(data[y][x] + min(result3[y+1][x], result3[y][-1]))
    # done result3
    
    for y in range(len(data) - 1):
        result4[y] = [result4[y][-1]]
    for y in range(len(data) - 2, -1, -1):    
        for x in range(len(data[0]) - 2, -1, -1):
            result4[y].insert(0, data[y][x] + min(result4[y+1][x], result4[y][0]))
    # done result4
    
    result = []
    
    for y in range(len(data)):
        tmp = []
        for x in range(len(data[0])):
            tmp.append(min(result1[y][x], result2[y][x], result3[y][x], result4[y][x]))     
        result.append(tmp)   
    
    result[-1][-1] = min(result[-1][-2], result[-2][-1]) + data[-1][-1]
      
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
    print(f'Result for test data for task 1 is {solution1("Day_15/testdata.txt")}')
    print(f'Result for data 15 for task 1 is {solution1("Day_15/data15.txt")}')
    print(f'Result for test data for task 2 is {solution2("Day_15/testdata.txt")}')
    print(f'Result for data 15 for task 2 is {solution2("Day_15/data15.txt")}')

if __name__ == '__main__':
    main()