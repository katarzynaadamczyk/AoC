'''
Advent of Code 
2022 day 6
my solution to tasks from day 6

solution 1 - 
solution 2 - 

'''


def solution_1(filename):
    markers = []
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line.strip()
            start = 0
            for ending in range(4, len(line)):
                if len(set([char for char in line[start:ending]])) == 4:
                    markers.append(ending)
                    break
                start += 1
    return markers


    
def main():
    print('test 1:', solution_1('2022/Day_6/test.txt'))
    print('Solution 1:', solution_1('2022/Day_6/task.txt'))
    
    

if __name__ == '__main__':
    main()
    