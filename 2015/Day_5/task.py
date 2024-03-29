'''
Advent of Code 
2015 day 3
my solution to tasks from day 3

solution 1 - check each word for rules named in task (if count of vowels is >= 3, if none of ['ab', 'cd', 'pq', 'xy'] is in word and if word contains any doubled letter). 
If so, add to actual count of nice words.
solution 2 - check each word for rules named in task (functions check_rule_1 and check_rule_2). If they say True that increase counter of nice words by 1.

'''

def solution_1(filename):
    nice_count = 0
    doubled_str = [x * 2 for x in 'abcdefghijklmnopqrstuvwxyz']
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line.strip()
            vowel_count = 0
            for vowel in 'aeiou':
                vowel_count += line.count(vowel)
            if vowel_count < 3:
                continue
            check = False
            for wrong_str in ['ab', 'cd', 'pq', 'xy']:
                if wrong_str in line:
                    check = True
                    break
            if check:
                continue
            for doubled in doubled_str:
                if doubled in line:
                    check = True
                    break
            if check:
                nice_count += 1
            
                
    return nice_count


def check_rule_1(word):
    for index in range(len(word) - 2):
        if word.find(word[index:index + 2], index + 2) >= index + 2:
            return True
    return False


def check_rule_2(word):
    for char_1, char_2 in zip(word[:-2], word[2:]):
        if char_1 == char_2:
            return True
    return False

def solution_2(filename):
    nice_count = 0
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line.strip()
            if check_rule_1(line) and check_rule_2(line):
                nice_count += 1           
                
    return nice_count

def main():
    print(f'Result for data for test 1 is {solution_1("2015/Day_5/test.txt")}')
    print(f'Result for data for task 1 is {solution_1("2015/Day_5/data.txt")}')
    
    print(f'Result for data for test 1 is {solution_2("2015/Day_5/test_2.txt")}')
    print(f'Result for data for task 1 is {solution_2("2015/Day_5/data.txt")}')
    
    
if __name__ == '__main__':
    main()