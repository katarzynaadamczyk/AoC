'''
Advent of Code 
2023 day 4
my solution to task 1 & 2

solution 1 - check if each number is in winning set, count winning numbers and then add 2 ** (count - 1) to result
solution 2 - 

'''

def solution_1(filename):
    act_sum = 0
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line[line.find(':') + 1:]
            line = line.split('|')
            winning_nums = set()
            for num in line[0].strip().split():
                winning_nums.add(int(num))
            act_count = 0
            for num in line[-1].strip().split():
                if int(num) in winning_nums:
                    act_count += 1
            if act_count > 0:
                act_sum += 2 ** (act_count - 1)

    return act_sum

def solution_2(filename):
    cards_count = {}
    winning_numbers = {}
    with open(filename, 'r') as myfile:
        for line in myfile:
            act_num = int(line[line.find(' ') + 1:line.find(':')])
            line = line[line.find(':') + 1:]
            line = line.split('|')
            winning_nums = set()
            for num in line[0].strip().split():
                winning_nums.add(int(num))
            act_count = 0
            for num in line[-1].strip().split():
                if int(num) in winning_nums:
                    act_count += 1
            cards_count.setdefault(act_num, 1)
            winning_numbers.setdefault(act_num, act_count)
    for act_num, act_count in winning_numbers.items():
        for i in range(1, act_count + 1):
            cards_count[act_num + i] = cards_count[act_num] + cards_count.get(act_num + i)
    return sum(cards_count.values())
    
    return 0

def main():
    print('test 1:', solution_1('2023/Day_4/test.txt'))
    print('Solution 1:', solution_1('2023/Day_4/task.txt'))
    
    print('test 2:', solution_2('2023/Day_4/test.txt'))
    print('Solution 2:', solution_2('2023/Day_4/task.txt'))

if __name__ == '__main__':
    main()
