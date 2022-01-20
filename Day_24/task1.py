# Katarzyna Adamczyk
# Solution to day 24 task 1 of Advent of Code 2021

from itertools import product

dimensions = {'w': 0, 'x': 0, 'y': 0, 'z': 0}

def inp(a, val):
    dimensions[a] = val
    
def add(a, b):
    dimensions[a] += (dimensions[b] if b.isalpha() else int(b))
    
def mul(a, b):
    dimensions[a] *= (dimensions[b] if b.isalpha() else int(b))
    
def div(a, b):
    dimensions[a] //= (dimensions[b] if b.isalpha() else int(b))
        
def mod(a, b):
    dimensions[a] %= (dimensions[b] if b.isalpha() else int(b))
    
def eql(a, b):
    dimensions[a] = 1 if dimensions[a] == (dimensions[b] if b.isalpha() else int(b)) else 0
    

def findmaxserialnumber(data):
    for num in product('987654321', repeat=14):
        numiterator = 0
        for key in dimensions:
            dimensions[key] = 0
        for instrucion in data:
            if instrucion[0] == 'inp':
                inp(instrucion[1], int(num[numiterator]))
                numiterator += 1
            elif instrucion[0] == 'add':
                add(instrucion[1], instrucion[2])
            elif instrucion[0] == 'mul':
                mul(instrucion[1], instrucion[2])
            elif instrucion[0] == 'div':
                div(instrucion[1], instrucion[2])
            elif instrucion[0] == 'mod':
                mod(instrucion[1], instrucion[2])
            elif instrucion[0] == 'eql':
                eql(instrucion[1], instrucion[2])
        if dimensions['z'] == 0:
            return int(''.join(num))

def solution1(filename):
    with open(filename, 'r') as myfile:
        data = []
        for line in myfile:
            tmp = line.split(' ')
            for i in range(len(tmp)):
                tmp[i] = tmp[i].strip()
            data.append(tmp)
        
        
        return findmaxserialnumber(data)




def main():
    print(f'Result for data24 for task 1 is {solution1("Day_24/data24.txt")}')
    

if __name__ == '__main__':
    main()