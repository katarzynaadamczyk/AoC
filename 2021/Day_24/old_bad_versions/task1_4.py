# Katarzyna Adamczyk
# Solution to day 24 task 1 of Advent of Code 2021

from itertools import product
from math import prod
import numbers

class Solution:
    equations = []
    commonparts = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [],
                   8: [], 9: [], 10: [], 11: [], 12: [], 13: []}
    
    def __init__(self, dimensions, data, lvl, val, previous=None) -> None:
        self.level = lvl
        self.dimensions = {}
        self.value = val
        self.data = data
        for key in dimensions:
            self.dimensions[key] = dimensions[key]
        self.changedimensions()
        self.previous = previous

    def evaluateequation(self, equation, num):
        result = 0 if not equation.isdecimal() else int(equation)
        while not (equation[0].isdecimal() or equation[0] == '-'):
            lastbracket = equation.find(')')
            if lastbracket > 0:
                firstbracket = equation.rfind('(', 0, lastbracket)
                sign = ''
                for i in range(firstbracket + 1, lastbracket):
                    if equation[i] in '+-*/%':
                        sign = equation[i]
                        break
                nums = equation[firstbracket+1:lastbracket].split(sign)
                for i in range(len(nums)):
                    if nums[i][0] == 'n' and nums[i][-1] == ']':
                        nums[i] = num
                    else: 
                        nums[i] = int(nums[i])
                if sign == '+':
                    result = nums[0] + nums[1]
                elif sign == '-':
                    result = nums[0] - nums[1]
                    while result < 0:
                        result = 9 + result
                elif sign == '*':
                    result = nums[0] * nums[1]
                elif sign == '/':
                    result = nums[0] // nums[1]
                elif sign == '%':
                    result = nums[0] % nums[1]
                equation = equation[0:firstbracket] + str(result) + equation[lastbracket+1::]
            else:
                result = num if '[' in equation else result
                equation = str(result)
        return result
    
    def evaluaterange(self, equation):
        resultmin = self.evaluateequation(equation, 1)
        resultmax = self.evaluateequation(equation, 9)
        return [min(resultmax, resultmin), max(resultmax, resultmin)]
    
    def dotheyhavecommonpart(self, equation1, equation2):
        #print('dotheyhavecommonpart')
        #print(equation1)
        evaluation1 = self.evaluaterange(equation1)
        #print(evaluation1)
        #print(equation2)
        evaluation2 = self.evaluaterange(equation2)
        #print(evaluation2)
        if ((evaluation1[0] >= evaluation2[0] and evaluation1[0] <= evaluation2[1]) or (evaluation1[1] >= evaluation2[0] and evaluation1[1] <= evaluation2[1]) or
           (evaluation2[0] >= evaluation1[0] and evaluation2[0] <= evaluation1[1]) or (evaluation2[1] >= evaluation1[0] and evaluation2[1] <= evaluation1[1])):
            if '[' in equation2:
                Solution.commonparts[int(equation2[equation2.find('[')+1:-1])] = [max(evaluation1[0], evaluation2[0]), min(evaluation1[1], evaluation2[1])]
            return True
        return False
        
    def inp(self, a, val):
        self.dimensions[a] = val
    
    def add(self, a, b):
        if self.dimensions[a] == '0':
            self.dimensions[a] = self.dimensions[b] if b.isalpha() else b
        elif self.dimensions[a].isdecimal() and b.isdecimal():
            self.dimensions[a] = str(int(self.dimensions[a]) + int(b))
        elif self.dimensions[a].isdecimal() and len(b) > 1 and b[0] == '-' and b[1::].isdecimal():
            self.dimensions[a] = str(int(self.dimensions[a]) + int(b))
        elif (self.dimensions[b] if b.isalpha() else b) != '0':
            if len(b) > 1 and b[0] == '-':
                self.dimensions[a] = '(' + self.dimensions[a] + b + ')'
            else:
                self.dimensions[a] = '(' + self.dimensions[a] + '+' + (self.dimensions[b] if b.isalpha() else b) + ')'
    
    def mul(self, a, b):
        if (self.dimensions[b] if b.isalpha() else b) == '0' or self.dimensions[a] == '0':
            self.dimensions[a] = '0'
        elif self.dimensions[a] == '1':
            self.dimensions[a] = self.dimensions[b] if b.isalpha() else b
        elif self.dimensions[a][-3:-1] == (self.dimensions[b] if b.isalpha() else b):
            self.dimensions[a] = self.dimensions[a][1:-4]
        elif (self.dimensions[b] if b.isalpha() else b) != '1':
            self.dimensions[a] = '(' + self.dimensions[a] + '*' + (self.dimensions[b] if b.isalpha() else b) + ')'
    
    def div(self, a, b):
        if not (self.dimensions[a] == '0' or (self.dimensions[b] if b.isalpha() else b) == '1'):
            self.dimensions[a] = '(' + self.dimensions[a] + '/' + (self.dimensions[b] if b.isalpha() else b) + ')'
        
    def mod(self, a, b):
        if self.dimensions[a] == '0':
            self.dimensions[a] = '0'            
        elif b != '1':
            self.dimensions[a] = '(' + self.dimensions[a] + '%' + (self.dimensions[b] if b.isalpha() else b) + ')'
    
    def eql(self, a, b):
        equation = self.dimensions[a]
        self.dimensions[a] = '1' if self.dimensions[a] == (self.dimensions[b] if b.isalpha() else b) or self.dotheyhavecommonpart(self.dimensions[a], self.dimensions[b] if b.isalpha() else b) else '0' 
        if self.dimensions[a] == '1' and equation != '0':
            Solution.equations.append([equation, (self.dimensions[b] if b.isalpha() else b)])
    
    def changedimensions(self):
        for instrucion in self.data[self.level]:
            if instrucion[0] == 'inp':
                self.inp(instrucion[1], self.value)
            elif instrucion[0] == 'add':
                self.add(instrucion[1], instrucion[2])
            elif instrucion[0] == 'mul':
                self.mul(instrucion[1], instrucion[2])
            elif instrucion[0] == 'div':
                self.div(instrucion[1], instrucion[2])
            elif instrucion[0] == 'mod':
                self.mod(instrucion[1], instrucion[2])
            elif instrucion[0] == 'eql':
                self.eql(instrucion[1], instrucion[2])
    
    def returnequations(self):
        return Solution.equations
    
    
