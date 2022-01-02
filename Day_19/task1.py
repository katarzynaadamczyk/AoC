# Katarzyna Adamczyk
# Solution to day 19 task 1 of Advent of Code 2021

transformation_table = [
                        [[0, 1, 2], [1, 1, 1]],
                        [[0, 1, 2], [-1, 1, 1]],
                        [[0, 1, 2], [1, -1, 1]],
                        [[0, 1, 2], [1, 1, -1]],
                        [[0, 1, 2], [-1, -1, 1]],
                        [[0, 1, 2], [-1, 1, -1]],
                        [[0, 1, 2], [1, -1, -1]],
                        [[0, 1, 2], [-1, -1, -1]],
            
                        [[2, 1, 0], [1, 1, 1]],
                        [[2, 1, 0], [-1, 1, 1]],
                        [[2, 1, 0], [1, -1, 1]],
                        [[2, 1, 0], [1, 1, -1]],
                        [[2, 1, 0], [-1, -1, 1]],
                        [[2, 1, 0], [-1, 1, -1]],
                        [[2, 1, 0], [1, -1, -1]],
                        [[2, 1, 0], [-1, -1, -1]],
                        
                        [[0, 2, 1], [1, 1, 1]],
                        [[0, 2, 1], [-1, 1, 1]],
                        [[0, 2, 1], [1, -1, 1]],
                        [[0, 2, 1], [1, 1, -1]],
                        [[0, 2, 1], [-1, -1, 1]],
                        [[0, 2, 1], [-1, 1, -1]],
                        [[0, 2, 1], [1, -1, -1]],
                        [[0, 2, 1], [-1, -1, -1]],
                        
                        [[1, 0, 2], [1, 1, 1]],
                        [[1, 0, 2], [-1, 1, 1]],
                        [[1, 0, 2], [1, -1, 1]],
                        [[1, 0, 2], [1, 1, -1]],
                        [[1, 0, 2], [-1, -1, 1]],
                        [[1, 0, 2], [-1, 1, -1]],
                        [[1, 0, 2], [1, -1, -1]],
                        [[1, 0, 2], [-1, -1, -1]],
                        
                        [[1, 2, 0], [1, 1, 1]],
                        [[1, 2, 0], [-1, 1, 1]],
                        [[1, 2, 0], [1, -1, 1]],
                        [[1, 2, 0], [1, 1, -1]],
                        [[1, 2, 0], [-1, -1, 1]],
                        [[1, 2, 0], [-1, 1, -1]],
                        [[1, 2, 0], [1, -1, -1]],
                        [[1, 2, 0], [-1, -1, -1]],
                        
                        [[2, 0, 1], [1, 1, 1]],
                        [[2, 0, 1], [-1, 1, 1]],
                        [[2, 0, 1], [1, -1, 1]],
                        [[2, 0, 1], [1, 1, -1]],
                        [[2, 0, 1], [-1, -1, 1]],
                        [[2, 0, 1], [-1, 1, -1]],
                        [[2, 0, 1], [1, -1, -1]],
                        [[2, 0, 1], [-1, -1, -1]],
                        ]


def transformation(point, num):
    return [point[transformation_table[num][0][x]] * transformation_table[num][1][x] for x in range(3)]

def countuniquepoints(scannersdata):
    uniquepoints = set()
    for point in scannersdata[0]:
        uniquepoints.add(tuple(point))
    del scannersdata[0]
    changesmade = 1
    while len(scannersdata) > 0 and changesmade > 0:
        scannerstodelete = dict() # noofscanner: [ifortransformation, [diffvector]]
        changesmade = 0
        for scanner in range(len(scannersdata)):
            for i in range(len(transformation_table)):
                howmanydiffer = dict()
                for point in uniquepoints:
                    for scannerpoint in scannersdata[scanner]:
                        newscannerpoint = transformation(scannerpoint, i)
                        diffvector = [point[x] - newscannerpoint[x] for x in range(3)]
                        howmanydiffer.setdefault(tuple(diffvector), 0)
                        howmanydiffer[tuple(diffvector)] += 1
                if max(list(howmanydiffer.values())) >= 12:
                    for key, value in howmanydiffer.items():
                        if value >= 12:
                            diffvector = key
                            break
                    scannerstodelete.setdefault(scanner, [i, diffvector])
                    changesmade += 1
                    break
        for key in sorted(list(scannerstodelete.keys()), reverse=True):
            print(f'delete key = {key}')
            print(f'num = {scannerstodelete[key][0]}')
            for point in scannersdata[key]:
                # diffvector = scannerstodelete[key][1]
                # num = scannerstodelete[key][0]
                newpoint = transformation(point, scannerstodelete[key][0])
                newpoint = [newpoint[x] + scannerstodelete[key][1][x] for x in range(3)]
                uniquepoints.add(tuple(newpoint))
            del scannersdata[key]

    print(len(scannersdata))
    return len(uniquepoints)

def solution1(filename):
    with open(filename, 'r') as myfile:
        scannersdata = []
        tmp = []
        for line in myfile:    
            if len(line) > 1:
                if 'scanner' in line:
                    tmp = []
                elif line[0].isdecimal() or line[0] == '-':
                    tmp.append([int(x) for x in line.strip().split(',')])
            else:
                scannersdata.append(tmp)
        scannersdata.append(tmp)
        
        return countuniquepoints(scannersdata)
    
def solution2(filename):
    with open(filename, 'r') as myfile:
        scannersdata = []
        tmp = []
        for line in myfile:    
            if len(line) > 1:
                if 'scanner' in line:
                    tmp = []
                elif line[0].isdecimal() or line[0] == '-':
                    tmp.append([int(x) for x in line.strip().split(',')])
            else:
                scannersdata.append(tmp)
        scannersdata.append(tmp)
        
        return countmanhattandistance(scannersdata)


def main():
    print(f'Result for test data for task 1 is {solution1("Day_19/testdata.txt")}')
    print(f'Result for data 19 for task 1 is {solution1("Day_19/data19.txt")}')
    
    print(f'Result for test data for task 2 is {solution2("Day_19/testdata.txt")}')
    print(f'Result for data 19 for task 2 is {solution2("Day_19/data19.txt")}')
    

if __name__ == '__main__':
    main()