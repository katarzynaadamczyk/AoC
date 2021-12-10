def ifnotcorrupted(line):
    # TODO
    pass

def main():
    
    with open('Day_10/data10.txt', 'r') as myfile:
        result = 0
        values = {')': 3, ']': 57, '}': 1197, '>': 25137}
        opening = '([{<'
        closing = ')]}>'
        for line in myfile:

            tmp = ''
            i = 0
            
            for char in line[:-1]:
                if char in opening:
                    tmp += char
                    i = opening.find(char)
                elif i == closing.find(char):
                    tmp = tmp[:-1]
                    if len(tmp) > 0:
                        i = opening.find(tmp[-1])
                else:
                    result += values[char]
                    break                 
                    
        
                
        print(f'Result is {result}')    
            

if __name__ == '__main__':
    main()