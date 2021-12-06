def main():
    with open('Day_6/data6.txt', 'r') as myfile:
        data = myfile.readline().split(',')
        for i in range(len(data)):
            data[i] = int(data[i])
        for day in range(80):
            tmp = []
            for i in range(len(data)):
                if data[i] == 0:
                    tmp.append(8)
                    data[i] = 6
                else:
                    data[i] -= 1
            for i in tmp:
                data.append(i)
        print(f'Result is {len(data)}')            
            

if __name__ == '__main__':
    main()