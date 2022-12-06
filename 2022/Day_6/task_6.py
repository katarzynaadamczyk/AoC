'''
Advent of Code 
2022 day 6
my solution to tasks from day 6

solution 1 & 2 - get chunks of given size (4 or 14), transform its characters into a set and check whether this set is of given size length. If so, then the ending is the answer.

'''


def solution_1(filename, no_of_characters):
    markers = []
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line.strip()
            start = 0
            for ending in range(no_of_characters, len(line)):
                if len(set([char for char in line[start:ending]])) == no_of_characters:
                    markers.append(ending)
                    break
                start += 1
    return markers

    
def main():
    print('test 1:', solution_1('2022/Day_6/test.txt', 4))
    print('Solution 1:', solution_1('2022/Day_6/task.txt', 4))
    
    print('test 2:', solution_1('2022/Day_6/test.txt', 14))
    print('Solution 2:', solution_1('2022/Day_6/task.txt', 14))
    

if __name__ == '__main__':
    main()
    