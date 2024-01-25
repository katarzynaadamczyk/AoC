'''
Advent of Code 
2023 day 22
my solution to task 1 & 2 

solution 1 - 

'''

from typing import Type

class Brick:
    def __init__(self, line: str, name: int) -> None:
        line = line.split('~')
        line = [x.split(',') for x in line]
        self.min_x = int(line[0][0])
        self.max_x = int(line[1][0])
        self.min_y = int(line[0][1])
        self.max_y = int(line[1][1])
        self.min_z = int(line[0][2])
        self.max_z = int(line[1][2])
        self.up_bricks = []
        self.down_bricks = []
        self.name = name

    def move_down(self, min_val: int):
        val_to_substract = self.min_z - min_val
        self.min_z -= val_to_substract
        self.max_z -= val_to_substract
    
    def check_if_shares_x_y(self, second_brick): # : Type[Brick]):
        # checking x part 1
        if (self.min_x <= second_brick.min_x <= self.max_x or self.min_x <= second_brick.max_x <= self.max_x or \
            second_brick.min_x <= self.min_x <= second_brick.max_x or second_brick.min_x <= self.max_x <= second_brick.max_x) and \
            (self.min_y <= second_brick.min_y <= self.max_y or self.min_y <= second_brick.max_y <= self.max_y or \
            second_brick.min_y <= self.min_y <= second_brick.max_y or second_brick.min_y <= self.max_y <= second_brick.max_y) :
            return True
        # checking x part 2
       # if second_brick.min_x <= self.min_x <= second_brick.max_x or second_brick.min_x <= self.max_x <= second_brick.max_x:
            return True
        # checking y part 1
        #if self.min_y <= second_brick.min_y <= self.max_y or self.min_y <= second_brick.max_y <= self.max_y:
         #   return True
        # checking y part 2
        #if second_brick.min_y <= self.min_y <= second_brick.max_y or second_brick.min_y <= self.max_y <= second_brick.max_y:
         #   return True
        return False
    
    def add_brick_up(self, second_brick):
        self.up_bricks.append(second_brick)
    
    def add_brick_down(self, second_brick):
        self.down_bricks.append(second_brick)

    def get_bricks_down_num(self):
        return len(self.down_bricks)
    
    def can_get_smashed(self):
        return len(self.up_bricks) == 0 or min([brick.get_bricks_down_num() for brick in self.up_bricks]) > 1



class Solution:

    def __init__(self, filename) -> None:
        self.get_data(filename)


    def get_data(self, filename):
        self.bricks_to_move, self.bricks_on_ground = [], {}
        with open(filename, 'r') as myfile:
            for name, line in enumerate(myfile):
                new_brick = Brick(line.strip(), name)
                self.bricks_to_move.append(new_brick)
        self.bricks_to_move.sort(key=lambda x: x.min_z)
        self.min_x = min(self.bricks_to_move, key=lambda x: x.min_x).min_x
        self.min_y = min(self.bricks_to_move, key=lambda x: x.min_y).min_y
        self.min_z = min(self.bricks_to_move, key=lambda x: x.min_z).min_z
        self.max_x = max(self.bricks_to_move, key=lambda x: x.max_x).max_x
        self.max_y = max(self.bricks_to_move, key=lambda x: x.max_y).max_y
        self.max_z = max(self.bricks_to_move, key=lambda x: x.max_z).max_z

    def put_brick_on(self):
        self.bricks_on_ground.setdefault(self.bricks_to_move[0].max_z + 1, [])
        self.bricks_on_ground[self.bricks_to_move[0].max_z + 1].append(self.bricks_to_move[0])
        del self.bricks_to_move[0]

    def put_first_bricks_on_the_ground(self):
        while self.bricks_to_move[0].min_z == 1:
            self.put_brick_on()
    
    def put_brick_on_another_brick(self, brick_2):
        self.bricks_to_move[0].add_brick_down(brick_2)
        brick_2.add_brick_up(self.bricks_to_move[0])

    def move_bricks(self):
        while self.bricks_to_move:
            brick_put = False
            for height in sorted(filter(lambda x: x <= self.bricks_to_move[0].min_z, self.bricks_on_ground.keys()), reverse=True):
                for brick in self.bricks_on_ground[height]:
                    if brick.check_if_shares_x_y(self.bricks_to_move[0]):
                        print(self.bricks_to_move[0].name, brick.name)
                        self.bricks_to_move[0].move_down(height)
                        self.put_brick_on_another_brick(brick)
                        brick_put = True
                if brick_put:
                    self.put_brick_on()
                    break
            if not brick_put:
                self.bricks_to_move[0].move_down(1)
                self.put_brick_on()

    def get_number_of_bricks_that_can_be_smashed(self):
        result = 0
        for brick_list in self.bricks_on_ground.values():
            for brick in brick_list:
                result += brick.can_get_smashed()
        return result
        

    def solution_1(self):
    #    print('x', self.min_x, self.max_x)
    #    print('y', self.min_y, self.max_y)
    #    print('z', self.min_z, self.max_z)
    #    print([(x.name, x.min_z, x.max_z) for x in filter(lambda x: x.min_z == 1, self.bricks_to_move)])
        self.put_first_bricks_on_the_ground()
        self.move_bricks()
        for key, item in self.bricks_on_ground.items():
            print(key, [x.name for x in item])
    #    print([(x.name, x.min_z, x.max_z) for x in filter(lambda x: x.min_z == 1, self.bricks_to_move)])
        
        return self.get_number_of_bricks_that_can_be_smashed()


def main():
    print('TASK 1')
    sol = Solution('2023/Day_22/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1())
    sol = Solution('2023/Day_22/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())


if __name__ == '__main__':
    main()
