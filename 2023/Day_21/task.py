'''
Advent of Code 
2023 day 21
my solution to task 1 & 2

solution 1 - create a set of points that are accessible at each iteration. So, at iteration 0 it is only starting point. Then for each iteration check
accessible positions for each point and add them to new set of points. Then delete old set and replace it with a new one. At the end we get a set of 
points that are accessible at last iteration. Just get their length and it is result.

solution 2 - I looked at my task data and then solved this task and based on this is made my solution. I replaced some parts of code of part 1 
so that it is one solution for both parts. I mean -> in part one I kept all points data for each iteration. In part 2 I replaced function solution_1
with two functions ->  get_gardener_positions and solution_1, where the last one gives the answer to task 1, and the first one gives the number of available
positions at each iteration. 
I checked that the answer is the number of available points at odd positions of a diamond figure. Then I found the equation and there we go.

'''

from itertools import product

class Solution:

    ROCK = '#'
    GARDEN = '.'


    def __init__(self, filename, start='S') -> None:
        self.get_data(filename, start)


    def get_data(self, filename, start):
        self.data, self.nums, self.data_lens = [], [], []
        with open(filename, 'r') as myfile:
            y = 0
            for line in myfile:
                if start in line:
                    self.start_pos = (y, line.find(start))
                    line = line.replace(start, Solution.GARDEN)
                self.data.append(line.strip())
                y += 1
        self.max_y, self.min_y = y, 0
        self.max_x, self.min_x = len(self.data[0]), 0
        


    def get_map_value(self, position):
        return self.data[position[0] % self.max_y][position[1] % self.max_x]

    def get_new_positions(self, position):
        # up  
        if position[0] - 1 >= self.min_y and self.get_map_value((position[0] - 1, position[1])) == Solution.GARDEN:
            yield (position[0] - 1, position[1])

        # down  
        if position[0] + 1 < self.max_y and self.get_map_value((position[0] + 1, position[1])) == Solution.GARDEN:
            yield (position[0] + 1, position[1])

        # left  
        if position[1] - 1 >= self.min_x and self.get_map_value((position[0], position[1] - 1)) == Solution.GARDEN:
            yield (position[0], position[1] - 1)
        

        #  right 
        if position[1] + 1 < self.max_x and self.get_map_value((position[0], position[1] + 1)) == Solution.GARDEN:
            yield (position[0], position[1] + 1)

    

    def solution_1(self, start_pos=(5,5), iterations=6):
        gardener_positions = self.get_gardener_positions(start_pos, iterations)
        return gardener_positions[-1] if (iterations + 1) % 2 == len(gardener_positions) % 2 else gardener_positions[-2]
    

    def get_gardener_positions(self, start_pos=(5,5), iterations=6):
        act_gardener_positions = set()
        act_gardener_positions.add(start_pos)
        len_of_gardener_positions = [1]
        for _ in range(iterations):
            new_positions = set()
            for position in act_gardener_positions:
                for new_position in self.get_new_positions(position):
                    new_positions.add(new_position)
            len_of_gardener_positions.append(len(new_positions))
            del act_gardener_positions
            act_gardener_positions = new_positions
            if len(len_of_gardener_positions) > 2 and len_of_gardener_positions[-1] == len_of_gardener_positions[-3]:
                return len_of_gardener_positions
        return len_of_gardener_positions
    
    def get_parameter_diag(self, coordinate, steps):
        result = 0
        for point in product((coordinate, self.max_x - 1 - coordinate), repeat=2):
            result += self.solution_1(start_pos=point, iterations=steps)
        return result
    
    
    def get_parameter_hor_ver(self, coordinate_1, coordinate_2, coordinate_3, steps):
        result = 0
        for point in [(coordinate_1, coordinate_2), (coordinate_2, coordinate_1), (coordinate_1, coordinate_3), (coordinate_3, coordinate_1)]:
            result += self.solution_1(start_pos=point, iterations=steps)
        return result
    
    def solution_2(self, steps=50, start_pos=(5,5)):
        N = steps // self.max_y
        print(N)
        gardener_positions = self.get_gardener_positions(start_pos=start_pos, iterations=steps)
        if len(gardener_positions) % 2 == 0: # as I add one position for 0 step
            neg = gardener_positions[-1]
            pos = gardener_positions[-2]
        else:
            neg = gardener_positions[-2]
            pos = gardener_positions[-1]
        # counts 
        pos_prim = self.get_parameter_diag(0, self.max_x // 2 - 1)
        neg_prim = self.get_parameter_diag(0, self.max_x + self.max_x // 2 - 1) 
        neg_bis = self.get_parameter_hor_ver(start_pos[0], 0, self.max_x - 1, self.max_x - 1)
        result = N ** 2 * pos + N * pos_prim + (N - 1) ** 2 * neg + (N - 1) * neg_prim + neg_bis
        return result


def main():
    print('TASK 1')
    sol = Solution('2023/Day_21/test.txt')
    print('TEST 1')
    print(sol.start_pos)
    print(sol.max_x, sol.max_y)
    print('test 1 -    6:', sol.solution_1(iterations=6))
    print('test 1 -  101:', sol.solution_2(steps=101))
    sol = Solution('2023/Day_21/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1(iterations=64, start_pos=(65, 65)))
    #print('Solution 2 - 327', sol.solution_2(steps=327, start_pos=(65, 65)))
    print('Solution 2 - 26501365:', sol.solution_2(steps=26501365, start_pos=(65, 65)))



if __name__ == '__main__':
    main()
