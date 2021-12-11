# data[x][y] = [value(0-9), number_of_basin_it_belongs_to]


def main():
    with open('Day_9/data9.txt', 'r') as myfile:
        lowpoints = []
        data = []
        basinno = 0
        for line in myfile:
            tmp = []
            for i in range(len(line) - 1):
                tmp.append([int(line[i]), basinno])
            data.append(tmp)
        
        basinno += 1
        
        for x in range(len(data)):
            for y in range(len(data[x])):
                if data[x][y][0] < 9:
                    if x > 0 and data[x-1][y][1] != 0:
                        data[x][y][1] = data[x-1][y][1]
                    elif y > 0 and data[x][y-1][1] != 0:
                        data[x][y][1] = data[x][y-1][1]
                    else:
                        data[x][y][1] = basinno
                        basinno += 1
        
        basinno = set()
        for i in range(len(data)):
            for x in range(len(data)):
                for y in range(len(data[x])): 
                    if x < (len(data) - 1) and data[x+1][y][1] != 0:
                        data[x][y][1] = min(data[x+1][y][1], data[x][y][1])
                    elif y < (len(data[x]) - 1) and data[x][y+1][1] != 0:
                        data[x][y][1] = min(data[x][y+1][1], data[x][y][1])
        for x in range(len(data)):
            for y in range(len(data[x])): 
                basinno.add(data[x][y][1])
                print(data[x][y][1], end=" ")
            print('')
        print(len(basinno))

if __name__ == '__main__':
    main()