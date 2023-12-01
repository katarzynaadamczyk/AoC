'''
Advent of Code 
2023 day 1
my solution to task 1 

solution 1 - 
solution 2 - 

'''
import re

nums = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', 
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

def solution_1(filename):
    data = []
    with open(filename, 'r') as myfile:
        for line in myfile:
            tmp = re.findall('\d', line)
            data.append(int(tmp[0] + tmp[-1]))
    return sum(data)

def solution_2(filename):
    data = []
    pattern = '|'.join(nums.keys())
    with open(filename, 'r') as myfile:
        for line in myfile:
            tmp = [[len(line), ''], [0, '']]
            for key in nums.keys():
                index = line.find(key)
                rindex = line.rfind(key)
              #  print(index)
             #   print(rindex)
                if index != -1 and tmp[0][0] >= index:
                    tmp[0][0] = index
                    tmp[0][1] = key
                if rindex != -1 and tmp[1][0] <= rindex:
                    tmp[1][0] = rindex
                    tmp[1][1] = key
            print(line)
            print(tmp)
            data.append(int(nums[tmp[0][1]] + nums[tmp[1][1]]))
    return sum(data)

def main():
    print('test 1:', solution_1('2023/Day_1/test_1.txt'))
    print('Solution 1:', solution_1('2023/Day_1/task_1.txt'))
    
    print('test 2:', solution_2('2023/Day_1/test_2.txt'))
    print('Solution 2:', solution_2('2023/Day_1/task_1.txt'))

if __name__ == '__main__':
    main()