'''
Advent of Code 
2022 day 16
my solution to tasks from day 16

First was to eliminate the valves with 0 pressure and get min paths between non-zero-pressure valves, so for that is function get_dict_of_min_paths.
solution 1 - With a help of a queue check all possible options to open valves in given minutes. 
act_pressure is max pressure that can be reached when opening the valves in the given minutes.
been_in_states eliminates duplication of coming back to same valve and thanks to it the result is given right away.
solution 2 - Similar to solution 1 although there is more counting as there is more possible options as the elephant is helping out.

'''

from copy import copy
from queue import PriorityQueue, Queue

class Valve:
    def __init__(self, name, next_valves, pressure=0) -> None:
        self.name = name
        self.next_valves = next_valves
        self.pressure = pressure
    
    def get_pressure(self):
        return self.pressure
    
    def get_next_valves(self):
        return self.next_valves
    
    def __repr__(self):
        return self.name + ': pressure - ' + str(self.pressure) + ', next valves: ' + str(self.next_valves)

    
    def __str__(self):
        return self.name + ': pressure - ' + str(self.pressure) + ', next valves: ' + str(self.next_valves)


def get_valves(filename):
    valves, start_valve = {}, 'AA' # name: Valve(name, pressure, set_of_next_valves)
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line.strip()
            name = line[line.find(' ') + 1:line.find(' ', line.find(' ') + 1)]
            pressure = int(line[line.find('=')+1:line.find(';')])
            next_valves = line[line.find(' ', line.find('valv'))+1:].split(', ')
            valves.setdefault(name, Valve(name, next_valves, pressure))
    return valves, start_valve


def find_min_path(valves, valve_1, valve_2):
    queue_of_positions, visited_points = PriorityQueue(), set()
    visited_points.add(valve_1)
    queue_of_positions.put((0, valve_1))
    act_pos = valve_1
    while not queue_of_positions.empty():
        act_priority, act_pos = queue_of_positions.get()
        if act_pos == valve_2:
            return act_priority
        for valve in valves[act_pos].get_next_valves():
            if valve not in visited_points:
                visited_points.add(act_pos)
                queue_of_positions.put((act_priority + 1, valve))


def get_dict_of_min_paths(valves, start_valve):
    valves_with_pressure = [start_valve] + list(filter(lambda valve: valves[valve].get_pressure() > 0, valves))
    valves_with_pressure_dict = {valve: {} for valve in valves_with_pressure}
    for index, valve_1 in enumerate(valves_with_pressure):
        for valve_2 in valves_with_pressure[index + 1:]:
            act_path = find_min_path(valves, valve_1, valve_2) + 1 # + 1 as opening the valve costs also 1 minute
            valves_with_pressure_dict[valve_1][valve_2] = act_path
            valves_with_pressure_dict[valve_2][valve_1] = act_path
    return valves_with_pressure_dict


def solution_1(valves, start_valve, minutes):
    valves_with_pressure_dict = get_dict_of_min_paths(valves, start_valve)
    queue_of_states, opened_valves, been_in_states = Queue(), set(), set()
    max_opened_valves = len(valves_with_pressure_dict)
    opened_valves.add(start_valve)
    been_in_states.add((0, minutes, start_valve))
    queue_of_states.put((start_valve, 0, minutes, opened_valves))
    while not queue_of_states.empty():
        act_valve, act_pressure, minutes_left, opened_valves = queue_of_states.get()
        if len(opened_valves) == max_opened_valves:
            continue
        for valve in (set(valves_with_pressure_dict.keys()) - opened_valves):
            if valves_with_pressure_dict[act_valve][valve] <= minutes_left:
                new_opened_valves = copy(opened_valves)
                new_opened_valves.add(valve)
                new_minutes_left = minutes_left - valves_with_pressure_dict[act_valve][valve]
                new_act_pressure = act_pressure + new_minutes_left * valves[valve].get_pressure()
                if (new_act_pressure, minutes_left, valve) not in been_in_states:
                    queue_of_states.put((valve, new_act_pressure, new_minutes_left, new_opened_valves))
                    been_in_states.add((new_act_pressure, minutes_left, valve))
    return max(been_in_states)

            
def solution_2(valves, start_valve, minutes):
    valves_with_pressure_dict = get_dict_of_min_paths(valves, start_valve)
    max_opened_valves = len(valves_with_pressure_dict)
    queue_of_states, opened_valves, been_in_states = Queue(), set(), set()
    opened_valves.add(start_valve)
    been_in_states.add((0, minutes * 2, start_valve))
    queue_of_states.put((0, start_valve, start_valve, minutes, minutes, opened_valves))
    while not queue_of_states.empty():
        act_pressure, my_act_valve, elephant_act_valve, my_minutes_left, elephant_minutes_left, opened_valves = queue_of_states.get()
        if len(opened_valves) == max_opened_valves:
            continue
        for valve in (set(valves_with_pressure_dict.keys()) - opened_valves):
            new_opened_valves = copy(opened_valves)
            new_opened_valves.add(valve)
            if valves_with_pressure_dict[my_act_valve][valve] <= my_minutes_left:
                my_new_minutes_left = my_minutes_left - valves_with_pressure_dict[my_act_valve][valve]
                new_act_pressure = act_pressure + my_new_minutes_left * valves[valve].get_pressure()
                if (new_act_pressure, my_new_minutes_left + elephant_minutes_left, elephant_act_valve, valve) not in been_in_states and \
                    (new_act_pressure, my_new_minutes_left + elephant_minutes_left, valve, elephant_act_valve) not in been_in_states: # \
                    queue_of_states.put((new_act_pressure, valve, elephant_act_valve, my_new_minutes_left, elephant_minutes_left, new_opened_valves))
                    been_in_states.add((new_act_pressure, my_new_minutes_left + elephant_minutes_left, elephant_act_valve, valve))
            if valves_with_pressure_dict[elephant_act_valve][valve] <= elephant_minutes_left:
                elephant_new_minutes_left = elephant_minutes_left - valves_with_pressure_dict[elephant_act_valve][valve]
                new_act_pressure = act_pressure + elephant_new_minutes_left * valves[valve].get_pressure()
                if (new_act_pressure, my_minutes_left + elephant_new_minutes_left, my_act_valve, valve) not in been_in_states and \
                    (new_act_pressure, my_minutes_left + elephant_new_minutes_left, valve, my_act_valve) not in been_in_states:
                    queue_of_states.put((new_act_pressure, my_act_valve, valve, my_minutes_left, elephant_new_minutes_left, new_opened_valves))
                    been_in_states.add((new_act_pressure, my_minutes_left + elephant_new_minutes_left, my_act_valve, valve))
    return max(been_in_states)
        

def main():
    test_valves, test_start_valve = get_valves('2022/Day_16/test.txt')
    print('test 1:', solution_1(test_valves, test_start_valve, 30)) # should be 1651
    task_valves, task_start_valve = get_valves('2022/Day_16/task.txt')
    print('Solution 1:', solution_1(task_valves, task_start_valve, 30)) # should be 2359
    print('test 2:', solution_2(test_valves, test_start_valve, 26)) # should be 1707
    print('Solution 2:', solution_2(task_valves, task_start_valve, 26)) # should be 2999
    
    
if __name__ == '__main__':
    main()
    