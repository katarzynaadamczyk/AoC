def main():
    myfile = open('Day_1/data1.txt', 'r')
    x = int(myfile.readline())
    counti = 0
    for i in myfile:
        if int(i) > x:
            counti += 1
        x = int(i)
    myfile.close()
    print(counti)
    
    pass

if __name__ == '__main__':
    main()