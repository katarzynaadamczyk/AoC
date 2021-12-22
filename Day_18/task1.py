# Katarzyna Adamczyk
# Solution to day 16 task 1&2 of Advent of Code 2021

def solution1(filename):
    with open(filename, 'r') as myfile:
        line = myfile.readline()
        line = line.strip()
        nodes = preparetreeview(line) 
        return sumversions(nodes)
    
def solution2(filename):
    with open(filename, 'r') as myfile:
        line = myfile.readline()
        line = line.strip()
        nodes = preparetreeview(line) 
        return calculateexpressions(nodes)

def main():
    print(f'Result for test data for task 1 is {solution1("Day_18/testdata.txt")}')
    print(f'Result for data 15 for task 1 is {solution1("Day_18/data18.txt")}')

if __name__ == '__main__':
    main()