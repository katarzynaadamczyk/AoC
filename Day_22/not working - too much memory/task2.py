# Katarzyna Adamczyk
# Solution to day 22 task 1 of Advent of Code 2021

from itertools import product

def checkifincube(data, cube):
    if ((data[0] >= cube[0] and data[1] <= cube[1]) and (data[2] >= cube[2] and data[3] <= cube[3]) and (data[4] >= cube[4] and data[5] <= cube[5])):
        return True
    return False

def darkenononeaxe(datamin, datamax, cubemin, cubemax):
    oneaxedata = []
    if datamin > cubemin:
        oneaxedata.append([cubemin, datamin - 1])
        if datamax < cubemax:
            oneaxedata.append([datamin, datamax])
            oneaxedata.append([datamax + 1, cubemax])
        else:
            oneaxedata.append([datamin + 1, cubemax])
    elif datamax < cubemax:
        oneaxedata.append([cubemin, datamax])
        oneaxedata.append([datamax + 1, cubemax])
    else:
        oneaxedata.append([cubemin, cubemax])
    
    return oneaxedata

def darken(data, cube):
    darkendatax = darkenononeaxe(data[0], data[1], cube[0], cube[1])
    darkendatay = darkenononeaxe(data[2], data[3], cube[2], cube[3])
    darkendataz = darkenononeaxe(data[4], data[5], cube[4], cube[5])
    
    # zrobic analogicznie do lighten tylko, że sprawdzać czy wynikowy cube jest w data 
    darkendata = []
    for x in darkendatax:
        for y in darkendatay:
            for z in darkendataz:
                xyz = [x[0], x[1], y[0], y[1], z[0], z[1]]
                if not checkifincube(xyz, data):
                    darkendata.append(xyz)
    return darkendata

def darkencubes(data, cubeson):
    actcubeson = []
    
    for cube in cubeson: 
        if (data[0] >= cube[0] and data[0] <= cube[1]) or (data[1] >= cube[0] and data[1] <= cube[1]):
            if (data[2] >= cube[2] and data[2] <= cube[3]) or (data[3] >= cube[2] and data[3] <= cube[3]):
                if (data[4] >= cube[4] and data[4] <= cube[5]) or (data[5] >= cube[4] and data[5] <= cube[5]):
                    adddata = darken(data, cube)
                    for cubiq in adddata:
                        actcubeson.append(cubiq)
                else:
                    actcubeson.append(cube)
            else:
                actcubeson.append(cube)
        else:
            actcubeson.append(cube)
    
    return actcubeson

def lightenoneaxe(datamin, datamax, cubemin, cubemax):
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

def lighten(data, cube):
    adddatax = lightenoneaxe(data[0], data[1], cube[0], cube[1])
    adddatay = lightenoneaxe(data[2], data[3], cube[2], cube[3])
    adddataz = lightenoneaxe(data[4], data[5], cube[4], cube[5])
    
    adddata = []
    
    for x in adddatax:
        for y in adddatay:
            for z in adddataz:
                xyz = [x[0], x[1], y[0], y[1], z[0], z[1]]
                if not checkifincube(xyz, cube):
                    adddata.append(xyz)
    
    return adddata

def lightencubes(data, cubeson):
    actcubeson = []
    if len(cubeson) == 0:
        cubeson.append(data)
    else:
        datainanycube = False
        for cube in cubeson:
            if checkifincube(data, cube):
                datainanycube = True
                continue
            # na razie usunelam znaki rownosci bo one nie powinny miec znaczenia przy zaswiecaniu
            if (data[0] > cube[0] and data[0] < cube[1]) or (data[1] > cube[0] and data[1] < cube[1]):
                if (data[2] > cube[2] and data[2] < cube[3]) or (data[3] > cube[2] and data[3] < cube[3]):
                    if (data[4] > cube[4] and data[4] < cube[5]) or (data[5] > cube[4] and data[5] < cube[5]):
                        adddata = lighten(data, cube)
                        for cubiq in adddata:
                            actcubeson.append(cubiq)
        
        for cube in actcubeson:
            cubeson.append(cube)
        
        if len(actcubeson) == 0 and not datainanycube:
            cubeson.append(data)
        
        
            
    return cubeson

def countcubes(cubeson):
    cubes = 0
    
    for cube in cubeson:
      #  cubes += ((cube[1] - cube[0]) * (cube[3] - cube[2]) * (cube[5] - cube[4])) # don't know if there will be need to add 1
        cubes += ((cube[1] + 1 - cube[0]) * (cube[3] + 1 - cube[2]) * (cube[5] + 1 - cube[4]))
    
    return cubes

def returnresult(cubeson): # working here, need to check intersections for each set
    cubesonset = set()
    #print(len(cubeson))
    for cube in cubeson:
        cubesonset.add(tuple(cube))  
    #print(len(cubesonset))
    cubesonset = list(cubesonset)
    tuplestoremove = set()
    for i in range(len(cubesonset) - 1):
        for j in range(i + 1, len(cubesonset)):
            if checkifincube(cubesonset[i], cubesonset[j]):
                tuplestoremove.add(cubesonset[i])
   # print(len(tuplestoremove))
    for t in tuplestoremove:
        cubesonset.remove(t)
    #print(len(cubesonset))
    #print(cubesonset)
    return countcubes(cubesonset)

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
                if type == 'on':
                    cubeson = lightencubes(data, cubeson)
                else:
                    cubeson = darkencubes(data, cubeson)
            else:
                break   
            
        return returnresult(cubeson)


def solution2(filename):
    with open(filename, 'r') as myfile:
        
        cubeson = []
        for line in myfile:    
            type = line[0:line.find(' ')]
            line = line[line.find(' ')::].strip()
            data = []
            for somerange in line.split(','):
                data.append(int(somerange[somerange.find('=')+1:somerange.find('.')]))
                data.append(int(somerange[somerange.rfind('.')+1::]))  
            if type == 'on':
                cubeson = lightencubes(data, cubeson)
            else:
                cubeson = darkencubes(data, cubeson)  
        
        return returnresult(cubeson)
        

def main():
    print(f'Result for test data for task 1 is {solution1("Day_22/testdata.txt")} (should be 590784)')
    print(f'Result for data 22 for task 1 is {solution1("Day_22/data22.txt")} (should be 615869)')
    
    print(f'Result for test data for task 2 is {solution2("Day_22/testdata.txt")}')
    print(f'Result for test data for task 2 is {solution2("Day_22/testdata2.txt")} (should be 2758514936282235)')
    print(f'Result for data 20 for task 2 is {solution2("Day_22/data22.txt")}')

if __name__ == '__main__':
    main()