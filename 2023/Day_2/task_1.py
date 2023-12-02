'''
Advent of Code 
2023 day 2
my solution to task 1 & 2

solution 1 - 
solution 2 - 

'''

def solution_1(filename):
    games_sum = 0
    cubes = {'red': 12, 'green': 13, 'blue': 14}
    with open(filename, 'r') as myfile:
        for line in myfile:
            act_game_num = int(line[line.find(' ') + 1: line.find(':')])
            line = line[line.find(':') + 1:].strip()
            games = line.split(';')
            add = True
            for game in games:
                act_game = game.split(',')
                for color in act_game:
                    act_color = color.strip().split()
                    if int(act_color[0]) > cubes.get(act_color[1], 0):
                        add = False
                        break
                if not add:
                    break
            if add:
                games_sum += act_game_num
    return games_sum
'''
def solution_2(filename):
    data = []
    with open(filename, 'r') as myfile:
        for line in myfile:
            tmp = [[len(line), ''], [0, '']]
            for key in nums.keys():
                index = line.find(key)
                rindex = line.rfind(key)
                if index != -1 and tmp[0][0] >= index:
                    tmp[0][0] = index
                    tmp[0][1] = key
                if rindex != -1 and tmp[1][0] <= rindex:
                    tmp[1][0] = rindex
                    tmp[1][1] = key
            data.append(int(nums[tmp[0][1]] + nums[tmp[1][1]]))
    return sum(data)
'''
def main():
    print('test 1:', solution_1('2023/Day_2/test_1.txt'))
    print('Solution 1:', solution_1('2023/Day_2/task_1.txt'))
    
   # print('test 2:', solution_2('2023/Day_1/test_2.txt'))
  #  print('Solution 2:', solution_2('2023/Day_1/task_1.txt'))

if __name__ == '__main__':
    main()
