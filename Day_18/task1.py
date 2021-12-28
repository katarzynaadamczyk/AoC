# Katarzyna Adamczyk
# Solution to day 18 task 1 of Advent of Code 2021


def checkposition(num):
    # check position of place to explode a pair or split a number
    numberofbrackets = 0
    positionofnumber = -1
    for i in range(len(num)):
        if num[i] == '[':
            numberofbrackets += 1
            if numberofbrackets > 4:
                break
        elif num[i] == ']':
            numberofbrackets -= 1
        elif num[i].isdecimal():
            if i < len(num) - 1 and num[i+1].isdecimal():
                if positionofnumber < 0:
                    positionofnumber = i
    
    
    return i if i < len(num) else positionofnumber if positionofnumber > 0 else len(num)

def explodeapair(num, pos):
    # explode a pair at given pos
    endpairpos = num.find(']', pos)
    leftnum = int(num[pos+1:num.find(',', pos)])
    rightnum = int(num[num.find(',', pos)+1:endpairpos])
    
    num = num[0:pos] + '0' + num[endpairpos+1::]
    print(num)
    for i in range(pos-1, 0, -1):
        if num[i].isdecimal():
            for j in range(i - 1, 0, -1):
                if not num[j].isdecimal():
                    break
            pos += i - j
            num = num[0:j+1] + str(leftnum + int(num[j+1:i+1])) + num[i+1::]
            break
    print(num)
    for i in range(pos+1, len(num)):
        if num[i].isdecimal():
            for j in range(i + 1, len(num)):
                if not num[j].isdecimal():
                    break
            num = num[0:i] + str(rightnum + int(num[i:j])) + num[j::]
            break    
    print(num)
    return num

def splitanumber(num, pos):
    # split a number at given pos
    for char in ',[]':
        commapos = num.find(char, pos)
        if commapos >= 0:
            break
    pairtoadd = '['
    pairtoadd += str(int(num[pos:commapos]) // 2) + ','
    pairtoadd += str((int(num[pos:commapos]) + 1) // 2) + ']'
    
    return num[0:pos] + pairtoadd + num[commapos::]

def explodeorsplit(num, pos):
    # explode or split a snailfish number
    if num[pos] == '[':
        return explodeapair(num, pos)
    return splitanumber(num, pos)

def shorten(num):
    # shortening the num
    pos = checkposition(num)
    while pos < len(num) - 1:
        print(num)
        num = explodeorsplit(num, pos)
        pos = checkposition(num)
    return num
    
def magnitude(num):
    # TODO - counting the magnitude of a number
    pass

def solution1(filename):
    with open(filename, 'r') as myfile:
        sum = ''
        i = 0
        for line in myfile:    
            line = shorten(line.strip())
            if sum == '':
                sum = line
            else:
                sum = '[' + sum + ',' + line + ']'
                sum = shorten(sum)
                i += 1
            if i > 2:
                break    
        print(sum)
        return magnitude(sum)
    

def main():
    print(f'Result for test data for task 1 is {solution1("Day_18/testdata.txt")}')
    #print(f'Result for data 18 for task 1 is {solution1("Day_18/data18.txt")}')

if __name__ == '__main__':
    main()