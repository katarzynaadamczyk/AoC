# Katarzyna Adamczyk
# Solution to day 19 task 1 of Advent of Code 2021

def transformation(point, num):
    if num == 0:
        return point
    if num == 1:
        return [-1 * point[1], point[0], point[2]]
    if num == 2:
        return [-1 * point[0], -1 * point[1], point[2]]
    if num == 3:
        return [point[1], -1 * point[0], point[2]]
    if num == 4:
        return [point[0], point[1], -1 * point[2]]
    if num == 5:
        return [-1 * point[1], point[0], -1 * point[2]]
    if num == 6:
        return [-1 * point[0], -1 * point[1], -1 * point[2]]
    if num == 7:
        return [point[1], -1 * point[0], -1 * point[2]]
    if num == 8:
        return [point[2], point[1], point[0]]
    if num == 9:
        return [-1 * point[2], point[1], point[0]]
    if num == 10:
        return [-1 * point[0], point[1], -1 * point[2]]
    if num == 11:
        return [point[2], point[1], -1 * point[0]]
    if num == 12:
        return [point[0], point[2], -1 * point[1]]
    if num == 13:
        return [-1 * point[2], point[0], -1 * point[1]]
    if num == 14:
        return [-1 * point[0], -1 * point[2], -1 * point[1]]
    if num == 15:
        return [point[2], -1 * point[0], -1 * point[1]]
    

def countuniquepoints(scannersdata):
    uniquepoints = set()
    for point in scannersdata[0]:
        uniquepoints.add(tuple(point))
    del scannersdata[0]
    counti = len(scannersdata)
    while len(scannersdata) > 0 and counti > 0:
        scannerstodelete = dict() # noofscanner: [ifortransformation, [diffvector]]
        for scanner in range(len(scannersdata)):
            for i in range(12):
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
                    break
        for key in sorted(list(scannerstodelete.keys()), reverse=True):
            for point in scannersdata[key]:
                # diffvector = scannerstodelete[key][1]
                # num = scannerstodelete[key][0]
                newpoint = transformation(point, scannerstodelete[key][0])
                newpoint = [newpoint[x] + scannerstodelete[key][1][x] for x in range(3)]
                uniquepoints.add(tuple(newpoint))
            del scannersdata[key]
        counti -= 1
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