'''
Advent of Code 
2024 day 12
my solution to tasks

before each task there is a need to get gardens areas as sets 
so in initialization there is a division for garden areas 

task 1 - for each garden area:
            calculate area: simply len of garden points set
            calculate perimeter: for each point in garden area check each neighboring point -> 
            if it is not in garden area then add 1 to perimeter
            multiply these two values and add them to result
task 2 - calculating sides is a little more complicated task:
        for each garden area:
            calculate sides:
                then put all points that not all neighboring points are in garden points set into correct sets: 
                    for up side, down side, left side and right side
                for each side set calculate number of sides (side is if points on same x or y are in growing by 1 sequence, otherwise 
                there is next side)
            
                

'''

class Solution:

    def __init__(self, filename) -> None:
        self.garden_map = []
        self.get_data(filename)
        self.max_y, self.max_x, self.min_y, self.min_x = len(self.garden_map), len(self.garden_map[0]), 0, 0
        self.dir_dict = {'up': (-1, 0),
                         'down': (1, 0), 
                         'left': (0, -1),
                         'right': (0, 1)}
        
        self.num_of_sides = {'up': (1, 0), 
                             'down': (1, 0),
                             'left': (0, 1),
                             'right': (0, 1)}
        
        self.areas = self.get_garden_areas()

    def get_data(self, filename):
        with open(filename, 'r') as myfile:
            for line in myfile:
                self.garden_map.append(line.strip())

    def get_map_value(self, point):
        return self.garden_map[point[0]][point[1]]
    
    def get_possible_points(self, point):
        new_points = set()
        for dir in self.dir_dict.values():
            new_point = (point[0] + dir[0], point[1] + dir[1])
            if self.min_y <= new_point[0] < self.max_y and self.min_x <= new_point[1] < self.max_x \
                and self.get_map_value(new_point) == self.get_map_value(point):
                new_points.add(new_point)
        return new_points

    def get_new_garden_area(self, starting_point):
        garden_area = set()
        new_points = set([starting_point])
        while len(new_points) > 0:
            garden_area = garden_area.union(new_points)
            new_new_points = set()
            for point in new_points:
                new_new_points = new_new_points.union(self.get_possible_points(point))
            new_points = new_new_points.difference(garden_area)
        return garden_area
    
    def get_garden_areas(self):
        garden_areas = []
        visited_points = set()
        for y in range(self.max_y):
            for x in range(self.max_x):
                if (y, x) in visited_points:
                    continue
                new_garden_area = self.get_new_garden_area((y, x))
                garden_areas.append(new_garden_area)
                visited_points = visited_points.union(new_garden_area)
        return garden_areas
    
    def get_garden_area(self, garden):
        return len(garden)
    
    def get_garden_perimeter(self, garden):
        perimeter = 0
        for point in garden:
            for dir in self.dir_dict.values():
                new_point = (point[0] + dir[0], point[1] + dir[1])
                if new_point not in garden:
                    perimeter += 1
        return perimeter

    def get_up_down_left_right_sides(self, garden): 
        new_sides = {key: set() for key in self.dir_dict.keys()}
        for point in garden:
            for key, direction in self.dir_dict.items():
                if (point[0] + direction[0], point[1] + direction[1]) not in garden:
                    new_sides[key].add(point)
        return new_sides

    def get_number_of_garden_sides(self, sides, indices):
        num = 0
        for x in set([a[indices[1]] for a in sides]):
            y = sorted([a[indices[0]] for a in sides if a[indices[1]] == x])
            if len(y) == 1:
                num += 1
                continue
            diffs = [y2 - y1 for y1, y2 in zip(y[:-1], y[1:])]
            num += 1 + len([a for a in diffs if a != 1])
        return num

    def get_garden_sides(self, garden):
        sides = self.get_up_down_left_right_sides(garden) 
        result = 0
        for direction, points in sides.items():
            result += self.get_number_of_garden_sides(points, self.num_of_sides[direction])
        return result

    
    def solution_1(self) -> int:
        return sum([self.get_garden_area(garden) * self.get_garden_perimeter(garden) for garden in self.areas])
    
    
    def solution_2(self) -> int:
        return sum([self.get_garden_area(garden) * self.get_garden_sides(garden) for garden in self.areas])



    

def main():
    print('TASK 1')
    sol = Solution('2024/Day_12/test.txt')
    area = sol.get_new_garden_area((0, 0))
    print(sol.get_garden_sides(area))
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 1930')
    print('test 1:', sol.solution_2(), 'should equal 1206')
    sol = Solution('2024/Day_12/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2())
   

if __name__ == '__main__':
    main()

