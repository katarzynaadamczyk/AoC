'''
Advent of Code 
2024 day 17
my solution to tasks


task 1 - proceed as described in the task - prepare all functions, simply follow the instructions
task 2 - finally made it in one file
a bit of reverse engineering and more look into task data -> 
in my data there was a register A division by 2 ** 3 in test_2 data there is a division by 2 ** 3 also
as well as in my data and in second test data last instruction is to jump to beginning of program
first add range(0, 2 **3) to tested A register values 
then looking backwards at the input data :
check if any a iteration matches actual output 
if so then add range (a * 2 ** 3, a * (2 ** 3 + 1) ) to next a tested values

at the end get all a from previous iteration and look for a which gives exact output and is input data

this is the first task this year I got < 5000 position in total leaderboard (but only for the second task)
'''

import time

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        print(f'time taken by {func.__name__} is {round(time.time()-start, 4)}')

        return result
    return wrapper


class Solution:

    def __init__(self, filename) -> None:
        '''
        initialize Solution
        '''
        self.registers = {}
        self.get_data(filename)
        self.operands_values = {0: 0, 1: 1, 2: 2, 3: 3, 4: 'A', 5: 'B', 6: 'C'}
        self.functions = {0: self.adv, 1: self.bxl, 2: self.bst, 3: self.jnz, 
                          4: self.bxc, 5: self.out, 6: self.bdv, 7: self.cdv}


    def get_register(self, line):
        '''
        returns int value of given line
        '''
        return int(line[line.find(':')+1:].strip())


    def get_data(self, filename):
        '''
        parse data
        '''
        with open(filename, 'r') as myfile:
            for letter in 'ABC':
                self.registers.setdefault(letter, self.get_register(myfile.readline()))
            myfile.readline()
            line = myfile.readline()
            self.instructions_operands = [int(x) for x in line[line.find(':')+1:].strip().split(',')]


    def get_combo_operand_value(self, combo_operand):
        '''
        function to get valid combo operand value based on given int (0-6)
        '''
        combo_operand = self.operands_values[combo_operand]
        return combo_operand if type(combo_operand) == type(1) else self.registers[combo_operand]


    def division(self, combo_operand):
        '''
        returns division of numerator - register A and 2 ** combo_operand_value
        '''
        return self.registers['A'] // (2 ** self.get_combo_operand_value(combo_operand))


    def adv(self, combo_operand):
        '''
        saves division result in register A
        '''
        self.registers['A'] = self.division(combo_operand)

    
    def bdv(self, combo_operand):
        '''
        saves division result in register B
        '''
        self.registers['B'] = self.division(combo_operand)

    
    def cdv(self, combo_operand):
        '''
        saves division result in register C
        '''
        self.registers['C'] = self.division(combo_operand)
    

    def bxl(self, combo_operand):
        '''
        calculates bitwise XOR of register B and instruction's literal operand
        '''
        self.registers['B'] = self.registers['B'] ^ combo_operand


    def bst(self, combo_operand):
        '''
        calculates value of combo operand % 8 and saves it to register B
        '''
        self.registers['B'] = self.get_combo_operand_value(combo_operand) % 8

    
    def jnz(self, combo_operand):
        '''
        return True if there is a need to jump, False otherwise
        '''
        return self.registers['A'] != 0
    

    def bxc(self, combo_operand):
        '''
        calculates bitwise XOR of registers B and C and stores the result in register B
        '''
        self.registers['B'] = self.registers['B'] ^ self.registers['C']
    

    def out(self, combo_operand):
        '''
        outputs combo_operand_value modulo 8
        '''
        return self.get_combo_operand_value(combo_operand) % 8




 #   @time_it
    def solution_1(self) -> int:
        '''
        get result for task 1
        run the instructions until index for instruction exceeds the number of instructions in program
        '''
        result = []
        instruction, operand = 0, 1
        self.len_instruction_operands = len(self.instructions_operands)
        while instruction < self.len_instruction_operands and operand < self.len_instruction_operands:
            output = self.functions[self.instructions_operands[instruction]](self.instructions_operands[operand])
            if type(output) == type(1):
                result.append(output)
            if type(output) == type(True) and output == True:
                instruction = self.instructions_operands[operand]
                operand = instruction + 1
            else:                
                instruction += 2
                operand = instruction + 1
        return result

        # return ','.join([str(x) for x in result]) was for task 1
    
    @time_it
    def solution_2(self, param=3) -> int:
        '''
        get result for task 1
        run the instructions until index for instruction exceeds the number of instructions in program
        '''
        new_possible_a = [i for i in range(2 ** param)]
        for act_value in self.instructions_operands[::-1]:
            possible_a = new_possible_a
            new_possible_a = []
            for a in possible_a:
                self.registers['A'] = a
                for instruction, operand in zip(self.instructions_operands[:len(self.instructions_operands) - 2:2], \
                                                self.instructions_operands[1:len(self.instructions_operands) - 1:2]):
                    output = self.functions[instruction](operand)
                    if type(output) == type(1) and output == act_value:
                        for i in range(a * 2 ** param, a * 2 ** param + 2 ** param):
                            new_possible_a.append(i)
        
        for a in possible_a:
            self.registers['A'] = a
            if self.solution_1() == self.instructions_operands:
                return a
        return 0

    


    

def main():

    print('TEST 1')
    sol = Solution('2024/Day_17/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal ?')
    print('TEST 2')
    sol = Solution('2024/Day_17/test_2.txt')
    print('TEST 2')
    print('test 1:', sol.solution_2(), 'should equal ?')
    print('SOLUTION')
    sol = Solution('2024/Day_17/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1()) 
    print('Solution 2:', sol.solution_2()) 
   


if __name__ == '__main__':
    main()
