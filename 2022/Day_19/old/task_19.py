'''
Advent of Code 
2022 day 19
my solution to tasks from day 19


solution 1 - 
solution 2 - 

'''
from copy import copy

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


def check_where_new_robot_can_be_built(data_1, data_2, robot, blueprint):
    if check_if_data_has_required_rocks(data_1, blueprint[robot]):
        return data_1
    return data_2

# knapsack algorithm
def get_max_number_of_geodes(blueprint, minutes):
    data_table = [[{ore_robot: 1, ore: x} for x in range(minutes + 1)]]
    for robot, rock in types_of_robots.items():
        print(robot, rock)
        new_dict = data_table[-1][0].copy()
        new_dict.setdefault(robot, 0)
        new_dict.setdefault(rock, 0)
        new_row = [new_dict]
        for index in range(minutes):
            pass
            # TODO
            # check if new robot can be built
            chosen_dict = copy(new_row[-1])
            determine_if_new_robot_can_be_built = check_if_data_has_required_rocks(chosen_dict, blueprint[robot])
            # add new resources
            for robot_name, rock_name in types_of_robots.items():
                if robot_name in chosen_dict.keys() and rock_name in chosen_dict.keys():
                    chosen_dict[rock_name] += chosen_dict[robot_name]
                else:
                    break
            # add new robots
            if determine_if_new_robot_can_be_built:
                chosen_dict[robot] += 1
                for rock, quantity in blueprint[robot].items():
                    chosen_dict[rock] -= quantity
            new_row.append(chosen_dict)
        print(new_row)
        data_table.append(new_row)
   # print(data_table)
    return data_table[-1][-1][geode] # need to change for geode

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
    