'''
Advent of Code 
2023 day 12
my solution to task 1 & 2

solution 1 - 

solution 2 - 

'''

from queue import PriorityQueue
from math import lcm
from copy import copy

HIGH = True # high pulse
LOW = False # low pulse

class Module:
    def __init__(self, lst_of_modules, name):
        self.__name__ = name
        self.__destinations_modules__ = []
        for arg in lst_of_modules:
            self.__destinations_modules__.append(arg)

    def receive_a_pulse(self, pulse, name):
        return [(module, pulse) for module in self.__destinations_modules__]

    def check_position(self):
        return True
    
    def get_inputs(self):
        return []

class Button(Module):
    def __init__(self, lst_of_modules, name) -> None:
        super().__init__(lst_of_modules, name)
    
    def receive_a_pulse(self, pulse, name):
        return super().receive_a_pulse(pulse, name)

    
class Broadcaster(Module):
    def __init__(self, lst_of_modules, name):
        super().__init__(lst_of_modules, name)

    def receive_a_pulse(self, pulse, name):
        return super().receive_a_pulse(pulse, name)

    
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
        return not self.turn_on
    
class Conjunction(Module):
    def __init__(self, lst_of_modules, name, lst_of_inputs):
        super().__init__(lst_of_modules, name)
        self.inputs = {name: LOW for name in lst_of_inputs}
    
    def receive_a_pulse(self, pulse, name):
        self.inputs[name] = pulse
        val_to_return = LOW
        if LOW in self.inputs.values():
            val_to_return = HIGH
        return [(module, val_to_return) for module in self.__destinations_modules__]
    
    def check_position(self):
        return not sum(self.inputs.values())
    
    def get_inputs(self):
        return self.inputs


class Solution:

    NAME = 'name'
    DESTINATIONS = 'dest'
    TYPE = 'type'
    BROAD = 'broadcaster'
    BUTTON = 'button'
    FLIPFLOP = '%'
    CONJUNCTION = '&'


    def __init__(self, filename) -> None:
        self.get_data(filename)
      #  print(self.data)


    def get_data(self, filename):
        self.data, self.nums, self.data_lens = [], [], []
        with open(filename, 'r') as myfile:
            for line in myfile:
                line = line.strip().split(' -> ')
                if line[0] == Solution.BROAD:
                    self.data.append({Solution.NAME: line[0], Solution.TYPE: line[0], Solution.DESTINATIONS: line[1].split(', ')})
                else:
                    self.data.append({Solution.NAME: line[0][1:], Solution.TYPE: line[0][0], Solution.DESTINATIONS: line[1].split(', ')})
        self.data.append({Solution.NAME: Solution.BUTTON, Solution.TYPE: Solution.BUTTON, Solution.DESTINATIONS: [Solution.BROAD]})


    def create_button(self, name, destinations):
        return Button(destinations, name)


    def create_broadcaster(self, name, destinations):
        return Broadcaster(destinations, name)
    

    def create_flipflop(self, name, destinations):
        return FlipFlop(destinations, name)

    
    def create_conjunction(self, name, destinations):
        inputs = []
        for module in self.data:
            if name in module[Solution.DESTINATIONS]:
                inputs.append(module[Solution.NAME])
        return Conjunction(destinations, name, inputs)


    def create_modules(self):
        module_function_dict = {Solution.BROAD: Solution.create_broadcaster,
                                Solution.BUTTON: Solution.create_button,
                                Solution.CONJUNCTION: Solution.create_conjunction,
                                Solution.FLIPFLOP: Solution.create_flipflop}
        self.lst_of_modules = {}
        for module in self.data:
            new_module = module_function_dict[module[Solution.TYPE]](self, module[Solution.NAME], module[Solution.DESTINATIONS])
            self.lst_of_modules.setdefault(module[Solution.NAME], new_module)

    
    def total_check(self):
        for module in self.lst_of_modules.values():
            if not module.check_position():
                return False
        return True

    
    def push_the_button(self):
        act_low, act_high = -1, 0
        pulses_queue = PriorityQueue()
        pulses_queue.put((0, Solution.BUTTON, LOW, Solution.BUTTON))
        while not pulses_queue.empty():
            act_step, module, pulse, prev_module = pulses_queue.get()
            if pulse == HIGH:
                act_high += 1
            else:
                act_low += 1
            if module in self.lst_of_modules.keys():
                act_iter = self.lst_of_modules[module].receive_a_pulse(pulse, prev_module)
                if act_iter is not None:
                    for new_module, new_pulse in act_iter:
                        pulses_queue.put((act_step + 1, new_module, new_pulse, module)) 

        return (act_low, act_high)
        

    def solution_1(self, iterations=1000):
        self.create_modules()
        lows, highs = [], []
        i = 0
        while i < iterations:
            i += 1
            new_low, new_high = self.push_the_button()
            lows.append(new_low)
            highs.append(new_high)
            if self.total_check():
                break
      #  print(lows)
      #  print(highs)
        return (sum(lows) * iterations // i + sum(lows[:iterations % i])) * (sum(highs) * iterations // i + sum(highs[:iterations % i])) 


    def push_the_button_2(self, names_dict, i):
        pulses_queue = PriorityQueue()
        pulses_queue.put((0, Solution.BUTTON, LOW, Solution.BUTTON))
        while not pulses_queue.empty():
            act_step, module, pulse, prev_module = pulses_queue.get()
            if module in self.lst_of_modules.keys():
                act_iter = self.lst_of_modules[module].receive_a_pulse(pulse, prev_module)
                if act_iter is not None:
                    for new_module, new_pulse in act_iter:
                        pulses_queue.put((act_step + 1, new_module, new_pulse, module)) 
                        if module in names_dict.keys() and new_pulse == HIGH:
                            names_dict[module].append((i, act_step + 1))
        for val in names_dict.values():
            if len(val) == 0:
                return False
        return True

    def solution_2(self, iterations=10000, name='jq'):
        self.create_modules()
        i = 0
        names_dict = {}
        for input_name in self.lst_of_modules[name].get_inputs():
            names_dict.setdefault(input_name, copy([]))
        while i < iterations:
            i += 1
            done = self.push_the_button_2(names_dict, i)
            if done:
                break
        return lcm(*[x[0][0] for x in names_dict.values()]) 


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
    sol = Solution('2023/Day_20/task.txt')
    print('SOLUTION 2')
    print('Solution 2:', sol.solution_2())



if __name__ == '__main__':
    main()
