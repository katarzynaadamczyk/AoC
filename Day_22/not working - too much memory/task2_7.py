# Katarzyna Adamczyk
# Solution to day 22 task 1&2 of Advent of Code 2021

# not finished 
# I want to check if the next cube is in the previous ones and in such a way add them to result

def checkifincube(data, cube):
    if ((data[0] >= cube[0] and data[1] <= cube[1]) and (data[2] >= cube[2] and data[3] <= cube[3]) and (data[4] >= cube[4] and data[5] <= cube[5])):
        return True
    return False

def checkifpartiallyincube(data, cube):
    if ((data[0] >= cube[0] and data[0] <= cube[1]) or (data[1] >= cube[0] and data[1] <= cube[1])):
        if ((data[2] >= cube[2] and data[2] <= cube[3]) or (data[3] >= cube[2] and data[3] <= cube[3])):
            if ((data[4] >= cube[4] and data[4] <= cube[5]) or (data[5] >= cube[4] and data[5] <= cube[5])):
                return True
    return False


# divide one axe of the cube data
# check if data is within cube
def divideoneaxe(datamin, datamax, cubemin, cubemax):
    oneaxedata = []
    if datamin < cubemin:
        if datamax < cubemin:
            oneaxedata.append([datamin, datamax])
        else:
            oneaxedata.append([datamin, cubemin - 1])
            if datamax > cubemax:
                oneaxedata.append([cubemin, cubemax])
                oneaxedata.append([cubemax + 1, datamax])
            else:
                oneaxedata.append([cubemin, datamax])
    elif datamin <= cubemax and datamax > cubemax:
        oneaxedata.append([datamin, cubemax])
        oneaxedata.append([cubemax + 1, datamax])
    else:
        oneaxedata.append([datamin, datamax])
    
    return oneaxedata

def lightenordarken(adddatax, adddatay, adddataz, cubeoriginal):
    datatodivide = []
    datatoreturn = []
    for x in adddatax:
        for y in adddatay:
            for z in adddataz:
                xyz = [x[0], x[1], y[0], y[1], z[0], z[1]]
                if not checkifincube(xyz, cubeoriginal):
                    if checkifpartiallyincube(xyz, cubeoriginal):
                        datatodivide.append(xyz)
                    else:
                        datatoreturn.append(xyz)
    
    return datatodivide, datatoreturn


def dividecube(cubetodivide, cubeoriginal, iftolighten=True):
    listofcubestocheckanddivide = [cubetodivide]
    ret = []
    
    while len(listofcubestocheckanddivide) > 0:
        lst = []
       # ret2 = []
        for cube in listofcubestocheckanddivide:
            #if not checkifpartiallyincube(cube, cubeoriginal) and not checkifincube(cube, cubeoriginal):
            #    ret.append(cube)
          #  elif checkifpartiallyincube(cube, cubeoriginal) and not checkifincube(cube, cubeoriginal):
            #else:
           # if checkifpartiallyincube(cube, cubeoriginal):
                adddatax = divideoneaxe(cube[0], cube[1], cubeoriginal[0], cubeoriginal[1])
                adddatay = divideoneaxe(cube[2], cube[3], cubeoriginal[2], cubeoriginal[3])
                adddataz = divideoneaxe(cube[4], cube[5], cubeoriginal[4], cubeoriginal[5])
                newlst, newret = lightenordarken(adddatax, adddatay, adddataz, cubeoriginal)
                ret += newret
                lst += newlst
            #else:
             #   ret.append(cube)
            
            
        listofcubestocheckanddivide = lst
    # TODO
    # zamiast po prostu je dodac to sprawdzac sobie po kolei i dopiero dodac, bo to tutaj moim zdaniem tworza nam sie duplikaty
   # ret += ret2
    return ret


