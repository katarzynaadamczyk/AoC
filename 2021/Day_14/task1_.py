# Katarzyna Adamczyk
# Solution to day 14 task 1 of Advent of Code 2021

def pairinsertion(polymer, data):
    tmp = polymer[0]
    for i in range(len(polymer) - 1):
        tmp += data[polymer[i:i+2]] + polymer[i+1]
    return tmp
    
def countelements(polymer):
    result = {}
    for i in polymer:
        result.setdefault(i, 0)
        result[i] += 1
    result = sorted(result.values(), reverse=True)    
    return result[0] - result[-1]

def solution(filename):
    with open(filename, 'r') as myfile:
        data = {}
        polymer = myfile.readline().strip()
        print(polymer)
        for line in myfile:
            line = line.strip()
            if line != '':
                data[line[0:2]] = line[-1::]
        
        for i in range(10):
            polymer = pairinsertion(polymer, data)
        
        return countelements(polymer)
        
            
                    
        

def main():
    print(f'Result for test data is {solution("Day_14/testdata.txt")}')
    print(f'Result for data 14 is {solution("Day_14/data14.txt")}')

if __name__ == '__main__':
    main()