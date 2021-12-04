def add(board, num):
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y][0] == num:
                board[x][y][1] = True
                return [x, y]
    return None

def check(board, x, y):
    checkx = True
    for i in board[x]:
        if i[1] == False:
            checkx = False
            break
    if checkx:
        return True
    checkx = True
    for i in range(len(board[x])):
        if board[i][y][1] == False:
            checkx = False
            break
    return True if checkx else False


def sumempty(board):
    ret = 0
    for y in board:
        for x in y:
            if x[1] == False:
                ret += x[0]
    return ret



def main():
    myfile = open('Day_4/data4.txt', 'r')
    
    line1 = myfile.readline()
    data = line1.split(',')
    for i in range(len(data)):
        data[i] = int(data[i])
    boards = []
    line1 = myfile.readline()
    while line1 != '':
        board = []
        line1 = myfile.readline()
        while line1 != '\n':
            i = 0
            newline = []
            while i < len(line1):
                newline.append(line1[i:i+3])
                i += 3
                
            for i in range(len(newline)):
                newline[i] = [int(newline[i]), False]
            board.append(newline)
            line1 = myfile.readline()
            if line1 == '':
                break
        boards.append(board)
    
    
    
    print(boards[0])
    print(boards[0][1][1][0])
    len(boards)
    print(boards[-1])
    
 # boards[i] - numer planszy
 # boards[i][x][y][0] - numer o pozycji x, y na planszy
 # boards[i][x][y][1] - True jeśli już było, False otherwise
 
        
    myfile.close()
    
    # dodawanie do plansz
    bingo = False
    for num in data:
        for board in boards:
            tmp = add(board, num)
            if tmp:
                if check(board, tmp[0], tmp[1]):
                    bingo = True
                    print(f'Bingo!')
                    print(board)
                    print(num)
                    print(sumempty(board))
                    print(f'Result: {sumempty(board) * num}')
                    break
        if bingo:
            break
    print(boards)
            

if __name__ == '__main__':
    main()