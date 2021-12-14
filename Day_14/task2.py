# Katarzyna Adamczyk
# Solution to day 14 task 1&2 of Advent of Code 2021

def pairinsertion(polymer, data):
    tmp = {}
    for key in polymer.keys():
        tmp.setdefault(key[0] + data[key], 0)
        tmp.setdefault(data[key] + key[1], 0)
        tmp[key[0] + data[key]] += polymer[key]
        tmp[data[key] + key[1]] += polymer[key]
    return tmp
    
def countelements(polymer, start):
    result = {}
    for key in polymer:
        result.setdefault(key[0], 0)
        result[key[0]] += polymer[key]
    result[start[-1]] += 1
    result = sorted(result.values(), reverse=True)    
    return result[0] - result[-1]

def solution(filename, quantity):
    with open(filename, 'r') as myfile:
        data = {}
        polymer = {} 
        tmp = myfile.readline().strip()
        for i in range(len(tmp) - 1):
            polymer.setdefault(tmp[i:i+2], 0)
            polymer[tmp[i:i+2]] += 1
        for line in myfile:
            line = line.strip()
            if line != '':
                data[line[0:2]] = line[-1::]
        
        for i in range(quantity):
            polymer = pairinsertion(polymer, data)
        
        return countelements(polymer, tmp)
        
            
                    
        

def main():
    print(f'Result for test data for task 1 is {solution("Day_14/testdata.txt", 10)}')
    print(f'Result for data 14 for task 1 is {solution("Day_14/data14.txt", 10)}')
    print(f'Result for data 14 for task 2 is {solution("Day_14/data14.txt", 40)}')

if __name__ == '__main__':
    main()