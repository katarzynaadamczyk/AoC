# Katarzyna Adamczyk
# Solution to day 15 task 1 of Advent of Code 2021

def solution(filename):
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
        

def main():
    print(f'Result for test data for task 1 is {solution("Day_15/testdata.txt")}')
    print(f'Result for data 15 for task 1 is {solution("Day_15/data15.txt")}')

if __name__ == '__main__':
    main()