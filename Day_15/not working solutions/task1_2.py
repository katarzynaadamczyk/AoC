# Katarzyna Adamczyk
# Solution to day 15 task 1 of Advent of Code 2021

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