def main():
    myfile = open('Day_3/data3.txt', 'r')
    data = []
    for i in myfile:
        data.append(i)
    myfile.close()
    countofones = []
    for i in range(len(data[0]) - 1):
        countofones.append(0)
    for i in data:
        for j in range(len(i)):
            if i[j] == '1':
                countofones[j] += 1
    gamma = ''
    epsilon = ''
    
    for i in countofones:
        if i > (len(data) - i):
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    print(countofones)
    print(f'{gamma} to decimal: {int(gamma, 2)}')
    print(f'{epsilon} to decimal: {int(epsilon, 2)}')
    print(f'Nasz wynik: {int(gamma, 2) * int(epsilon, 2)}')

if __name__ == '__main__':
    main()