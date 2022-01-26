# Katarzyna Adamczyk
# Solution to day 24 task 1 of Advent of Code 2021

from itertools import product
from select import select

class Solution:
    # prepared
    equations = []
    
    def __init__(self, rrange=14) -> None:
        self.rrange = rrange
        self.preparedata()
        
    
    def preparedata(self):
        self.dimensions = {}
        for i in range(self.rrange):
            lst = []
            for j in range(9, 0, -1):
                lst.append(j)
            self.dimensions[i] = lst
        for i in 'xyzw':
            self.dimensions[i] = '0'
        print(self.dimensions)
        
    # evaluates equation putting num in every possible num[] in the equation
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
        if ((evaluation1[0] >= evaluation2[0] and evaluation1[0] <= evaluation2[1]) or (evaluation1[1] >= evaluation2[0] and evaluation1[1] <= evaluation2[1]) or
           (evaluation2[0] >= evaluation1[0] and evaluation2[0] <= evaluation1[1]) or (evaluation2[1] >= evaluation1[0] and evaluation2[1] <= evaluation1[1])):
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
        elif (self.dimensions[b] if b.isalpha() else b) != '0' and b != '':
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
    
    def changedimensions(self, data):
        for i in range(len(data)):
            for instrucion in data[i]:
                if instrucion[0] == 'inp':
                    self.inp(instrucion[1], 'num[' + str(i) + ']')
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

    
    def preparez(self, z):
        lessthan = 1
        while z[-4] == '/':
            lessthan *= int(z[-3:-1])
            z = z[1:-4]    
    
        return [z, lessthan]

    def evaluate(self, equation, numdict):
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

    
    def solve(self, data):
        self.changedimensions(data)
        print(self.dimensions)
        print(Solution.equations)
        mydict = {0: 9, 1: 9, 2: 9}
        print(self.evaluate(Solution.equations[0][0], mydict))
        return 0
    

def findmaxserialnumber(data):
    newsol = Solution()
    return newsol.solve(data)

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
    for xyz in product(['a', 'b', 'c'], ['d', 'e']):
        mydict = {}
        for i in range(len(xyz)):
            mydict[i] = xyz[i]
        print(mydict)
    

if __name__ == '__main__':
    main()