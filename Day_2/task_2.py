def main():
    myfile = open('Day_2/data2.txt', 'r')
    x = 0
    y = 0
    aim = 0
    for i in myfile:
        add = int(i[i.find(' ') + 1::])
        if i[0] == 'f':
            x += add
            y += add * aim
        elif i[0] == 'u':
            aim -= add
        else:
            aim += add
    myfile.close()
    print(f'Result: x = {x}, y={y}, x*y = {x*y}')
    

if __name__ == '__main__':
    main()