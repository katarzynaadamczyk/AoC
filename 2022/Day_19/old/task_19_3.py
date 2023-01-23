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

# earlier version
'''
def check_if_data_has_required_rocks(data, requirements):
    for rock, quantity in requirements.items():
        if data[rock] < quantity:
            return False
    return True
'''
# new version
def check_if_data_has_required_rocks(data, blueprint, max_no_of_robots):
    robots_that_cannot_be_built = set()
    for robot, requirements in blueprint.items():
        if max_no_of_robots[robot] <= data[robot]:
            robots_that_cannot_be_built.add(robot)
            continue
        for rock, quantity in requirements.items():
            if data[rock] < quantity:
                robots_that_cannot_be_built.add(robot)
                break
    return set(blueprint.keys()).difference(robots_that_cannot_be_built)

def add_to_queue(act_dict, minute, queue_of_states): #, been_in_states):
   # if tuple(act_dict.values()) not in been_in_states:
   #     been_in_states.add(act_dict.values())
    queue_of_states.put((minute + 1, copy(act_dict)))
        
def get_max_no_of_robots(blueprint, minutes):
    tmp, ret_dict = {}, {}
    for material in types_of_robots.values():
        tmp.setdefault(material, 0)
    for robot_dict in blueprint.values():
        for material, cost in robot_dict.items():
            if cost > tmp[material]:
                tmp[material] = cost
    for robot, material in types_of_robots.items():
        ret_dict.setdefault(robot, tmp[material])
    ret_dict[geode_robot] = minutes
    return ret_dict

def add_materials(state):
    for robot, material in types_of_robots.items():
        state[material] += state[robot]
 #   print('state', state)

def build_robot(state, robot, blueprint):
    act_dict = copy(state)
    act_dict[robot] += 1
    for rock, quantity in blueprint[robot].items():
        act_dict[rock] -= quantity
    return act_dict

# A* algorithm
def get_max_number_of_geodes(blueprint, minutes):
  #  queue_of_states, been_in_states, max_no_of_robots = Queue(), set(), get_max_no_of_robots(blueprint, minutes)
    queue_of_states, max_no_of_robots = Queue(), get_max_no_of_robots(blueprint, minutes)
    max_geode, max_obsidian_robot = [0 for _ in range(minutes + 1)], [0 for _ in range(minutes + 1)]
  #  queue_of_states, max_no_of_robots, max_geode = Queue(), get_max_no_of_robots(blueprint, minutes), 0
    first_dict = {}
    for robot, rock in types_of_robots.items():
        first_dict.setdefault(robot, 0)
        first_dict.setdefault(rock, 0)
    first_dict[ore_robot] += 1
    queue_of_states.put((0, first_dict))
   # been_in_states.add(tuple(first_dict.values()))
    while not queue_of_states.empty():
        act_minute, act_dict = queue_of_states.get()
        max_geode[act_minute] = max(max_geode[act_minute], act_dict[geode])
        max_obsidian_robot[act_minute] = max(max_obsidian_robot[act_minute], act_dict[obsidian_robot])
        if act_minute >= minutes or act_dict[geode] < max_geode[act_minute] or act_dict[obsidian_robot] < max_obsidian_robot[act_minute]:
            continue
        
        # check which robots can be built
        robots_can_be_built = check_if_data_has_required_rocks(act_dict, blueprint, max_no_of_robots)
        add_materials(act_dict)
       # if len(robots_can_be_built) == 0:
        add_to_queue(act_dict, act_minute, queue_of_states) #, been_in_states)
        if geode_robot in robots_can_be_built:
            act_dict = build_robot(act_dict, geode_robot, blueprint)
           # del queue_of_states
           # queue_of_states = Queue()
            add_to_queue(act_dict, act_minute, queue_of_states) #, been_in_states)
        elif obsidian_robot in robots_can_be_built:
            act_dict = build_robot(act_dict, obsidian_robot, blueprint)
            add_to_queue(act_dict, act_minute, queue_of_states) #, been_in_states)
        else:
            for robot in robots_can_be_built:
                # build robot
                act_dict = build_robot(act_dict, robot, blueprint)
                # add to queue
                add_to_queue(act_dict, act_minute, queue_of_states) #, been_in_states)
    print(max_geode[minutes])
    return max_geode[minutes]
    return max([been_in[-1] for been_in in been_in_states]) # need to change for geode


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
    