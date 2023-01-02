'''
Advent of Code 
2022 day 17
my solution to tasks from day 17


solution 1 - 
solution 2 - 

'''

class Simulation:
    
    flat_rock = lambda y: set([(x, y + 4) for x in range(3, 7)])
    cross_rock = lambda y: set([(3, y + 5), (4, y + 4), (4, y + 5), (4, y + 6), (5, y + 5)])
    l_shape_rock = lambda y: set([(3, y + 4), (4, y + 4), (5, y + 4), (5, y + 5), (5, y + 6)])
    line_rock = lambda y: set([(3, y + i) for i in range(4, 8)])
    brick_rock = lambda y: set([(3, y + 4), (4, y + 4), (3, y + 5), (4, y + 5)])
    
    rock_min_x = lambda rock: min(rock, key=lambda point: point[0])[0]
    rock_max_x = lambda rock: max(rock, key=lambda point: point[0])[0]
    
    def __init__(self, wind_blows):
        self.wall_left, self.wall_right = 1, 7
        self.tower = set()
        for x in range(1, 8):
            self.tower.add((x, 0))
        self.wind_blows = wind_blows
        self.len_wind_blows = len(self.wind_blows)
        self.tower_height = 0
    
    def rock_generator(self, i):
        if i % 5 == 0:
            return Simulation.flat_rock(self.tower_height)
        if i % 5 == 1:
            return Simulation.cross_rock(self.tower_height)
        if i % 5 == 2:
            return Simulation.l_shape_rock(self.tower_height)
        if i % 5 == 3:
            return Simulation.line_rock(self.tower_height)
        if i % 5 == 4:
            return Simulation.brick_rock(self.tower_height)            
        
    def get_max_y(self):
        return max(self.tower, key=lambda point: point[1])[1]
    
    def simulate(self, no_of_rocks):
        self.no_of_wind_blows = 0
        self.tower_height = 0
        for i in range(no_of_rocks):
            new_rock = self.rock_generator(i)
            # first wind blow, then it will be done in reverse order
            new_rock = self.wind_blow_on_rock(new_rock)
            while self.rock_can_move(new_rock):
                # go_down
                new_rock = self.rock_go_down(new_rock)
                # wind blows
                new_rock = self.wind_blow_on_rock(new_rock)
            self.tower = self.tower.union(new_rock)
            self.tower_height = self.get_max_y()
            
    def simulate_2(self, no_of_rocks):
        self.no_of_wind_blows = 0
        self.tower_height = 0
        self.heights, self.differences = [], []
        for i in range(2001):
            new_rock = self.rock_generator(i)
            # first wind blow, then it will be done in reverse order
            new_rock = self.wind_blow_on_rock(new_rock)
            while self.rock_can_move(new_rock):
                # go_down
                new_rock = self.rock_go_down(new_rock)
                # wind blows
                new_rock = self.wind_blow_on_rock(new_rock)
            self.tower = self.tower.union(new_rock)
            self.tower_height = self.get_max_y()
            self.no_of_wind_blows = self.no_of_wind_blows % self.len_wind_blows
            self.heights.append(self.tower_height)
        for h1, h2 in zip(self.heights[:-1], self.heights[1:]):
            self.differences.append(h2 - h1)
        long_len_str = ' '.join(str(x) for x in self.differences[100:200])
        differences_str = ' '.join(str(x) for x in self.differences)
        first_match = differences_str.find(long_len_str)
        second_match = differences_str.find(long_len_str, first_match + 1)
        first_match = differences_str[:first_match].count(' ') + 1
        second_match = differences_str[:second_match].count(' ') + 1
        diff = second_match - first_match
        first_height = self.heights[first_match]
        second_height = self.heights[second_match]
        self.result_sec_simulation = ((no_of_rocks - first_match) // diff) * (second_height - first_height) + self.heights[first_match + (no_of_rocks - first_match) % diff] - 1

        
    def get_second_result(self):
        return self.result_sec_simulation
    
    def wind_blow_on_rock(self, rock):
        act_wind_dir = self.wind_blows[self.no_of_wind_blows % self.len_wind_blows]
        self.no_of_wind_blows += 1
        if act_wind_dir == '>' and Simulation.rock_max_x(rock) < self.wall_right:
            maybe_result = set([(point[0] + 1, point[1]) for point in rock])
            if len(maybe_result.intersection(self.tower)) == 0:
                return maybe_result
        elif act_wind_dir == '<' and Simulation.rock_min_x(rock) > self.wall_left:
            maybe_result = set([(point[0] - 1, point[1]) for point in rock])
            if len(maybe_result.intersection(self.tower)) == 0:
                return maybe_result
        return rock

    def rock_go_down(self, rock):
        return set([(point[0], point[1] - 1) for point in rock])
    
    def rock_can_move(self, rock):
        return len(self.tower.intersection(self.rock_go_down(rock))) == 0
    
    def print_simulation(self, start_line=1):
        result = []
        for y in range(start_line, self.tower_height + 1):
            act_line = ['|'] + ['.' for _ in range(7)] + ['|']
            points = list(filter(lambda point: point[1] == y, self.tower))
            for point in points:
                act_line[point[0]] = '#'
            result.append(''.join(act_line))
        print('\n'.join(reversed(result)))
        print('|' + '-' * 7 + '|')



def get_wind_blows(filename):
    with open(filename, 'r') as myfile:
        for line in myfile:
            wind_blows = line.strip()
    return wind_blows


def solution_1(wind_blows, no_of_rocks):
    solution_simulator = Simulation(wind_blows)
    solution_simulator.simulate(no_of_rocks)
   # solution_simulator.print_simulation(solution_simulator.get_max_y() - 20)
    return solution_simulator.get_max_y()

def solution_2(wind_blows, no_of_rocks):
    solution_simulator = Simulation(wind_blows)
    solution_simulator.simulate_2(no_of_rocks)
  #  solution_simulator.print_simulation()
    return solution_simulator.get_second_result()

  
def main():
    test_wind_blows = get_wind_blows('2022/Day_17/test.txt')
  #  print('test 1:', solution_1(test_wind_blows, 2022))
    task_wind_blows = get_wind_blows('2022/Day_17/task.txt')
   # print('Solution 1:', solution_1(task_wind_blows, 2022))
    print('test 2:', solution_2(test_wind_blows, 1000000000000))
    print('Solution 2:', solution_2(task_wind_blows, 1000000000000))
    
    
if __name__ == '__main__':
    main()
    