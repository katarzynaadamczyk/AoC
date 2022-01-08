# Katarzyna Adamczyk
# Solution to day 23 task 1 of Advent of Code 2021


from types import BuiltinFunctionType


roomforamphipod = {2: 'A', 4: 'B', 6: 'C', 8: 'D'}
energyforamphipod = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

def print_burrow(burrow):
    for i in range(len(burrow) + 2):
        print('#', end='')
    print()
    print('#', end='')
    for i in range(len(burrow)):
        print(burrow[i][0], end='')
    print('#')
    for i in range(1, 3):
        if i == 1:
            print('###', end='')
        else:
            print('  #', end='')
        for j in range(2, 9, 2):
            print(burrow[j][i], end='#')
        if i == 1:
            print('##')
        else:
            print()
    print('  #########')
    

def isempty(burrow, posx):
    if len(burrow[posx]) > 1:
        for room in burrow[posx]:
            if room != '.':
                return False
        return True
    return False

def containsonerightamphipod(burrow, posx, amphipod):
    if len(burrow[posx]) > 1:
        for room in range(len(burrow[posx])):
            if burrow[posx][room] != '.':
                if burrow[posx][room] == amphipod and room == 2:
                    return True
                return False
    return False

def containsrightamphipods(burrow, posx, amphipod):
    if len(burrow[posx]) > 1:
        if burrow[posx][1] == burrow[posx][2] and burrow[posx][2] == amphipod:
            return True 
    return False

def ifmaygoleft(burrow, posx):
    if burrow[posx - 1][0] == '.':
        return True
    return False

def ifmaygoright(burrow, posx):
    if burrow[posx + 1][0] == '.':
        return True
    return False

def goup(burrow, posx, posy):
    if ifmaygoleft(burrow, posx) or ifmaygoright(burrow, posx):
        moves = 0
        for y in range(posy - 1, -1, -1):
            if burrow[posx][y] == '.':
                burrow[posx][y] = burrow[posx][y + 1]
                burrow[posx][y + 1] = '.'
                moves += 1
            else:
                return burrow, -1
        return burrow, moves * energyforamphipod[burrow[posx][y]]
    
def goleft(burrow, posx, moves=0):
    burrows = []
    for x in range(posx - 1, -1, -1):
        if burrow[x][0] == '.':
            if len(burrow[x]) == 1:
                burrow[x][0] = burrow[x + 1][0]
                burrow[x + 1][0] = '.'
                moves += 1
                burrows.append([burrow.copy(), moves * energyforamphipod[burrow[x][0]]])
            else:
                if roomforamphipod[x] == burrow[x + 1][0]:
                    if isempty(burrow, x):
                        moves += 3
                        burrow[x][2] = burrow[x + 1][0]
                        burrow[x + 1][0] = '.'
                        return [burrow, moves * energyforamphipod[burrow[x][2]]]
                    elif containsonerightamphipod(burrow, x, burrow[x + 1][0]):
                        moves += 2
                        burrow[x][1] = burrow[x + 1][0]
                        burrow[x + 1][0] = '.'
                        return [burrow, moves * energyforamphipod[burrow[x][1]]]
                if ifmaygoleft:
                    burrow[x][0] = burrow[x + 1][0]
                    burrow[x + 1][0] = '.'
                    moves += 1
                else: 
                    return burrows
                    
        else:
            return burrows
            
    
def goright(burrow, posx, posy, moves=0):
    burrows = []
    for x in range(posx + 1, len(burrow)):
        if burrow[x][0] == '.':
            if len(burrow[x]) == 1:
                burrow[x][0] = burrow[x - 1][0]
                burrow[x - 1][0]= '.'
                moves += 1
                burrows.append([burrow.copy(), moves * energyforamphipod[burrow[x][0]]])
            else:
                if roomforamphipod[x] == burrow[x - 1][0]:
                    if isempty(burrow, x):
                        moves += 3
                        burrow[x][2] = burrow[x - 1][0]
                        burrow[x - 1][0] = '.'
                        return [burrow, moves * energyforamphipod[burrow[x][2]]]
                    elif containsonerightamphipod(burrow, x, burrow[x - 1][0]):
                        moves += 2
                        burrow[x][1] = burrow[x - 1][0]
                        burrow[x - 1][0] = '.'
                        return [burrow, moves * energyforamphipod[burrow[x][1]]]
                if ifmaygoright:
                    burrow[x][0] = burrow[x - 1][0]
                    burrow[x - 1][0] = '.'
                    moves += 1
                else: 
                    return burrows
                    
        else:
            return burrows


def gofromcorridortoroom(burrow, posx):
    room = 0
    moves = 0
    for key, value in roomforamphipod:
        if value == burrow[posx][0]:
            room = key
            
    obstacles = False
    if posx > room: # need to go left    
        for x in range(room, posx):
            if burrow[x][0] != '.':
                obstacles = True
    else: # posx < room, need to go right
        for x in range(posx + 1, room + 1):
            if burrow[x][0] != '.':
                obstacles = True
    if not obstacles:
        moves = abs(room - posx)
        if isempty(burrow, room):
            moves += 3
            burrow[room][2] = burrow[posx][0]
            burrow[posx][0] = '.'
            return [burrow, moves * energyforamphipod[burrow[room][2]]]
        elif containsonerightamphipod(burrow, x, burrow[x - 1][0]):
            moves += 2
            burrow[room][1] = burrow[posx][0]
            burrow[posx][0] = '.'
            return [burrow, moves * energyforamphipod[burrow[room][1]]]
    
    return burrow, -1


def moveamphipods(burrow):
    
    
    
    pass


def organizeamphipods(burrow):
    result = moveamphipods(burrow)
    
    return min(result)
    

def solution1(filename):
    with open(filename, 'r') as myfile:
        
        burrow = []
        alllines = myfile.readlines()
        for char in alllines[1]:
            if char == '.':
                burrow.append([char])
        
        for i in range(2, 4):
            for position in range(1, len(alllines[i]) - 2):
                if alllines[i][position] in 'ABCD':
                    burrow[position - 1].append(alllines[i][position])
        
        
        return organizeamphipods(burrow)


def solution2(filename):
    with open(filename, 'r') as myfile:
        
        pass
    
        return 0

def main():
    print(f'Result for test data for task 1 is {solution1("Day_23/testdata.txt")}')
    print(f'Result for data 23 for task 1 is {solution1("Day_23/data23.txt")}')
    

if __name__ == '__main__':
    main()