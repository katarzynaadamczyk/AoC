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

def add_to_queue(act_dict, minute, queue_of_states, been_in_states):
    if tuple(act_dict.values()) not in been_in_states:
        been_in_states.add(act_dict.values())
        queue_of_states.put((copy(act_dict), minute + 1))
        
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
    print('state', state)


# A* algorithm
def get_max_number_of_geodes(blueprint, minutes):
    queue_of_states, been_in_states, max_no_of_robots, max_geode = Queue(), set(), get_max_no_of_robots(blueprint, minutes), 0
    first_dict = {}
    for robot, rock in types_of_robots.items():
        first_dict.setdefault(robot, 0)
        first_dict.setdefault(rock, 0)
    first_dict[ore_robot] += 1
    queue_of_states.put((first_dict, 0))
    been_in_states.add(tuple(first_dict.values()))
    while not queue_of_states.empty():
        act_dict, act_minute = queue_of_states.get()
        print(act_minute, act_dict, max_geode)
        if act_minute >= 24:
            max_geode = max(act_dict[geode], max_geode)
            continue
        # check which robots can be built
        robots_can_be_built = check_if_data_has_required_rocks(act_dict, blueprint, max_no_of_robots)
        print(robots_can_be_built)
        if len(robots_can_be_built) == 0:
            add_materials(act_dict)
            add_to_queue(act_dict, act_minute, queue_of_states, been_in_states)
        else:
            for robot in robots_can_be_built:
                # build robot
                # add to queue
                
                pass
       # return 0
    '''
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
                break'''
    return max_geode
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
    