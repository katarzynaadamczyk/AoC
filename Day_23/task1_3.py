# Katarzyna Adamczyk
# Solution to day 23 task 1 of Advent of Code 2021


from copy import deepcopy

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
    

def convertlisttotuple(burrow):
    return tuple(tuple(i) for i in burrow)

def converttupletolist(burrow):
    return list(list(i) for i in burrow)
    

def isempty(burrow, posx):
    if len(burrow[posx]) > 1:
        for room in burrow[posx]:
            if room != '.':
                return False
        return True
    return False

def containsonerightamphipod(burrow, posx): 
    if len(burrow[posx]) > 1:
        for room in range(len(burrow[posx])):
            if burrow[posx][room] != '.':
                if burrow[posx][room] == roomforamphipod[posx] and room == 2:
                    return True
                return False
    return False

def containsrightamphipods(burrow, posx):
    if len(burrow[posx]) > 1:
        if burrow[posx][1] == burrow[posx][2] and burrow[posx][2] == roomforamphipod[posx]:
            return True 
    return False

def ifsolved(burrow):
    for x in range(2, 9, 2):
        if not containsrightamphipods(burrow, x):
            return False
    return True

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
        return deepcopy(burrow), moves * energyforamphipod[burrow[posx][y]]
    return burrow, -1

def godown(burrow, posx, x, startingmoves):
    if isempty(burrow, x):
        burrow[x][2] = burrow[posx][0]
        burrow[posx][0] = '.'
        return [deepcopy(burrow), startingmoves + 2 * energyforamphipod[burrow[x][2]]] # było 3
    elif containsonerightamphipod(burrow, x):
        burrow[x][1] = burrow[posx][0]
        burrow[posx][0] = '.'
        return [deepcopy(burrow), startingmoves + 1 * energyforamphipod[burrow[x][1]]] # było 2
    return [burrow, -1]
    
def goleft(burrow, posx, startingmoves):
    burrows = []
    moves = 0
    for x in range(posx - 1, -1, -1):
        moves += 1
        if burrow[x][0] == '.':
            if len(burrow[x]) == 1:
                burrow[x][0] = burrow[x + 1][0]
                burrow[x + 1][0] = '.'
                burrows.append([deepcopy(burrow), startingmoves + moves * energyforamphipod[burrow[x][0]]])
            else:
                if x in roomforamphipod.keys() and roomforamphipod[x] == burrow[x + 1][0]:
                    amphipod = roomforamphipod[x]
                    newburrow, downmoves = godown(deepcopy(burrow), x + 1, x, 0) # change 0 to starting moves
                    if downmoves > 0:
                        return [[newburrow, startingmoves + moves * energyforamphipod[amphipod] + downmoves]]
                if ifmaygoleft:
                    burrow[x][0] = burrow[x + 1][0]
                    burrow[x + 1][0] = '.'
                else: 
                    return burrows   
        else:
            return burrows

    return burrows
            
    
def goright(burrow, posx, startingmoves):
    burrows = []
    moves = 0
    for x in range(posx + 1, len(burrow)):
        if burrow[x][0] == '.':
            
            moves += 1
            if len(burrow[x]) == 1:
                burrow[x][0] = burrow[x - 1][0]
                burrow[x - 1][0]= '.'
                burrows.append([deepcopy(burrow), startingmoves + moves * energyforamphipod[burrow[x][0]]])
            else:
                if x in roomforamphipod.keys() and roomforamphipod[x] == burrow[x - 1][0]:
                    amphipod = roomforamphipod[x]
                    newburrow, downmoves = godown(deepcopy(burrow), x - 1, x, 0) # change 0 to starting moves
                    if downmoves > 0:
                        return [[newburrow, startingmoves + moves * energyforamphipod[amphipod] + downmoves]]
                if ifmaygoright:
                    burrow[x][0] = burrow[x - 1][0]
                    burrow[x - 1][0] = '.'
                else: 
                    return burrows
        else:
            return burrows
    return burrows



def gofromcorridortoroom(burrow, posx, startingmoves):
    room = 0
    for key, value in roomforamphipod.items():
        if value == burrow[posx][0]:
            room = key
            break
            
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
      #  print('gofromcorridortoroom')
      #  print_burrow(burrow)
      #  print(burrow)
        newburrow, downmoves = godown(deepcopy(burrow), posx, room, startingmoves + abs(room - posx) * energyforamphipod[value])
        if downmoves > 0:
            return [newburrow, downmoves]
    
    return [burrow, -1]


def moveamphipods(burrow):
    burrows = [[burrow, 0]]
    results = set()
    i = 0
    while len(burrows) > 0:
        i += 1
        newburrows = []
        burrowsleft = []
        burrowsright = []
        for burrow in burrows:
            # go from corridor to room
            changed = True
            noofchanges = 0
            while changed:
                changed = False
                for x in range(len(burrow[0])):
                    if burrow[0][x] != '.':
                        newburrow, moves = gofromcorridortoroom(deepcopy(burrow[0]), x, burrow[1])
                        if moves > 0:
                            burrow[0] = newburrow
                            burrow[1] = moves
                            changed = True
                            noofchanges += 1
            if noofchanges > 0:
                newburrows.append([burrow[0], burrow[1]])

            # go from room to corridor
            for room in roomforamphipod.keys():
                if not containsrightamphipods(burrow[0], room) and not containsonerightamphipod(burrow[0], room) and not isempty(burrow[0], room):
                    y = 1 if burrow[0][room][1] != '.' else 2
                    newburrow, moves = goup(deepcopy(burrow[0]), room, y)
                    if moves > 0:
                        if ifmaygoleft(burrow[0], room):
                            burrowsleft += goleft(deepcopy(newburrow), room, moves + burrow[1])
                           # burrowsleft = goleft(deepcopy(newburrow), room, moves + burrow[1])
                            
                        if ifmaygoright(burrow[0], room):
                            burrowsright += goright(deepcopy(newburrow), room, moves + burrow[1])
                           # burrowsright = goright(deepcopy(newburrow), room, moves + burrow[1])
                            
        # shorten newburrows - check for no moves and check for finished ones
        # if no moves - delete from newburrows
        # if finished - add its result to results
        
        #print('newburrows')
        #print(newburrows)
        newburrows = newburrows + burrowsleft + burrowsright
        #print('left')
        #print(burrowsleft)
        #print('right')
        #print(burrowsright)
        
        burrows = []
        burrowsset = set()
        for burrow in newburrows:
            if ifsolved(burrow[0]):
                results.add(burrow[1])
            elif burrow[1] > 0:
                if convertlisttotuple(burrow[0]) not in burrowsset:
                    burrowsset.add(convertlisttotuple(burrow[0]))
                    burrows.append(burrow)
                else:
                    sortedburrow = sorted(burrow[0])
                    for i in range(len(burrows)):
                        if sortedburrow == sorted(burrows[i][0]):
                            burrows[i][1] = min(burrows[i][1], burrow[1])
                            break
        print(f'len(burrows) = {len(burrows)}')
    
    return results


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