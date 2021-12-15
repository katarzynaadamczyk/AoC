# Katarzyna Adamczyk
# Solution to day 15 task 1 of Advent of Code 2021

def findpath(data, x, y, result):
    while True:
      #  print(data[y][x], end=": ")
      #  print(result)
        if y < (len(data) - 1) and x < (len(data[y]) - 1):
            result, x, y = min(findpath(data, x+1, y, result + data[y][x+1]), findpath(data, x, y+1, result + data[y+1][x]))
            '''            if data[y+1][x] < data[y][x+1]:
                result += data[y+1][x]
                y = y + 1
            elif data[y+1][x] > data[y][x+1]:
                result += data[y][x+1]
                x = x + 1
            else:
                result += data[y][x+1]
                return min(findpath(data, x+1, y, result), findpath(data, x, y+1, result))
        '''
        elif y < (len(data) - 1) and x == (len(data[y]) - 1):
            result += data[y+1][x]
            y = y + 1
        elif x < (len(data[y]) - 1) and y == (len(data) - 1):
            result += data[y][x+1]
            x = x + 1
        if x == (len(data[y]) - 1) and y == (len(data) - 1):
            break
    return result, x, y
                 

def solution(filename):
    with open(filename, 'r') as myfile:
        data = [] 
        for line in myfile:
            tmp = [int(x) for x in line.strip()]
            data.append(tmp)
        
        return findpath(data, 0, 0, 0)

def main():
    print(f'Result for test data for task 1 is {solution("Day_15/testdata.txt")}')
    print(f'Result for data 15 for task 1 is {solution("Day_15/data15.txt")}')

if __name__ == '__main__':
    main()