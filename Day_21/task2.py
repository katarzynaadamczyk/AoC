# Katarzyna Adamczyk
# Solution to day 21 task 2 of Advent of Code 2021

from itertools import product

def makeamove(result, whoplays):
    # result - dictionary with key as tuple 
    # (positionplayer1, resultplayer1, positionplayer2, resultplayer2): numberofuniverses
    # whoplays if True player 1, player 2 otherwise
    newresult = dict()
    for dice in product([1, 2, 3], repeat=3):
        for key in result:
            
            actualposition = (key[0] if whoplays else key[2]) + sum(dice) 
            
            while actualposition > 10:
                actualposition -= 10
            
            actualresult = (key[1] if whoplays else key[3]) + actualposition
            
            if whoplays:
                newkey = (actualposition, actualresult, key[2], key[3])
            else:
                newkey = (key[0], key[1], actualposition, actualresult)
            
            newresult.setdefault(newkey, 0)
            newresult[newkey] += result[key]
    

    return newresult

def playagame(player1startingposition, player2startingposition):
    playersresult = {(player1startingposition, 0, player2startingposition, 0): 1}
    player1universes = 0
    player2universes = 0
    
    whoplays = True
    
    while len(playersresult) > 0:
        keystodelete = []
        playersresult = makeamove(playersresult, whoplays)
        whoplays = not whoplays
        
        for key in playersresult:
            if key[1] >= 21 or key[3] >= 21:
                keystodelete.append(key)
                if key[1] >= 21:
                    player1universes += playersresult[key]
                else:
                    player2universes += playersresult[key]
                    
        for key in keystodelete:
            del playersresult[key]
            
    return max(player1universes, player2universes)
    

def solution2(filename):
    with open(filename, 'r') as myfile:
        line1 = myfile.readline().strip()
        line2 = myfile.readline().strip()
        
        player1startingposition = int(line1[line1.find(':')+1::])
        player2startingposition = int(line2[line2.find(':')+1::])
        
        return playagame(player1startingposition, player2startingposition)


def main():
    print(f'Result for test data for task 1 is {solution2("Day_21/testdata.txt")}')
    print(f'Result for data 21 for task 1 is {solution2("Day_21/data21.txt")}')
    
if __name__ == '__main__':
    main()