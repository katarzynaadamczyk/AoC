
def main():
    with open('Day_5/data5.txt', 'r') as myfile:
        xmax = 0
        ymax = 0
        data = []
        
        for line in myfile:
            tmp = []
            x = int(line[0:line.find(',')])
            tmp.append(x)
            if x > xmax:
                xmax = x
            y = int(line[line.find(',')+1:line.find(' ')])
            if y > ymax:
                ymax = y
            tmp.append(y)
            x = int(line[line.rfind(' ')+1:line.rfind(',')])
            tmp.append(x)
            if x > xmax:
                xmax = x
            y = int(line[line.rfind(',')+1::])
            if y > ymax:
                ymax = y
            tmp.append(y)
            data.append(tmp)
        
        print(data[0])
        print(data[-1])
        xmax += 10
        ymax += 10
        
        nums = []
        for x in range(xmax):
            tmp = []
            for y in range(ymax):
                tmp.append(0)
            nums.append(tmp)
        
        for line in data:
            if line[0] == line[2]:
                for i in range(line[1], line[3] + 1):
                    nums[line[0]][i] += 1
                for i in range(line[3], line[1] + 1):
                    nums[line[0]][i] += 1

            elif line[1] == line[3]:
                for i in range(line[0], line[2] + 1):
                    nums[i][line[1]] += 1
                for i in range(line[2], line[0] + 1):
                    nums[i][line[1]] += 1
            
        result = 0
        
        for x in range(xmax):
            for y in range(ymax):
                if nums[x][y] > 1:
                    result += 1
       # print(nums)
        print(f'Result: {result}')        
            
            

if __name__ == '__main__':
    main()