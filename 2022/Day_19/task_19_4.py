'''
Advent of Code 
2022 day 19
my solution to tasks from day 19
*** new version as my seems to fail - wrong results for tests
*** reimplemented solution from reddit: https://pastebin.com/KDTmtHCk

solution 1 - 
solution 2 - 

'''

import re
from functools import reduce

ore = 'ore'
clay = 'clay'
obsidian = 'obsidian'
geode = 'geode'
types_of_robots = (ore, clay, obsidian, geode)

class Blueprint:
    __slots__ = ("id", "cost", "useful")

    def __init__(self, input_string: str) -> None:
        vals = [int(i) for i in re.findall(r"\d+", input_string)]
        self.id = vals[0]
        self.cost = {
            ore: {ore: vals[1]},
            clay: {ore: vals[2]},
            obsidian: {ore: vals[3], clay: vals[4]},
            geode: {ore: vals[5], obsidian: vals[6]}
        }
        self.useful = {
            ore: max(self.cost[clay][ore],
                       self.cost[obsidian][ore],
                       self.cost[geode][ore]),
            clay: self.cost[obsidian][clay],
            obsidian: self.cost[geode][obsidian],
            geode: 999
        }
        
class State:
    __slots__ = ("robots", "resources", "ignored")

    def __init__(self, robots: dict = None, resources: dict = None,
                 ignored: list = None):
        self.robots = robots.copy() if robots else {
            ore: 1, clay: 0, obsidian: 0, geode: 0
        }
        self.resources = resources.copy() if resources else {
            ore: 0, clay: 0, obsidian: 0, geode: 0
        }
        self.ignored = ignored.copy() if ignored else []

    def copy(self) -> "State":
        return State(self.robots, self.resources, self.ignored)

    def __gt__(self, other):
        return self.resources[geode] > other.resources[geode]

    def __repr__(self):
        return f"{{robots: {self.robots}, resources: {self.resources}}}"

        
def get_blueprints(filename):
    blueprints = []
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line.strip()
            blueprints.append(Blueprint(line))
    return blueprints


def add_materials(state):
    state = state.copy()
    for robot, quantity in state.robots.items():
        state.resources[robot] += quantity
    return state

def build_robot(state, robot, blueprint):
    act_state = state.copy()
    act_state.ignored = []
    act_state.robots[robot] += 1
    for rock, quantity in blueprint.cost[robot].items():
        act_state.resources[rock] -= quantity
    return act_state


def get_max_number_of_geodes_for_a_blueprint(blueprint, prior_states, minutes):
    time_remaining = minutes - len(prior_states)
    curr_state = prior_states[-1]
    
    # determine what can be done in current state
    options = [] # list[str]
    if time_remaining >= 0:
        # look for something affordable and useful and not ignored last time
        for robot, cost in blueprint.cost.items():
            if (curr_state.robots[robot] < blueprint.useful[robot]
                    and all(curr_state.resources[rock] >= quantity for rock, quantity in cost.items())
                    and robot not in curr_state.ignored):
                options.append(robot)
                
        # if geode robot can be purchased, do it and do not look at any other robot
        if geode in options:
            options = [geode]
        # if time is less than 1 it does not matter if any other robot is purchased so limit the options
        elif time_remaining < 1:
            options = []
        else:
            # removing the options that build resources more than 2 phases back
            if ((curr_state.robots[clay] > 3 or curr_state.robots[obsidian]
                 or obsidian in options) and ore in options):
                options.remove("ore")
            if ((curr_state.robots[obsidian] > 3 or curr_state.robots[geode]) and clay in options):
                options.remove(clay)
        
        # copy curr_state, add materials and save it to next_state
        next_state = add_materials(curr_state)
        
        # the 'do nothing' option
        next_state.ignored += options
        results = [get_max_number_of_geodes_for_a_blueprint(blueprint, prior_states + [next_state], minutes)]

        # the rest of the options
        for opt in options:
            next_state_opt = build_robot(next_state, opt, blueprint)
            results.append(
                get_max_number_of_geodes_for_a_blueprint(blueprint, prior_states + [next_state_opt], minutes)
            )

        return max(results)

    return prior_states[-1].resources[geode], prior_states
    

def solution_1(blueprints, minutes):
    return sum([blueprint.id * get_max_number_of_geodes_for_a_blueprint(blueprint, [State()], minutes)[0] for blueprint in blueprints])

def solution_2(blueprints, minutes):
    blueprints = blueprints[:3]
    return reduce(lambda x, y: x * y, [get_max_number_of_geodes_for_a_blueprint(blueprint, [State()], minutes)[0] for blueprint in blueprints])


def main():
    test_blueprints = get_blueprints('2022/Day_19/test.txt')
    print('test 1:', solution_1(test_blueprints, 24))
    task_blueprints = get_blueprints('2022/Day_19/task.txt')
    print('Solution 1:', solution_1(task_blueprints, 24))
    print('test 2:', solution_2(test_blueprints, 32))
    print('Solution 2:', solution_2(task_blueprints, 32))
    
    
if __name__ == '__main__':
    main()
