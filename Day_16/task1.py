# Katarzyna Adamczyk
# Solution to day 16 task 1 of Advent of Code 2021


def count_versions(bits):
    pass

def solution(filename):
    with open(filename, 'r') as myfile:
        line = myfile.readline()
        line = line.strip()
        return count_versions(line)

def main():
    print(f'Result for test data for task 1 is {solution("Day_16/testdata1.txt")}')
    print(f'Result for test data for task 1 is {solution("Day_16/testdata2.txt")}')
    print(f'Result for test data for task 1 is {solution("Day_16/testdata3.txt")}')
    print(f'Result for test data for task 1 is {solution("Day_16/testdata4.txt")}')
    print(f'Result for data 15 for task 1 is {solution("Day_16/data16.txt")}')

if __name__ == '__main__':
    main()