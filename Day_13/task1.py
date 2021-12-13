# Katarzyna Adamczyk
# Solution to day 13 task 1 of Advent of Code 2021

import numpy as np
from numpy.typing import _128Bit

def fold(points, foldline):
    if foldline[0] == 'x':
        newpoints = np.delete(points, [x for x in range(foldline[1], points.shape[1])], 1)
        newpoints = np.flip(newpoints, axis=1)
        foldedpoints = np.delete(points, [x for x in range(0, foldline[1] + 1)], 1)
        for y in range(newpoints.shape[0]):
            for x in range(newpoints.shape[1] if newpoints.shape[1] <= foldedpoints.shape[1] else foldedpoints.shape[1]):
                newpoints[y][x] = newpoints[y][x] or foldedpoints[y][x]
        return newpoints
    
    elif foldline[0 == 'y']:
        newpoints = np.delete(points, [x for x in range(foldline[1], points.shape[0])], 0)
        foldedpoints = np.delete(points, [x for x in range(0, foldline[1] + 1)], 0)
        foldedpoints = np.flip(foldedpoints, axis=0)
        for y in range(newpoints.shape[0] if newpoints.shape[0] <= foldedpoints.shape[0] else foldedpoints.shape[0]):
            for x in range(newpoints.shape[1]):
                newpoints[y][x] = newpoints[y][x] or foldedpoints[y][x]
        return newpoints

def solution(filename):
    with open(filename, 'r') as myfile:
        data = []
        maxx = 0
        maxy = 0
        line = myfile.readline()
        while line != '\n':
            elems = [int(x) for x in line.strip().split(',')]
            data.append(elems)
            if elems[0] > maxx:
                maxx = elems[0]
            if elems[1] > maxy:
                maxy = elems[1]
            line = myfile.readline()
        folding = []
        for line in myfile:
            if line.find('x') != -1:
                folding.append(['x', int(line[line.find('=')+1::])])
            if line.find('y') != -1:
                folding.append(['y', int(line[line.find('=')+1::])])
        
        points = np.zeros((maxy + 1, maxx + 1), dtype=bool)
        for point in data:
            points[point[1]][point[0]] = True
        
        points = fold(points, folding[0])
      
        return(sum(sum(points)))
                    
        

def main():
    print(f'Result for test data 1 is {solution("Day_13/testdata.txt")}')
    print(f'Result for data 13 is {solution("Day_13/data13.txt")}')

if __name__ == '__main__':
    main()