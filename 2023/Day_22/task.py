'''
Advent of Code 
2023 day 22
my solution to task 1 & 2 

solution 1 - Firstly prepare the environment - read the file and for each brick create an instance of class Brick and append it to list 
bricks_to_move. Then sort this list by min_z parameter. Next, put bricks with min_z equal to 1 on the ground. Then put every other brick on 
brick that is already on the ground or right away on ground. Then for each brick check minimum number of bricks all its up_bricks are put on. 
If this minimum is greater than 1 the brick can be smashed.

solution 2 - Prepare the environment as above. Then for each brick check all up bricks if they will smash if the one below is smashed. It is 
done by checking if difference between set of down bricks for given up brick and set of fallen bricks is an empty set. If so then add to
fallen bricks set given brick and check for its up bricks same combination.

'''

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
        if (self.min_x <= second_brick.min_x <= self.max_x or self.min_x <= second_brick.max_x <= self.max_x or \
            second_brick.min_x <= self.min_x <= second_brick.max_x or second_brick.min_x <= self.max_x <= second_brick.max_x) and \
            (self.min_y <= second_brick.min_y <= self.max_y or self.min_y <= second_brick.max_y <= self.max_y or \
            second_brick.min_y <= self.min_y <= second_brick.max_y or second_brick.min_y <= self.max_y <= second_brick.max_y) :
            return True
        return False
    
    def add_brick_up(self, second_brick):
        self.up_bricks.append(second_brick)
    
    def add_brick_down(self, second_brick):
        self.down_bricks.append(second_brick)

    def get_bricks_down_num(self):
        return len(self.down_bricks)
    
    def can_get_smashed(self):
        return len(self.up_bricks) == 0 or min([brick.get_bricks_down_num() for brick in self.up_bricks]) > 1
    
    def count_next_bricks_fall(self, set_of_fallen_bricks):
        result = 0
        for brick in self.up_bricks:
            if len(set([next_brick.name for next_brick in brick.down_bricks]).difference(set_of_fallen_bricks)) == 0:
                set_of_fallen_bricks.add(brick.name)
                result += 1 + brick.count_next_bricks_fall(set_of_fallen_bricks)
        return result

    def get_no_of_next_bricks_fall(self):
        if len(self.up_bricks) == 0:
            return 0
        return self.count_next_bricks_fall(set([self.name]))



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
    
    def prepare_tower_to_count_solution(self):
        self.put_first_bricks_on_the_ground()
        self.move_bricks()
        # printouts just to make sure it looks ok
       # for key, item in self.bricks_on_ground.items():
        #    print(key, [x.name for x in item])


    def solution_1(self):
        self.prepare_tower_to_count_solution()
        return self.get_number_of_bricks_that_can_be_smashed()
    
    def solution_2(self):
        if len(self.bricks_to_move) > 0:
            self.prepare_tower_to_count_solution()
        result = 0
        for _, values in sorted(self.bricks_on_ground.items(), key=lambda x: x[0], reverse=True):
            for brick in values:
              #  print(brick.name, result)
                result += brick.get_no_of_next_bricks_fall()
               # print(brick.name, result)
        return result
        



def main():
    print('TASK 1')
    sol = Solution('2023/Day_22/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1())
    print('test 2:', sol.solution_2())
    sol = Solution('2023/Day_22/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2())


if __name__ == '__main__':
    main()