def addlights(newcube, cubeson):
    if len(cubeson) < 1:
        cubeson.append(newcube)
    else:
        listofcubestocheckanddivide = [newcube]
        changesmade = True
        while changesmade:
            changesmade = False
            for cubeoriginal in cubeson:
                lst = []
                for cubetodivide in listofcubestocheckanddivide:
                    if checkifpartiallyincube(cubetodivide, cubeoriginal):
                        lst += dividecube(cubetodivide, cubeoriginal)
                    else:
                        lst.append(cubetodivide)
                listofcubestocheckanddivide = lst
            cubetodel = []
            for i in range(len(listofcubestocheckanddivide) - 1):
                for j in range(i + 1, len(listofcubestocheckanddivide)):
                    if checkifpartiallyincube(listofcubestocheckanddivide[i], listofcubestocheckanddivide[j]):
                        changesmade = True
                        cubetodel.append([j, i])
            cubetodel2 = []
            for pair in cubetodel:
                listofcubestocheckanddivide += dividecube(listofcubestocheckanddivide[pair[0]], listofcubestocheckanddivide[pair[1]])
                cubetodel2.append(pair[0])
            for i in sorted(cubetodel2, reverse=True):
                listofcubestocheckanddivide.pop(i)
                
        cubeson += listofcubestocheckanddivide
        
    return cubeson


# to do - remove lights that any of the cubes on have in common with data
def removelights(cubetodarken, cubeson):
    if len(cubeson) > 1:
        lst = []
        for cubetodivide in cubeson:
            lst += dividecube(cubetodivide, cubetodarken, False)
        cubeson = lst
        
    return cubeson

def countlights(cubeson):
    cubes = 0
    
    for cube in cubeson:
        cubes += ((cube[1] + 1 - cube[0]) * (cube[3] + 1 - cube[2]) * (cube[5] + 1 - cube[4]))
    
    return cubes

def solution1(filename):
    with open(filename, 'r') as myfile:
        
        cubeson = []
        for line in myfile:    
            type = line[0:line.find(' ')]
            line = line[line.find(' ')::].strip()
            data = []
            for somerange in line.split(','):
                data.append(int(somerange[somerange.find('=')+1:somerange.find('.')]))
                data.append(int(somerange[somerange.rfind('.')+1::]))
            print(type)
            if data[0] >= -50 and data[0] <= 50:    
                if type == 'on':
                    cubeson = addlights(data, cubeson)
                else:
                    cubeson = removelights(data, cubeson)
            else:
                break 
            print(countlights(cubeson))
            counti = 0
            for i in range(len(cubeson) - 1):
                for j in range(i + 1, len(cubeson)):
                    if checkifpartiallyincube(cubeson[j], cubeson[i]):
                        counti += 1  
            print(f'overlapping: {counti} out of {len(cubeson)}')  
        
            
        return countlights(cubeson)


def solution2(filename):
    with open(filename, 'r') as myfile:
        
        cubeson = []
        i = 0
        for line in myfile:    
            type = line[0:line.find(' ')]
            line = line[line.find(' ')::].strip()
            data = []
            for somerange in line.split(','):
                data.append(int(somerange[somerange.find('=')+1:somerange.find('.')]))
                data.append(int(somerange[somerange.rfind('.')+1::]))  
            if type == 'on':
                cubeson = addlights(data, cubeson)
            else:
                cubeson = removelights(data, cubeson)
            i += 1
           # print(i)
        
        return countlights(cubeson)
        

def main():  
    
    print(f'Result for test data for task 1 is {solution1("Day_22/testdata.txt")} (should be 590784)')
    print(f'Result for data 22 for task 1 is {solution1("Day_22/data22.txt")} (should be 615869)')
    
    print(f'Result for test data for task 2 is {solution2("Day_22/testdata.txt")} (maybe 39769202357779)')
    print(f'Result for test data for task 2 is {solution2("Day_22/testdata2.txt")} (should be 2758514936282235)')
    print(f'Result for data 20 for task 2 is {solution2("Day_22/data22.txt")}')

if __name__ == '__main__':
    main()