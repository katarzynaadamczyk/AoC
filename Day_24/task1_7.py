# Katarzyna Adamczyk
# Solution to day 24 task 1&2 of Advent of Code 2021



from copy import deepcopy


surelywrongsn = set() # level: z
digitsmaxtolow = [9, 8, 7, 6, 5, 4, 3, 2, 1]
digitslowtomax = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def inp(dimensions, a, val):
    dimensions[a] = val
    return dimensions
    
def add(dimensions, a, b):
    dimensions[a] += (dimensions[b] if b.isalpha() else int(b))
    return dimensions
    
def mul(dimensions,a, b):
    dimensions[a] *= (dimensions[b] if b.isalpha() else int(b))
    return dimensions
    
def div(dimensions,a, b):
    dimensions[a] //= (dimensions[b] if b.isalpha() else int(b))
    return dimensions
        
def mod(dimensions,a, b):
    dimensions[a] %= (dimensions[b] if b.isalpha() else int(b))
    return dimensions
    
def eql(dimensions,a, b):
    dimensions[a] = 1 if dimensions[a] == (dimensions[b] if b.isalpha() else int(b)) else 0
    return dimensions
    
def changedimensions(dimensions, data, level, value):
    for instrucion in data[level]:
        if instrucion[0] == 'inp':
            dimensions = inp(dimensions, instrucion[1], value)
        elif instrucion[0] == 'add':
            dimensions = add(dimensions, instrucion[1], instrucion[2])
        elif instrucion[0] == 'mul':
            dimensions = mul(dimensions, instrucion[1], instrucion[2])
        elif instrucion[0] == 'div':
            dimensions = div(dimensions, instrucion[1], instrucion[2])
        elif instrucion[0] == 'mod':
            dimensions = mod(dimensions, instrucion[1], instrucion[2])
        elif instrucion[0] == 'eql':
            dimensions = eql(dimensions, instrucion[1], instrucion[2])
    return dimensions


def findserialnumber(level, modelnumber, dimensions, digits, data):
    
    if (level, dimensions['z']) in surelywrongsn or level == 14:
        return None
    
    modelnumber *= 10
    originaldimensions = deepcopy(dimensions)
    
    for digit in range(len(digits)):
        if level == 0:
            print(digits[digit])
        dimensions = deepcopy(originaldimensions)
        dimensions = changedimensions(dimensions, data, level, digits[digit])
        
    
        if dimensions['z'] == 0 and level == 13:
            return modelnumber + digits[digit]
        newresult = findserialnumber(level + 1, modelnumber + digits[digit], dimensions, digits, data)
        if newresult is not None:
            return newresult
        
    surelywrongsn.add((level, dimensions['z']))
    return None
    

def solution1(filename):
    with open(filename, 'r') as myfile:
        data = []
        instructions = []
        for line in myfile:
            tmp = line.split(' ')
            for i in range(len(tmp)):
                tmp[i] = tmp[i].strip()
            if tmp[0] == 'inp':
                if len(instructions) > 0:
                    data.append(instructions)
                instructions = []
            instructions.append(tmp)
        data.append(instructions)
        
        dimensions = {}
        for char in 'xyzw':
            dimensions[char] = 0
        
        return findserialnumber(0, 0, dimensions, digitsmaxtolow, data)




def main():
    print(f'Result for data24 for task 1 is {solution1("Day_24/data24.txt")}')
    

if __name__ == '__main__':
    main()