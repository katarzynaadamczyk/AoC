# Katarzyna Adamczyk
# Solution to day 22 task 1&2 of Advent of Code 2021
# with help from Reddit forum 


from dis import Instruction


def getinstructions(filename):
    with open(filename, 'r') as myfile:
        instructions = []
        for line in myfile:    
            type = line[0:line.find(' ')]
            line = line[line.find(' ')::].strip()
            data = []
            for somerange in line.split(','):
                data.append(int(somerange[somerange.find('=')+1:somerange.find('.')]))
                data.append(int(somerange[somerange.rfind('.')+1::]))
            data.append(-1 if type == 'off' else 1)
            instructions.append(data)
        return instructions

def checkifpartiallyincube(cube1, cube2):
    if not(cube1[0] <= cube2[1] and cube1[1] >= cube2[0]):
        return False
 
    if not(cube1[2] <= cube2[3] and cube1[3] >= cube2[2]):
        return False
 
    if not(cube1[4] <= cube2[5] and cube1[5] >= cube2[4]):
        return False
 
    return True
 
def getintersection(cube1, cube2):
    min_x = max(cube1[0], cube2[0])
    max_x = min(cube1[1], cube2[1])
 
    min_y = max(cube1[2], cube2[2])
    max_y = min(cube1[3], cube2[3])
 
    min_z = max(cube1[4], cube2[4])
    max_z = min(cube1[5], cube2[5])
 
    if cube1[6] == cube2[6]:
        sign = -cube1[6]
    elif cube1[6] == 1 and cube2[6] == -1:
        sign = 1
    else:
        sign = cube1[6] * cube2[6]
 
    return [min_x, max_x, min_y, max_y, min_z, max_z, sign]
 
 
def countlights(cubeson):
    cubes = 0
    
    for cube in cubeson:
        cubes += ((cube[1] + 1 - cube[0]) * (cube[3] + 1 - cube[2]) * (cube[5] + 1 - cube[4]) * cube[6])
    
    return cubes

def solution1(filename):
    cuboids = []
    
    instructions = getinstructions(filename)
    for cube in instructions:
        
        if cube[0] < -50 or cube[0] > 50 or cube[1] < -50 or cube[1] > 50 or cube[2] < -50 or cube[2] > 50 or cube[3] < -50 or cube[3] > 50:
            print('>50')
            break
        
        intersections = []
 
        for cuboid in cuboids:
            if checkifpartiallyincube(cube, cuboid):
                intersection = getintersection(cube, cuboid)
                intersections.append(intersection)
 
        for intersection in intersections:
            cuboids.append(intersection)
 
        if cube[6] == 1:
            cuboids.append(cube)
 
    return countlights(cuboids)


def solution2(filename):
    cuboids = []
    instructions = getinstructions(filename)
 
    for cube in instructions:
        
        intersections = []
 
        for cuboid in cuboids:
            if checkifpartiallyincube(cube, cuboid):
                intersection = getintersection(cube, cuboid)
                intersections.append(intersection)
 
        for intersection in intersections:
            cuboids.append(intersection)
 
        if cube[6] == 1:
            cuboids.append(cube)
 
    return countlights(cuboids)

    
def main():  
    
    
    
    print(f'Result for test data for task 1 is {solution1("Day_22/testdata.txt")} (should be 590784)')
    print(f'Result for data 22 for task 1 is {solution1("Day_22/data22.txt")} (should be 615869)')
    
    print(f'Result for test data for task 2 is {solution2("Day_22/testdata.txt")} (maybe 39769202357779)')
    print(f'Result for test data for task 2 is {solution2("Day_22/testdata2.txt")} (should be 2758514936282235)')
    print(f'Result for data 20 for task 2 is {solution2("Day_22/data22.txt")}')

if __name__ == '__main__':
    main()