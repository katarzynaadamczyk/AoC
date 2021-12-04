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
 
 # boards[i] - numer planszy
 # boards[i][x][y][0] - numer o pozycji x, y na planszy
 # boards[i][x][y][1] - True jeśli już było, False otherwise
 
        
    myfile.close()

if __name__ == '__main__':
    main()