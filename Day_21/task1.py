# Katarzyna Adamczyk
# Solution to day 21 task 1 of Advent of Code 2021


def rolldice(lastroll):
    return [lastroll + i if lastroll + i <= 100 else (lastroll + i) % 100 for i in range(1, 4)]

def makeamove(position, result, lastroll):
    dice = rolldice(lastroll)
    position += sum(dice)
    while position > 10:
        position -= 10
    result += position
    return position, result, dice[-1]

def playagame(player1startingposition, player2startingposition):
    player1result = 0
    player1position = player1startingposition
    player2result = 0
    player2position = player2startingposition
    
    whoplays = True
    dietimesrolled = 0
    lastroll = 0
    
    while player1result < 1000 and player2result < 1000:
        if whoplays:
            player1position, player1result, lastroll = makeamove(player1position, player1result, lastroll)
            whoplays = False
        else:
            player2position, player2result, lastroll = makeamove(player2position, player2result, lastroll)
            whoplays = True
        dietimesrolled += 3
    
    return min(player1result, player2result) * dietimesrolled
    

def solution1(filename):
    with open(filename, 'r') as myfile:
        line1 = myfile.readline().strip()
        line2 = myfile.readline().strip()
        
        player1startingposition = int(line1[line1.find(':')+1::])
        player2startingposition = int(line2[line2.find(':')+1::])
        
        return playagame(player1startingposition, player2startingposition)


def main():
    print(f'Result for test data for task 1 is {solution1("Day_21/testdata.txt")}')
    print(f'Result for data 21 for task 1 is {solution1("Day_21/data21.txt")}')
    
    

if __name__ == '__main__':
    main()