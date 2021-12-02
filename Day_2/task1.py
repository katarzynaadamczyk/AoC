def main():
    myfile = open('Day_2/data2.txt', 'r')
    x = 0
    y = 0
    j = 0
    for i in myfile:
        add = int(i[i.find(' ') + 1::])
        if i[0] == 'f':
            x += add
        elif i[0] == 'u':
            y -= add
        else:
            y += add
        if j < 10:
            print(add)
        j += 1
    myfile.close()
    print(f'Result: x = {x}, y={y}, x*y = {x*y}')
    

if __name__ == '__main__':
    main()