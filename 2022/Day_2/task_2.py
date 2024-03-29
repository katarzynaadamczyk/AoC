'''
Advent of Code 
2022 day 2
my solution to tasks from day 2

solution 1 - Score is sum of (for each line add appriopriate - win, lose or dram and chosen hand - scissors, paper, rock). Options is a dict: {hand: score}
solution 2 - As above, options is a dict {result: [points, dict {hand_of_opponent: my_hand}}

'''

def solution_1(filename):
    data = []
    options = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
    winning_tuples = {('A', 'Y'), ('B', 'Z'), ('C', 'X'),}
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line.strip().split()
            data.append(tuple(line))
    act_sum = sum([options[x[1]] + (6 if x in winning_tuples else 3 if options[x[0]] == options[x[1]] else 0) for x in data])
    return act_sum

def solution_2(filename):
    act_sum = 0
    options = {'X': [0, {'A': 3, 'B': 1, 'C': 2}], 
               'Y': [3, {'A': 1, 'B': 2, 'C': 3}], 
               'Z': [6, {'A': 2, 'B': 3, 'C': 1}]}
    with open(filename, 'r') as myfile:
        for line in myfile:
            a, b = line.strip().split()
            act_sum += options[b][0] + options[b][1][a]
    return act_sum

    
def main():
    print('test 1:', solution_1('2022/Day_2/test_2.txt'))
    print('Solution 1:', solution_1('2022/Day_2/task_2.txt'))
    
    print('test 2:', solution_2('2022/Day_2/test_2.txt'))
    print('Solution 2:', solution_2('2022/Day_2/task_2.txt'))

if __name__ == '__main__':
    main()