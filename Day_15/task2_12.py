# Katarzyna Adamczyk
# Solution to day 15 task 1 & 2 of Advent of Code 2021
# with a huge help from reddit forum
# original code: https://github.com/Farbfetzen/Advent_of_Code/blob/main/python/2021/day15.py
# using A* algorithm

from queue import PriorityQueue


def findpath(cavemap):
    """Pathfinding using A*"""
    start = (0, 0)
    destination = (len(cavemap[0]) - 1, len(cavemap) - 1)
    queueofpositions = PriorityQueue() # (risk, position)
    queueofpositions.put((0, start))
    camefrom = {start: None}
    risksofar = {start: 0}
    offsets = ((1, 0), (0, 1), (-1, 0), (0, -1))
    actpos = None
    while not queueofpositions.empty():
        actpos = queueofpositions.get()[1]
        if actpos == destination:
            break
        for offset in offsets:
            newpos = (actpos[0] + offset[0], actpos[1] + offset[1])
            if 0 <= newpos[0] < len(cavemap[0]) and 0 <= newpos[1] < len(cavemap):
                newrisk = risksofar[actpos] + cavemap[newpos[1]][newpos[0]]
                if newpos not in camefrom.keys() or newrisk < risksofar[newpos]:
                    risksofar[newpos] = newrisk
                    priority = newrisk
                    queueofpositions.put((priority, newpos))
                    camefrom[newpos] = actpos
    return risksofar[destination]


def preparemap(data, num):
    # make data table [5 x len(data)][len(data[0])]
    xlen = len(data[0])
    ylen = len(data)
    for i in range(ylen, num * ylen):
        tmp = []
        for x in range(len(data[0])):
            tmp.append((data[i - ylen][x] + (2 if data[i - ylen][x] == 9 else 1)) % 10)
        data.append(tmp)
    # make data table [5 x len(data)][5 x len(data[0])]
    for y in range(num * ylen):
        for x in range(xlen, num * xlen):
            data[y].append((data[y][x - xlen] + (2 if data[y][x - xlen] == 9 else 1)) % 10)
    return data

def solution1(filename):
    with open(filename, 'r') as myfile:
        data = [] 
        for line in myfile:
            tmp = [int(x) for x in line.strip()]
            data.append(tmp)
            
        return findpath(data)


def solution2(filename):
    with open(filename, 'r') as myfile:
        data = [] 
        for line in myfile:
            tmp = [int(x) for x in line.strip()]
            data.append(tmp)
        data = preparemap(data, 5)
        return findpath(data)

def main():
    print(f'Result for test data for task 1 is {solution1("Day_15/testdata.txt")} (should be 40)')
    print(f'Result for data 15 for task 1 is {solution1("Day_15/data15.txt")} (should be 487)')
    print(f'Result for test data for task 2 is {solution2("Day_15/testdata.txt")} (should be 315)')
    print(f'Result for data 15 for task 2 is {solution2("Day_15/data15.txt")} (should not be 2824)')
    
if __name__ == '__main__':
    main()