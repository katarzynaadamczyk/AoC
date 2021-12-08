def get_easy_numbers(datain):
    four, seven = '', ''
    for num in datain:
        if len(num) == 3:
            seven = num
        elif len(num) == 4:
            four = num
    return four, seven

def get_number(num, four, seven):
    result = 0
    if len(num) == 2:
        return 1
    elif len(num) == 3:
        return 7
    elif len(num) == 4:
        return 4
    elif len(num) == 7:
        return 8
    elif len(num) == 5:
        tmp = ''
        for i in seven:
            if i not in num:
                tmp += i
        if tmp == '':
            return 3
        tmp = ''
        for i in four:
            if i not in num:
                tmp += i
        if len(tmp) == 1:
            return 5
        return 2
    elif len(num) == 6:
        tmp = ''
        for i in four:
            if i not in num:
                tmp += i
        if tmp == '':
            return 9
        tmp = ''
        for i in seven:
            if i not in num:
                tmp += i
        if len(tmp) == 1:
            return 6
        return 0
    
    return 0

def main():
    with open('Day_8/data8.txt', 'r') as myfile:
        result = 0
        for line in myfile:
            datain = line[0:line.find('|')-1].split(' ')
            dataout = line[line.find('|')+2:len(line)-1].split(' ')
            four, seven = get_easy_numbers(datain)
            num = 0
            for x in range(len(dataout)):
                num += 10 ** (3 - x) * get_number(dataout[x], four, seven)
            
            result += num
        
        print(f'Result is {result}')      
            

if __name__ == '__main__':
    main()