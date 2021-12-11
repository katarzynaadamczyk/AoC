# data[x][y] = [value(0-9), True if it belongs to any basin, False otherwise]
def basinsize(data, x, y):
    result = 1
    data[x][y][1] = True
    if x > 0 and data[x - 1][y][0] < 9 and not data[x - 1][y][1]:
        result += basinsize(data, x - 1, y)
    if y > 0 and data[x][y-1][0] < 9 and not data[x][y-1][1]: 
        result += basinsize(data, x, y - 1)
    if x < len(data) - 1 and data[x + 1][y][0] < 9 and not data[x + 1][y][1]:
        result += basinsize(data, x + 1, y)
    if y < len(data[x]) - 1 and data[x][y+1][0] < 9 and not data[x][y+1][1]: 
        result += basinsize(data, x, y + 1)
    return result


def main():
    with open('Day_9/data9.txt', 'r') as myfile:
        data = []
        top3 = [0, 0, 0]
        for line in myfile:
            tmp = []
            for i in range(len(line) - 1):
                tmp.append([int(line[i]), False])
            data.append(tmp)
        
        for x in range(len(data)):
            for y in range(len(data[x])):
                if data[x][y][0] < 9 and not data[x][y][1]:
                    basin = basinsize(data, x, y)
                    if basin >= top3[0]:
                        top3[2] = top3[1]
                        top3[1] = top3[0]
                        top3[0] = basin
                    elif basin >= top3[1]:
                        top3[2] = top3[1]
                        top3[1] = basin
                    elif basin > top3[2]:
                        top3[2] = basin
        
        print(top3)
        print(f'Result is {top3[2] * top3[1] * top3[0]}')

if __name__ == '__main__':
    main()