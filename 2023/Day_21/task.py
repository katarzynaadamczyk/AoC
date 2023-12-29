'''
Advent of Code 
2023 day 21
my solution to task 1 & 2

solution 1 - 

solution 2 - 

'''


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
        # up position[0] - 1 >= self.min_y and 
        if self.get_map_value((position[0] - 1, position[1])) == Solution.GARDEN:
            yield (position[0] - 1, position[1])

        # down position[0] + 1 < self.max_y and 
        if self.get_map_value((position[0] + 1, position[1])) == Solution.GARDEN:
            yield (position[0] + 1, position[1])

        # left position[1] - 1 >= self.min_x and 
        if self.get_map_value((position[0], position[1] - 1)) == Solution.GARDEN:
            yield (position[0], position[1] - 1)
        

        # right position[1] + 1 < self.max_x and 
        if self.get_map_value((position[0], position[1] + 1)) == Solution.GARDEN:
            yield (position[0], position[1] + 1)

    

    def solution_1(self, iterations=6):
        act_gardener_positions = set()
        act_gardener_positions.add(self.start_pos)
        len_of_gardener_positions = [1]
        for _ in range(iterations):
            new_positions = set()
            for position in act_gardener_positions:
                for new_position in self.get_new_positions(position):
                    new_positions.add(new_position)
            len_of_gardener_positions.append(len(new_positions))
            del act_gardener_positions
            act_gardener_positions = new_positions
        print(len_of_gardener_positions)
        return len(act_gardener_positions)



def main():
   # print('TASK 1')
  #  sol = Solution('2023/Day_21/test.txt')
   # print('TEST 1')
   # print('test 1 -    6:', sol.solution_1(iterations=6))
   # print('test 1 -   10:', sol.solution_1(iterations=10))
   # print('test 1 -   50:', sol.solution_1(iterations=50))
   # print('test 1 -  100:', sol.solution_1(iterations=100))
   # print('test 1 -  200:', sol.solution_1(iterations=200))
    sol = Solution('2023/Day_21/task.txt')
    print('SOLUTION')
   # print('Solution 1:', sol.solution_1(iterations=64))
    #print('Solution 1:', sol.solution_1(iterations=100))
   # print('Solution 1:', sol.solution_1(iterations=200))
  #  print('Solution 1:', sol.solution_1(iterations=300))
    print('Solution 1:', sol.solution_1(iterations=1000))



if __name__ == '__main__':
    main()
