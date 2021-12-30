# Katarzyna Adamczyk
# Solution to day 17 task 2 of Advent of Code 2021

from itertools import product

def howmanyiterationsforx(xmin, xmax):
    xiterations = dict()
    xiterations.setdefault(1, set())
    xiterations[1].add(xmax)
    xzeros = {}
    for x in range(xmax - 1, 0, -1):
        velx = x
        xposition = 0
        noofit = 0
        while velx > 0 and xposition <= xmax:
            xposition += velx
            velx -= 1
            noofit += 1
            if xposition >= xmin and xposition <= xmax:
                xiterations.setdefault(noofit, set())
                xiterations[noofit].add(x)
                if velx == 0:
                    xiterations.setdefault('more', set())
                    xiterations['more'].add(x)
                    xzeros.setdefault(x, noofit)
        if xposition < xmin:
            break
    if 'more' in xiterations.keys():
        lst = list(xiterations.keys())
        lst.remove('more')
        for x in xiterations['more']:
            maxx = 0
            for i in range(max(lst), 0, -1):
                if i in xiterations.keys():
                    if x not in xiterations[i]:
                        if i > xzeros[x]:
                            xiterations[i].add(x)
                        else:
                            break
                    
    return xiterations


def howmanyiterationsfory(ymin, ymax):
    yiterations = dict()
    for y in range(1000, -1000, -1):
        yvel = y
        yposition = 0
        noofit = 0
        
        while yposition >= ymin:
            yposition += yvel
            yvel -= 1
            noofit += 1
            if yposition >= ymin and yposition <= ymax:
                yiterations.setdefault(noofit, set())
                yiterations[noofit].add(y)
    
    return yiterations

def findeveryinitialvelocity(xmin, xmax, ymin, ymax):
    xiterations = howmanyiterationsforx(xmin, xmax)
    yiterations = howmanyiterationsfory(ymin, ymax)
    print(xiterations)
    print(yiterations)
    xkeys = set(xiterations.keys())
    ykeys = set(yiterations.keys())
    result = set()
    common = xkeys.intersection(ykeys)
    xmaxit = max(common)
    for key in common:
        for s in product(xiterations[key], yiterations[key]):
            result.add(s)
        del xiterations[key]
        del yiterations[key]
    
    for key in yiterations.keys():
        if key > xmaxit:
            for s in product(xiterations['more'], yiterations[key]):
                print(s)
                result.add(s)
    
    print(len(result))
    lst = list(result)
    lst.sort()
    print(lst)
    
    return len(result)

def solution2(filename):
    with open(filename, 'r') as myfile:
        line = myfile.readline().strip()
        xmin = int(line[line.find('=')+1:line.find('..')])
        xmax = int(line[line.find('..')+2:line.find(',')])
        ymin = int(line[line.rfind('=')+1:line.rfind('..')])
        ymax = int(line[line.rfind('..')+2::]) 
        print(xmin, xmax, ymin, ymax)   
        return findeveryinitialvelocity(xmin, xmax, ymin, ymax)

def main():
    print(f'Result for test data for task 1 is {solution2("Day_17/testdata.txt")}')
    print(f'Result for data 15 for task 1 is {solution2("Day_17/data17.txt")}')

if __name__ == '__main__':
    main()