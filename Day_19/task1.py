# Katarzyna Adamczyk
# Solution to day 18 task 1&2 of Advent of Code 2021

def transformation(point, num):
    if num == 0:
        return point
    if num == 1:
        return [point[0], point[1], -1 * point[2]]
    if num == 2:
        return [point[0], -1 * point[1], point[2]]
    if num == 3:
        return [point[0], -1 * point[1], -1 * point[2]]
    if num == 4:
        return [-1 * point[0], point[1], point[2]]
    if num == 5:
        return [-1 * point[0], point[1], -1 * point[2]]
    if num == 6:
        return [-1 * point[0], -1 * point[1], point[2]]
    if num == 7:
        return [-1 * point[0], -1 * point[1], -1 * point[2]]
    

def countuniquepoints(scannersdata):
    uniquepoints = set()
    for point in scannersdata[0]:
        uniquepoints.add(tuple(point))
    del scannersdata[0]
    while len(scannersdata) > 0:
        scannerstodelete = dict() # noofscanner: [ifortransformation, [diffvector]]
        for scanner in range(len(scannersdata)):
            for i in range(8):
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
        for key in sorted(list(scannerstodelete.keys()), reverse=True):
            for point in scannersdata[key]:
                # diffvector = scannerstodelete[key][1]
                # num = scannerstodelete[key][0]
                newpoint = transformation(point, scannerstodelete[key][0])
                newpoint = [newpoint[x] + scannerstodelete[key][1][x] for x in range(3)]
                uniquepoints.add(tuple(newpoint))
            del scannersdata[key]
        break
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


def main():
    print(f'Result for test data for task 1 is {solution1("Day_19/testdata.txt")}')
    print(f'Result for data 19 for task 1 is {solution1("Day_19/data19.txt")}')
    

if __name__ == '__main__':
    main()