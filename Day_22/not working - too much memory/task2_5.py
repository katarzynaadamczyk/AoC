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
        for cube in listofcubestocheckanddivide:
            
            if not checkifincube(cube, cubeoriginal):
                if checkifpartiallyincube(cube, cubeoriginal):
                    adddatax = divideoneaxe(cube[0], cube[1], cubeoriginal[0], cubeoriginal[1])
                    adddatay = divideoneaxe(cube[2], cube[3], cubeoriginal[2], cubeoriginal[3])
                    adddataz = divideoneaxe(cube[4], cube[5], cubeoriginal[4], cubeoriginal[5])
                    newlst, newret = lightenordarken(adddatax, adddatay, adddataz, cubeoriginal)
                    ret += newret
                    lst += newlst
                else:
                    ret.append(cube)
            
            
        listofcubestocheckanddivide = lst
    return ret


def addlights(newcube, cubeson):
    if len(cubeson) < 1:
        cubeson.append(newcube)
    else:
        listofcubestocheckanddivide = [newcube]
        for cubeoriginal in cubeson:
            lst = []
            for cubetodivide in listofcubestocheckanddivide:
                lst += dividecube(cubetodivide, cubeoriginal)
            listofcubestocheckanddivide = lst
        cubeson += listofcubestocheckanddivide
        
    return cubeson

# to do - remove lights that any of the cubes on have in common with data
def removelights(cubetodarken, cubeson):
    # TODO
    # zrobic, zeby po kazdej iteracji liczylo ile jeszcze jest tych overlapping i wtedy jeszcze raz zeby liczylo
    if len(cubeson) >= 1:
        listtodivide = [cubetodarken]
        changesmade = True
        while len(listtodivide) > 0 or not changesmade:
            newlsttodivide = []
            changesmade = False
            for cubetodarken in listtodivide:
                lst = []
                for cubetodivide in cubeson:
                    if checkifpartiallyincube(cubetodivide, cubetodarken):
                        lst += dividecube(cubetodivide, cubetodarken, False)
                        newlsttodivide += dividecube(cubetodarken, cubetodivide)
                        changesmade = True
            listtodivide = newlsttodivide
            
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
            if data[0] >= -50 and data[0] <= 50:    
                print(type)
                if type == 'on':
                    cubeson = addlights(data, cubeson)
                else:
                    cubeson = removelights(data, cubeson)
                
                
                print(countlights(cubeson))
                counti = 0
                for i in range(len(cubeson) - 1):
                    for j in range(i + 1, len(cubeson)):
                        if checkifpartiallyincube(cubeson[j], cubeson[i]):
                            counti += 1  
                print(f'overlapping: {counti} out of {len(cubeson)}')
            else:
                break   
        
            
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
        counti = 0
        for i in range(len(cubeson) - 1):
            for j in range(i + 1, len(cubeson)):
                if checkifpartiallyincube(cubeson[j], cubeson[i]):
                    counti += 1  
        print(f'overlapping: {counti} out of {len(cubeson)}')
        return countlights(cubeson)
        

def main():  
    
    print(f'Result for test data for task 1 is {solution1("Day_22/testdata.txt")} (should be 590784)')
    print(f'Result for data 22 for task 1 is {solution1("Day_22/data22.txt")} (should be 615869)')
    
    print(f'Result for test data for task 2 is {solution2("Day_22/testdata.txt")} (maybe 39769202357779)')
    print(f'Result for test data for task 2 is {solution2("Day_22/testdata2.txt")} (should be 2758514936282235)')
    print(f'Result for data 20 for task 2 is {solution2("Day_22/data22.txt")}')

if __name__ == '__main__':
    main()