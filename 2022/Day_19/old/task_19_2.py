'''
Advent of Code 
2022 day 19
my solution to tasks from day 19


solution 1 - 
solution 2 - 

'''
from copy import copy
from queue import Queue

ore_robot = 'ore_robot'
ore = 'ore'
clay_robot = 'clay_robot'
clay = 'clay'
obsidian_robot = 'obsidian_robot'
obsidian = 'obsidian'
geode_robot = 'geode_robot'
geode = 'geode'
types_of_robots = {ore_robot: ore, clay_robot: clay, obsidian_robot: obsidian, geode_robot: geode}

def get_blueprints(filename):
    blueprints = []
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line.strip().split('.')
            costs = [x[x.find('costs') + 5:].replace('and', '').split() for x in line]
            blueprint_dict = {}
            for robot, cost in zip(types_of_robots.keys(), costs):
                blueprint_dict.setdefault(robot, {cost[i + 1]: int(cost[i]) for i in range(0, len(cost), 2)})
            blueprints.append(blueprint_dict)
    return blueprints

def check_if_data_has_required_rocks(data, requirements):
    for rock, quantity in requirements.items():
        if data[rock] < quantity:
            return False
    return True

def add_to_queue(act_dict, minute, queue_of_states, been_in_states):
    if tuple(act_dict.values()) not in been_in_states:
        been_in_states.add(act_dict.values())
        queue_of_states.put((copy(act_dict), minute - 1))

# A* algorithm
def get_max_number_of_geodes(blueprint, minutes):
    queue_of_states, been_in_states = Queue(), set()
    first_dict = {}
    for robot, rock in types_of_robots.items():
        first_dict.setdefault(robot, 0)
        first_dict.setdefault(rock, 0)
    first_dict[ore_robot] += 1
    queue_of_states.put((first_dict, minutes))
    been_in_states.add(tuple(first_dict.values()))
    while not queue_of_states.empty():
        act_dict, act_minute = queue_of_states.get()
        print(act_minute, act_dict)
        for robot, rock in reversed(types_of_robots.items()):
            # check if new robot can be built
            determine_if_new_robot_can_be_built = check_if_data_has_required_rocks(act_dict, blueprint[robot])
            # add new resources
            for robot_name, rock_name in types_of_robots.items():
                if robot_name in act_dict.keys() and rock_name in act_dict.keys():
                    act_dict[rock_name] += act_dict[robot_name]
                else:
                    break
            add_to_queue(act_dict, act_minute, queue_of_states, been_in_states)
            # add new robots
            if determine_if_new_robot_can_be_built:
                act_dict[robot] += 1
                for rock, quantity in blueprint[robot].items():
                    act_dict[rock] -= quantity
                add_to_queue(act_dict, act_minute, queue_of_states, been_in_states)
                break
    return max([been_in[-1] for been_in in been_in_states]) # need to change for geode

'''
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

'''

def solution_1(blueprints, minutes):
    return sum([(index + 1) * get_max_number_of_geodes(blueprint, minutes) for index, blueprint in enumerate(blueprints)])

  
def main():
    test_blueprints = get_blueprints('2022/Day_19/test.txt')
    print('test 1:', solution_1(test_blueprints, 24))
    task_blueprints = get_blueprints('2022/Day_19/task.txt')
   # print('Solution 1:', solution_1(task_blueprints, 24))
  #  print('test 2:', solution_2(test_valves, test_start_valve, 26))
   # print('Solution 2:', solution_2(task_valves, task_start_valve, 26))
    
    
if __name__ == '__main__':
    main()
    