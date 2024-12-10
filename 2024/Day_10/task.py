'''
Advent of Code 
2024 day 10
my solution to tasks

task 1 - 


'''

from tqdm import tqdm

class Solution:

    def __init__(self, filename) -> None:
        self.top_map = {}
        self.trailheads = set()
        self.get_data(filename)
        self.directions = set([(0, 1), (1, 0), (-1, 0), (0, -1)])

    def get_data(self, filename):
        with open(filename, 'r') as myfile:
            for y, line in enumerate(myfile):
                for x, val in enumerate(line.strip()):
                    self.top_map.setdefault((y, x), int(val))
                    if val == '0':
                        self.trailheads.add((y, x))
    
    def get_map_value(self, point):
        return self.top_map.get(point, -1)

    def get_possible_moves(self, point, val):
        for dir in self.directions:
            new_point = (point[0] + dir[0], point[1] + dir[1])
            if self.get_map_value(new_point) - val == 1:
                yield new_point
    
    def solution_1(self) -> int:
        result = 0
        for trailhead in tqdm(self.trailheads):
            visited_points = set()
            visited_points.add(trailhead)
            act_positions = set()
            act_positions.add(trailhead)
            for _ in range(9):
                new_act_positions = set()
                for point in act_positions:
                    for new_point in self.get_possible_moves(point, self.get_map_value(point)):
                        if new_point not in visited_points:
                            visited_points.add(new_point)
                            new_act_positions.add(new_point)
                act_positions = new_act_positions
            result += len(act_positions)
        return result
    


    
    def solution_2(self) -> int:
        result = 0
        for trailhead in tqdm(self.trailheads):
            visited_points = set()
            visited_points.add(trailhead)
            act_positions = set()
            act_positions.add(trailhead)
            how_many_routes_led_here = {}
            how_many_routes_led_here.setdefault(trailhead, 1)
            for _ in range(9):
                new_act_positions = set()
                for point in act_positions:
                    for new_point in self.get_possible_moves(point, self.get_map_value(point)):
                        how_many_routes_led_here.setdefault(new_point, 0)
                        how_many_routes_led_here[new_point] += how_many_routes_led_here.get(point, 0)
                        if new_point not in visited_points:
                            visited_points.add(new_point)
                            new_act_positions.add(new_point)
                
                act_positions = new_act_positions
            for position in act_positions:
                result += how_many_routes_led_here[position]
        return result



    

def main():

    print('TASK 1')
    sol = Solution('2024/Day_10/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 36')
    print('test 1:', sol.solution_2(), 'should equal 81')
    sol = Solution('2024/Day_10/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2())
   


if __name__ == '__main__':
    main()
