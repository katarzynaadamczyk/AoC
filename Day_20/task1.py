# Katarzyna Adamczyk
# Solution to day 20 task 1 of Advent of Code 2021


def imageenhacement(image, decodedata):
    # copying the image 
    newimage = []
    for i in range(len(image)):
        tmp = []
        for j in range(len(image[i])):
            tmp.append(image[i][j])
        newimage.append(tmp)
    
    # working with the image enhacement algorithm
    for i in range(1, len(image) - 1):
        for j in range(1, len(image[i]) - 1):
            binarynum = ''
            for y in range(i-1, i + 2):
                for x in range(j - 1, j + 2):
                    binarynum += image[y][x]
            newimage[i][j] = '1' if decodedata[int(binarynum, 2)] == '#' else '0'
    
    if decodedata[0] == '#':
        for i in range(len(newimage[0])):
            if newimage[0][i] == '0':
                newimage[0][i] = '1'
            else:
                newimage[0][i] = '0'
            if newimage[-1][i] == '0':
                newimage[-1][i] = '1'
            else:
                newimage[-1][i] = '0'
        for i in range(1, len(newimage) - 1):
            if newimage[i][0] == '0':
                newimage[i][0] = '1'
            else:
                newimage[i][0] = '0'
            if newimage[i][-1] == '0':
                newimage[i][-1] = '1'
            else:
                newimage[i][-1] = '0'
                
    
    return newimage

def solution1(filename):
    with open(filename, 'r') as myfile:
        image = []
        decodedata = myfile.readline()
        
        # create image
        for line in myfile:    
            if len(line) > 1:
                line = line.strip()
                tmp = []
                for char in line:
                    if char == '#':
                        tmp.append('1')
                    else:
                        tmp.append('0')
                image.append(tmp)
        
        # add additional columns at the beginning and end of each line
        for i in range(len(image)):
            for j in range(5):
                image[i].insert(0, '0')
                image[i].append('0')
        
        # add additional rows at beginning and at the end of image
        tmp = []
        for j in range(len(image[0])):
            tmp.append('0')
        for i in range(5):
            image.insert(0, tmp.copy())
            image.append(tmp.copy())
        
        image = imageenhacement(image, decodedata)
        image = imageenhacement(image, decodedata)   
        
        lightenedup = 0
        for line in image:
            for char in line:
                if char == '1':
                    lightenedup += 1
        
        return lightenedup


def solution2(filename):
    with open(filename, 'r') as myfile:
        image = []
        decodedata = myfile.readline()
        
        # create image
        for line in myfile:    
            if len(line) > 1:
                line = line.strip()
                tmp = []
                for char in line:
                    if char == '#':
                        tmp.append('1')
                    else:
                        tmp.append('0')
                image.append(tmp)
        
        # add additional columns at the beginning and end of each line
        for i in range(len(image)):
            for j in range(60):
                image[i].insert(0, '0')
                image[i].append('0')
        
        # add additional rows at beginning and at the end of image
        tmp = []
        for j in range(len(image[0])):
            tmp.append('0')
        for i in range(60):
            image.insert(0, tmp.copy())
            image.append(tmp.copy())
        
        for i in range(50):
            image = imageenhacement(image, decodedata)   
        
        lightenedup = 0
        for line in image:
            for char in line:
                if char == '1':
                    lightenedup += 1
        
        return lightenedup

def main():
    print(f'Result for test data for task 1 is {solution1("Day_20/testdata.txt")}')
    print(f'Result for data 20 for task 1 is {solution1("Day_20/data20.txt")}')
    
    print(f'Result for test data for task 2 is {solution2("Day_20/testdata.txt")}')
    print(f'Result for data 20 for task 2 is {solution2("Day_20/data20.txt")}')
    

if __name__ == '__main__':
    main()