def main():
    with open('Day_7/data7.txt', 'r') as myfile:
        data = myfile.readline().split(',')
        for i in range(len(data)):
            data[i] = int(data[i])
        sorted_data = sorted(data)
        if sorted_data[0] == sorted_data[-1]:
            print('Result is 0')
        else:
            median = sorted_data[len(sorted_data) // 2]
            result = 0
            for i in sorted_data:
                result += abs(median - i)
            print(f'Result is: {result}')           
            

if __name__ == '__main__':
    main()
    