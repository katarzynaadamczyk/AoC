# Katarzyna Adamczyk
# Solution to day 24 task 1 of Advent of Code 2021

from itertools import product

class Solution:
    equations = []
    
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
        evaluation1 = self.evaluaterange(equation1)
        evaluation2 = self.evaluaterange(equation2)
        if evaluation1[0] >= evaluation2[0] and evaluation1[0] <= evaluation2[1]:
            return True
        if evaluation1[1] >= evaluation2[0] and evaluation1[1] <= evaluation2[1]:
            return True
        if evaluation2[0] >= evaluation1[0] and evaluation2[0] <= evaluation1[1]:
            return True
        if evaluation2[1] >= evaluation1[0] and evaluation2[1] <= evaluation1[1]:
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

def preparedict():
    newdict = {}
    for i in range(14):
        newdict[i] = ''
    return newdict

def evaluate(equation, numbers, numdict):
    result = 0 if not equation.isdecimal() else int(equation)
    pos = 0
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
                    if numdict[int(nums[i][nums[i].find('[')+1:-1])] == '':
                        numdict[int(nums[i][nums[i].find('[')+1:-1])] = int(numbers[pos])
                        pos += 1
                    nums[0] = numdict[int(nums[i][nums[i].find('[')+1:-1])]
                else: 
                    nums[i] = int(nums[i])
            if sign == '+':
                result = nums[0] + nums[1]
            elif sign == '-':
                result = nums[0] - nums[1]
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

def countnumber(equations):
    countz = 1000
    howmany = equations[0][0].count('num[')
    

    for nums in product('987654321', repeat=howmany):
        mydict = preparedict()
        countz = evaluate(equations[0][0], nums, mydict)
        if countz >= equations[0][1]:
            continue
        for i in range(1, len(equations)):
            evaluation = evaluate(equations[i][0], [], mydict)
            if evaluation < 1 or evaluation > 9:
                break
            mydict[int(equations[i][1][equations[i][1].find('[')+1:-1])] = evaluation
        print(countz)
        print(mydict)
        if evaluation < 1 or evaluation > 9:
            continue
        else:
            break
    
    result = ''
    for i in range(14):
        result += str(mydict[i])
    
    return int(result)
    

def findmaxserialnumber(data):
    dimensions = {'w': '0', 'x': '0', 'y': '0', 'z': '0'}
    newnode = None
    for i in range(14):
        newnode = Solution(dimensions, data, i, 'num[' + str(i) + ']', newnode)
        dimensions = newnode.dimensions
        
    equations = Solution.equations
    equations.insert(0, preparez(dimensions['z']))
    print(equations)
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
    print(f'Result for data24 for task 1 is {solution1("Day_24/data24.txt")}')
    

if __name__ == '__main__':
    main()