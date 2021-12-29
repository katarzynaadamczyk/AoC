# Katarzyna Adamczyk
# Solution to day 18 task 1&2 of Advent of Code 2021


def checkforexplode(num):
    numberofbrackets = 0
    for i in range(len(num)):
        if num[i] == '[':
            numberofbrackets += 1
            if numberofbrackets > 4:
                return i
        elif num[i] == ']':
            numberofbrackets -= 1

    return -1
    
def checkforsplit(num):
    for i in range(len(num) - 1):
        if num[i].isdecimal() and num[i+1].isdecimal():
            return i
    return len(num)

def checkposition(num):
    # check position of place to explode a pair or split a number
    posexplode = checkforexplode(num)
    return posexplode if posexplode >= 0 else checkforsplit(num)

def explodeapair(num, pos):
    # explode a pair at given pos
    endpairpos = num.find(']', pos)
    leftnum = int(num[pos+1:num.find(',', pos)])
    rightnum = int(num[num.find(',', pos)+1:endpairpos])
    
    num = num[0:pos] + '0' + num[endpairpos+1::]
    
    for i in range(pos-1, 0, -1):
        if num[i].isdecimal():
            for j in range(i - 1, 0, -1):
                if not num[j].isdecimal():
                    break
            pos += i - j
            num = num[0:j+1] + str(leftnum + int(num[j+1:i+1])) + num[i+1::]
            break
    
    for i in range(pos+1, len(num)):
        if num[i].isdecimal():
            for j in range(i + 1, len(num)):
                if not num[j].isdecimal():
                    break
            num = num[0:i] + str(rightnum + int(num[i:j])) + num[j::]
            break    
    
    return num

def splitanumber(num, pos):
    # split a number at given pos
    for endofnumber in range(pos + 1, len(num)):
        if not num[endofnumber].isdecimal():
            break
    numtosplit = int(num[pos:endofnumber])
    pairtoadd = '['
    pairtoadd += str(numtosplit // 2) + ','
    pairtoadd += str(numtosplit // 2 + (1 if numtosplit % 2 == 1 else 0)) + ']'
    
    return num[0:pos] + pairtoadd + num[endofnumber::]

def explodeorsplit(num, pos):
    # explode or split a snailfish number
    if num[pos] == '[':
        return explodeapair(num, pos)
    return splitanumber(num, pos)

def shorten(num):
    # shortening the num
    pos = checkposition(num)
    while pos < len(num) - 1:
        #print(num)
        num = explodeorsplit(num, pos)
        pos = checkposition(num)
    return num
    
def magnitude(num):
    # counting the magnitude of a number
    if num.isdecimal():
        return int(num)
    numberofbrackets = 0
    for i in range(len(num)):
        if num[i] == '[':
            numberofbrackets += 1
        elif num[i] == ']':
            numberofbrackets -= 1
        elif num[i] == ',' and numberofbrackets == 1:
            return 3 * magnitude(num[1:i]) + 2 * magnitude(num[i+1:-1])    
    

def solution1(filename):
    with open(filename, 'r') as myfile:
        sum = ''
        for line in myfile:    
            line = shorten(line.strip())
            if sum == '':
                sum = line
            else:
                sum = '[' + sum + ',' + line + ']'
                sum = shorten(sum)
    #        print(sum)
        return magnitude(sum)
    

def solution2(filename):
    with open(filename, 'r') as myfile:
        lstofnumbers = []
        for line in myfile:    
            lstofnumbers.append(shorten(line.strip()))
        
        print(lstofnumbers)
        maxmagnitude = 0
        
        for i in range(len(lstofnumbers)):
            for j in range(len(lstofnumbers)):
                if lstofnumbers[i] != lstofnumbers[j]:
                    actualmagnitude = magnitude(shorten('[' + lstofnumbers[i] + ',' + lstofnumbers[j] + ']'))
                    
                    if actualmagnitude > maxmagnitude:
                        maxmagnitude = actualmagnitude
                        print(lstofnumbers[i])
                        print(lstofnumbers[j])
                    
                        
        return maxmagnitude


def main():
    print(f'Result for test data for task 1 is {solution1("Day_18/testdata.txt")}')
    print(f'Result for test data for task 1 is {solution1("Day_18/testdata1.txt")}')
    print(f'Result for data 18 for task 1 is {solution1("Day_18/data18.txt")}')
    
    print(f'Result for test data for task 1 is {solution2("Day_18/testdata.txt")}')
    print(f'Result for data 18 for task 1 is {solution2("Day_18/data18.txt")}')

if __name__ == '__main__':
    main()