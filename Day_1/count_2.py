def main():
    myfile = open('Day_1/data1.txt', 'r')
    x = []
    counti = 0
    for i in myfile:
        x.append(int(i))
    for i in range(0, len(x) - 3):
        if (x[i] + x[i + 1] + x[i + 2]) < (x[i + 1] + x[i + 2] + x[i + 3]):
            counti += 1
    myfile.close()
    print(f'First try: {counti}')
    
    x2 = []
    counti2 = 0
    for i in range(0, len(x) - 2):
        x2.append(x[i] + x[i + 1] + x[i + 2])
    
    for i in range(0, len(x2) - 1):
        if x2[i] < x2[i + 1]:
            counti2 += 1
    
    print(f'Second try: {counti2}')
    
    pass

if __name__ == '__main__':
    main()