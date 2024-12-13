'''
Advent of Code 
2024 day 13
my solution to tasks



task 1 - 
            
                

'''

from tqdm import tqdm
import re

class Solution:

    def __init__(self, filename) -> None:
        self.claw_machines = []
        self.get_data(filename)
        

    def get_data(self, filename):
        with open(filename, 'r') as myfile:
            tag = 0
            for line in myfile:
                if tag % 4 == 0:
                    new_data = {}
                    for name, num in zip(['AX', 'AY'], re.findall(r'-?\d+', line)):
                        new_data.setdefault(name, int(num))
                elif tag % 4 == 1:
                    for name, num in zip(['BX', 'BY'], re.findall(r'-?\d+', line)):
                        new_data.setdefault(name, int(num))
                elif tag % 4 == 2:
                    for name, num in zip(['X', 'Y'], re.findall(r'\d+', line)):
                        new_data.setdefault(name, int(num))
                    self.claw_machines.append(new_data)
                tag += 1
   
    
    def get_tokens_for_machine(self, machine):
        # calculate a
        diff = machine['BY'] * machine['AX'] - machine['BX'] * machine['AY']
        if diff == 0: 
            return 0
        a = (machine['BY'] * machine['X'] - machine['BX'] * machine['Y']) // diff
        if a < 0 or a > 100 or machine['BX'] == 0:
            return 0
        # calculate b
        b1 = (machine['X'] - machine['AX'] * a) // machine['BX']
        b2 = (machine['Y'] - machine['AY'] * a) // machine['BY']
        if b1 == b2 and 0 <= b1 <= 100:
            return a * 3 + b1
        return 0
    
    def get_tokens_for_machine_2(self, machine):
        # calculate a
        diff = machine['BY'] * machine['AX'] - machine['BX'] * machine['AY']
        if diff == 0: 
            return 0
        a = (machine['BY'] * machine['X'] - machine['BX'] * machine['Y']) // diff
        if a < 0 or machine['BX'] == 0:
            return 0
        # calculate b
        b1 = (machine['X'] - machine['AX'] * a) // machine['BX']
        b2 = (machine['Y'] - machine['AY'] * a) // machine['BY']
        if b1 == b2 and 0 <= b1 and machine['AX'] * a + machine['BX'] * b1 == machine['X'] and \
            machine['AY'] * a + machine['BY'] * b1 == machine['Y']:
            #print(a, b1)
            return a * 3 + b1
        return 0
    
    def solution_1(self) -> int:
        return sum([self.get_tokens_for_machine(machine) for machine in self.claw_machines])
    

    
    def solution_2(self) -> int:
        result = 0
        for machine in self.claw_machines:
            machine['X'] += 10000000000000
            machine['Y'] += 10000000000000
            result += self.get_tokens_for_machine_2(machine)
        return result

    

def main():

    print('TASK 1')
    sol = Solution('2024/Day_13/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 480')
    print('test 1:', sol.solution_2(), 'should equal ?')
    sol = Solution('2024/Day_13/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1()) # 28044 too high
    print('Solution 2:', sol.solution_2()) # 131439516923806 too high
   


if __name__ == '__main__':
    main()
