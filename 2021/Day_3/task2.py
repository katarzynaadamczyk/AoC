def gettherating(data, key):
    indexes = [x for x in range(len(data))]
    for i in range(len(data[0])):
        count1 = 0
        count0 = 0
        for j in indexes:
            if data[j][i] == '1':
                count1 += 1
            else:
                count0 += 1
        if key == 'o':
            if count1 >= count0:
                key2 = '1'
            else:
                key2 = '0'
        else:
            if count0 <= count1:
                key2 = '0'
            else:
                key2 = '1'
        tmp = []
        for j in indexes:
            if data[j][i] == key2:
                tmp.append(j)
        indexes = tmp
        if len(indexes) == 1:
            break
    return data[indexes[0]]
            


def main():
    myfile = open('Day_3/data3.txt', 'r')
    data = []
    for i in myfile:
        data.append(i)
    myfile.close()
    
    oxygenrating = gettherating(data, 'o')
    co2rating = gettherating(data, 'c')
    print(f'oxygenrating: {oxygenrating}, {int(oxygenrating, 2)}')
    print(f'co2rating: {co2rating}, {int(co2rating, 2)}')
    print(f'result: {int(co2rating, 2) * int(oxygenrating, 2)}')
    
    

if __name__ == '__main__':
    main()