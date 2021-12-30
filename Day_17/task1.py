# Katarzyna Adamczyk
# Solution to day 17 task 1 of Advent of Code 2021

def howmanyiterationsforx(xmin, xmax):
    iterations = set()
    for x in range(xmax, 0, -1):
        velx = x
        xposition = 0
        noofit = 0
        while velx > 0 and xposition < xmax:
            xposition += velx
            velx -= 1
            noofit += 1
            if xposition > xmin:
                iterations.add(noofit - 1)
        if xposition < xmin:
            break
        print(f'x: {x}, noofit {noofit}')
        iterations.add(noofit - 1)
    return iterations

def sumofones(num):
    return sum([i for i in range(1, num + 1)])

def findmaxy(ymin, ymax):
    print(ymin, ymax)
    for y in range(1000, 0, -1):
        yvel = y
        yposition = 0
        maxyvalue = 0
        while yposition >= ymin:
            yposition += yvel
            yvel -= 1
            if yposition > maxyvalue:
                maxyvalue = yposition
            if yposition >= ymin and yposition <= ymax:
                print(f'max: {maxyvalue} for yvel = {y}')
                return maxyvalue

def solution1(filename):
    with open(filename, 'r') as myfile:
        line = myfile.readline().strip()
        xmin = int(line[line.find('=')+1:line.find('..')])
        xmax = int(line[line.find('..')+2:line.find(',')])
        ymin = int(line[line.rfind('=')+1:line.rfind('..')])
        ymax = int(line[line.rfind('..')+2::]) 
        print(xmin, xmax, ymin, ymax)   
        return findmaxy(ymin, ymax)

def main():
    print(f'Result for test data for task 1 is {solution1("Day_17/testdata.txt")}')
    print(f'Result for data 15 for task 1 is {solution1("Day_17/data17.txt")}')

if __name__ == '__main__':
    main()