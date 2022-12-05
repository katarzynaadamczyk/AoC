'''
Advent of Code 
2022 day 5
my solution to tasks from day 5

solution 1 - make a list of stacks and list of dicts of commands. Then follow the commands and move appropriate number of crates from apprpriate stack.
solution 2 - as above, the difference is in moving the crates.

'''

def make_stacks(filename_stack):
    stacks = [[] for _ in range(9)]
    with open(filename_stack, 'r') as myfile:
        for line in myfile:
            line = line.strip('\n')
            for index, elem in enumerate([line[i:i+4] for i in range(0, len(line), 4)]):
                if '[' in elem:
                    stacks[index].append(elem.strip('[] '))
    for index in range(len(stacks)):
        stacks[index].reverse()
    return stacks


def get_moves(filename_moves):
    moves = []
    with open(filename_moves, 'r') as myfile:
        for line in myfile:
            line = line.strip().split()
            act_dict = {}
            for index in range(0, len(line), 2):
                act_dict.setdefault(line[index], int(line[index + 1]))
            moves.append(act_dict)
    return moves


def solution_1(filename_stack, filename_moves):
    stacks = make_stacks(filename_stack)
    moves = get_moves(filename_moves)
    for move in moves:
        for _ in range(move['move']):
            value = stacks[move['from'] - 1].pop()
            stacks[move['to'] - 1].append(value)
    return ''.join([stack[-1] if len(stack) else ' ' for stack in stacks])

def solution_2(filename_stack, filename_moves):
    stacks = make_stacks(filename_stack)
    moves = get_moves(filename_moves)
    for move in moves:
        last_elems_indexes = len(stacks[move['from'] - 1]) - move['move']
        stacks[move['to'] - 1] = stacks[move['to'] - 1] + stacks[move['from'] - 1][last_elems_indexes:]
        stacks[move['from'] - 1] = stacks[move['from'] - 1][:last_elems_indexes]
    return ''.join([stack[-1] if len(stack) else ' ' for stack in stacks])
    
def main():
    print('test 1:', solution_1('2022/Day_5/test_stacks.txt', '2022/Day_5/test_moves.txt'))
    print('Solution 1:', solution_1('2022/Day_5/task_stacks.txt', '2022/Day_5/task_moves.txt'))
    
    
    print('test 2:', solution_2('2022/Day_5/test_stacks.txt', '2022/Day_5/test_moves.txt'))
    print('Solution 2:', solution_2('2022/Day_5/task_stacks.txt', '2022/Day_5/task_moves.txt'))

if __name__ == '__main__':
    main()
    