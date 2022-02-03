def flash(data, x, y):
    data[x][y][1] = True
    xmin = x - 1 if x > 0 else x
    xmax = x + 2 if x < (len(data) - 1) else x + 1
    ymin = y - 1 if y > 0 else y
    ymax = y + 2 if y < (len(data[x]) - 1) else y + 1
    for i in range(xmin, xmax):
        for j in range(ymin, ymax):
            data[i][j][0] += 1
            if data[i][j][0] > 9 and not data[i][j][1]:
                flash(data, i, j)


def main():    
    with open('Day_11/data11.txt', 'r') as myfile:
        data = []
        for line in myfile:
            tmp = []
            for i in range(len(line) - 1):
                tmp.append([int(line[i]), False])
            data.append(tmp)
        noofflashes = 0
        for i in range(100):
            
            # adding 1
            
            for x in range(len(data)):
                for y in range(len(data[x])):
                    data[x][y][0] += 1
            
            # flashing
            for x in range(len(data)):
                for y in range(len(data[x])):
                    if data[x][y][0] > 9 and not data[x][y][1]:
                        flash(data, x, y)
            
            # changing state
            # print(f'Step {i + 1}')
            for x in range(len(data)):
                for y in range(len(data[x])):
                    
                    if data[x][y][0] > 9 and data[x][y][1]:
                        data[x][y][0] = 0
                        data[x][y][1] = False
                        noofflashes += 1
              #      print(data[x][y][0], end=' ')
              #  print('')
           # print('')

        print(f'Result is {noofflashes}')
        
if __name__ == '__main__':
    main()