def preparez(z):
    lessthan = 1
    while z[-4] == '/':
        lessthan *= int(z[-3:-1])
        z = z[1:-4]    
    
    return [z, lessthan]

def preparedict(nums, numbers):
    newdict = {}
    j = 0
    for i in range(len(numbers)):
        if numbers[i] == 2 or numbers[i] == 4:
            newdict[numbers[i]] = 1
        else:
            newdict[numbers[i]] = int(nums[j])
            j += 1
    return newdict

def evaluate(equation, numdict):
    result = 0 if not equation.isdecimal() else int(equation)
    while not (equation[0].isdecimal() or equation[0] == '-'):
        #print(equation)
        lastbracket = equation.find(')')
        if lastbracket > 0:
            firstbracket = equation.rfind('(', 0, lastbracket)
            sign = ''
            for i in range(firstbracket + 1, lastbracket):
                if equation[i] in '+-*/%':
                    sign = equation[i]
                    break
            nums = equation[firstbracket+1:lastbracket].split(sign)
            for i in range(len(nums)):
                if nums[i][0] == 'n' and nums[i][-1] == ']':
                    nums[0] = numdict[int(nums[i][nums[i].find('[')+1:-1])]
                else: 
                    nums[i] = int(nums[i])
            if sign == '+':
                result = nums[0] + nums[1]
            elif sign == '-':
                result = nums[0] - nums[1]
                
                while result > 9:
                    result -= nums[1]
                while result < 1:
                    result = 9 + result
                        
            elif sign == '*':
                result = nums[0] * nums[1]
            elif sign == '/':
                result = nums[0] // nums[1]
            elif sign == '%':
                result = nums[0] % nums[1]
            equation = equation[0:firstbracket] + str(result) + equation[lastbracket+1::]
        else:
            result = numdict[int(equation[equation.find('[')+1:-1])] if '[' in equation else result
            equation = str(result)
    return result

def findnumbers(howmany, equation):
    pos = 0
    numbers = []
    for i in range(howmany):
        newnumber = int(equation[equation.find('[', pos)+1:equation.find(']', pos)])
        pos = equation.find(']', pos) + 1
        numbers.append(newnumber)
    return numbers

def countresult(mydict):
    result = ''
    for i in range(14):
        result += str(mydict[i])
    return result

def countnumber(equations):
    countz = 1000
    howmany = equations[0][0].count('num[')
    numbers = findnumbers(howmany, equations[0][0])
    result = 0
    print('numbers')
    print(numbers)
    for nums in product('987654321', repeat=howmany-2):
        mydict = preparedict(nums, numbers)
        countz = evaluate(equations[0][0], mydict)
        if countz >= equations[0][1]:
            continue
        for i in range(1, len(equations)):
            evaluation = evaluate(equations[i][0], mydict)
            if evaluation < 1 or evaluation > 9:
                break
            mydict[int(equations[i][1][equations[i][1].find('[')+1:-1])] = evaluation
      #  print(i)
      #  print(equations[i][1])
      #  print(evaluation)
        print(countz)
        print(mydict)
        actresult = int(countresult(mydict))
        if actresult > result:
            result = actresult
        if nums[0] == '4':
            break
    
    return result
    

def findmaxserialnumber(data):
    dimensions = {'w': '0', 'x': '0', 'y': '0', 'z': '0'}
    newnode = None
    for i in range(14):
        newnode = Solution(dimensions, data, i, 'num[' + str(i) + ']', newnode)
        dimensions = newnode.dimensions
        print(f'i = {i}')
        print(dimensions)
        
    equations = Solution.equations
    equations.insert(0, preparez(dimensions['z']))
    print(equations)
    print(dimensions)
    return countnumber(equations)

def solution1(filename):
    with open(filename, 'r') as myfile:
        data = []
        instructions = []
        for line in myfile:
            tmp = line.split(' ')
            for i in range(len(tmp)):
                tmp[i] = tmp[i].strip()
            if tmp[0] == 'inp':
                if len(instructions) > 0:
                    data.append(instructions)
                instructions = []
            instructions.append(tmp)
        data.append(instructions)
        
        return findmaxserialnumber(data)




def main():
    mydict = {}
    for key in range(14):
        mydict[key] = 0
    equation = '((((((((((((((((((((num[0]+7)*26)+(num[1]+15))*26)+(num[2]+2))+(num[3]+15))*26)+(num[4]+14))+(num[5]+2))*26)+(num[6]+15))+(num[7]+1))+(num[8]+15))+(num[9]+15))*26)+(num[10]+12))*26)+(num[11]+2))+(num[12]+13))+(num[13]+13))'
    print(evaluate(equation, mydict))
    
    for key in range(14):
        mydict[key] = 9
    print(evaluate(equation, mydict))
    
    
    
    
    print(f'Result for data24 for task 1 is {solution1("Day_24/data24.txt")}')
    

if __name__ == '__main__':
    main()