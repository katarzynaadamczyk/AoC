def main():
    with open('Day_6/data6.txt', 'r') as myfile:
        data = myfile.readline().split(',')
        for i in range(len(data)):
            data[i] = int(data[i])
        indata = [0 for i in range(9)]
        for j in data:
            indata[j] += 1
        print(indata)
        for day in range(256):
            tmp = [0 for i in range(9)]
            for j in range(1, len(indata)):
                tmp[j-1] = indata[j]
                
            tmp[8] = indata[0]
            tmp[6] += indata[0]
            indata = tmp
            print(indata)
        print(indata)
        print(f'Result is {sum(indata)}')            
            

if __name__ == '__main__':
    main()