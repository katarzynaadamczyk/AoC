'''
Advent of Code 
2023 day 12
my solution to task 1 & 2

solution 1 - 

solution 2 - 

'''

from functools import reduce
from queue import Queue

HIGH = True # high pulse
LOW = False # low pulse

class Module:
    def __init__(self, lst_of_modules, name):
        self.__name__ = name
        self.__destinations_modules__ = []
        for arg in lst_of_modules:
            self.__destinations_modules__.append(arg)

    def receive_a_pulse(self, pulse, name):
        return False

    def check_position(self):
        return True

class Button(Module):
    def __init__(self, lst_of_modules, name) -> None:
        super().__init__(lst_of_modules, name)

    def receive_a_pulse(self, pulse, name):
        return (self.__broadcaster__, pulse)
    
class Broadcaster(Module):
    def __init__(self, lst_of_modules, name):
        super().__init__(lst_of_modules, name)
    
    def receive_a_pulse(self, pulse, name):
        return [(module, pulse) for module in self.__destinations_modules__]
    
class FlipFlop(Module):
    def __init__(self, lst_of_modules, name) -> None:
        super().__init__(lst_of_modules, name)
        self.turn_on = False
    
    def receive_a_pulse(self, pulse, name):
        if pulse:
            return None
        self.turn_on = not self.turn_on
        return [(module, self.turn_on) for module in self.__destinations_modules__]
    
    def check_position(self):
        return self.turn_on
    
class Conjunction(Module):
    def __init__(self, lst_of_modules, name, lst_of_inputs):
        super().__init__(lst_of_modules, name)
        self.inputs = {name: LOW for name in lst_of_inputs}
    
    def receive_a_pulse(self, pulse, name):
        self.inputs[name] = pulse
        val_to_return = HIGH
        if LOW in self.inputs.values():
            val_to_return = LOW
        return [(module, val_to_return) for module in self.__destinations_modules__]
    
    def check_position(self):
        return not LOW in self.inputs.values()


class Solution:
    NAME = 'name'
    DESTINATIONS = 'dest'
    TYPE = 'type'
    
    def __init__(self, filename) -> None:
        self.get_data(filename)
        print(self.data)

    def get_data(self, filename):
        self.data, self.nums, self.data_lens = [], [], []
        with open(filename, 'r') as myfile:
            for line in myfile:
                line = line.strip().split(' -> ')
                if line[0] == 'broadcaster':
                    self.data.append({Solution.NAME: line[0], Solution.TYPE: line[0], Solution.DESTINATIONS: line[1].split(', ')})
                else:
                    self.data.append({Solution.NAME: line[0][1:], Solution.TYPE: line[0][0], Solution.DESTINATIONS: line[1].split(', ')})
        self.data.append({Solution.NAME: 'button', Solution.TYPE: 'button', Solution.DESTINATIONS: 'broadcaster'})



    def solution_1(self):
        lows, highs = [], []
        # TODO


        return 0


def main():
    print('TASK 1')
    sol = Solution('2023/Day_20/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1())
    sol = Solution('2023/Day_20/test_2.txt')
    print('test 2:', sol.solution_1())
    sol = Solution('2023/Day_20/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())


if __name__ == '__main__':
    main()
