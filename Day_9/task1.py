def main():
    with open('Day_9/data9.txt', 'r') as myfile:
        result = 0
        data = []
        for line in myfile:
            tmp = []
            for i in range(len(line) - 1):
                tmp.append(int(line[i]))
            data.append(tmp)
        
        for x in range(len(data)):
            for y in range(len(data[x])):
                num = data[x][y]
                minx = x - 1 if x > 0 else x + 1
                miny = y - 1 if y > 0 else y + 1
                maxx = x + 2 if x < (len(data) - 1) else x
                maxy = y + 2 if y < (len(data[x]) - 1) else y
                check = True
                for i in range(minx, maxx, 2):
                    if data[i][y] <= num:
                        check = False
                        break
                if check:
                    for j in range(miny, maxy, 2):
                        if data[x][j] <= num:
                            check = False
                            break        
                    if check:
                        result += num + 1
        
        print(f'Result is {result}')      
            

if __name__ == '__main__':
    main()