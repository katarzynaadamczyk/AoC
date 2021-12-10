def main():
    
    with open('Day_10/data10.txt', 'r') as myfile:
        values = {'(': 1, '[': 2, '{': 3, '<': 4}
        opening = '([{<'
        closing = ')]}>'
        scores = []
        for line in myfile:

            tmp = ''
            i = 0
            score = 0
            wrongline = False
            
            for char in line[:-1]:
                if char in opening:
                    tmp += char
                    i = opening.find(char)
                elif i == closing.find(char):
                    tmp = tmp[:-1]
                    if len(tmp) > 0:
                        i = opening.find(tmp[-1])
                else:
                    wrongline = True
                    break                 
            if not wrongline:
                for i in range(len(tmp)):
                    score *= 5
                    score += values[tmp[- i - 1]]
            
            if score > 0:
                scores.append(score)    
            
        scores = sorted(scores)
                   
        print(scores)          
        
                
        print(f'Result is {scores[len(scores) // 2]}')    
            

if __name__ == '__main__':
    main()