def main():
    with open('Day_8/data8.txt', 'r') as myfile:
        result = 0
        for line in myfile:
            tmp = line[line.find('|')+1:len(line)-1].split(' ')
            print(tmp)
            for i in tmp:
                if (len(i) >=2 and len(i) <=4) or len(i) == 7:
                    result += 1
        
        print(f'Result is {result}')      
            

if __name__ == '__main__':
    main()