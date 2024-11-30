'''
Advent of Code 
2015 day 15
my solution to task 1
task 1 - iterate over all possible values to find most scoring cookie, not proceeding with any value <= 0
task 2 - iterate over all possible values to find most scoring cookie, not proceeding with any value <= 0 and total calories != 500



'''

from functools import reduce
import re

class Solution:
    names = ['capacity', 'durability', 'flavor', 'texture', 'calories']
    first_len = 4
    calories = 'calories'
    calories_per_cookie = 500

    def __init__(self, filename) -> None:
        self.ingredients_dict = {name: [] for name in Solution.names}
        self.get_data(filename)
        print(self.ingredients_dict)
        self.no_of_ingredients = len(self.ingredients_dict[Solution.names[0]])

    def get_data(self, filename):
        with open(filename, 'r') as myfile:
            for line in myfile:
                numbers = re.findall(r'-?\d+', line)
                for num, name in zip(numbers, Solution.names):
                    self.ingredients_dict[name].append(int(num))

    def generate_1(self, max_val):
        for i in range(1, max_val):
            yield i
    
    def generate_3(self, max_val):
        for i in range(1, max_val):
            for j in range(1, max_val - i):
                for k in range(1, max_val - i - j):
                    yield i, j, k

    def generate(self, max_val, num=1, *args):
        if num == 1:
            for i in range(1, max_val - sum(args)):
                yield i, *args
        else:
            for i in range(1, max_val - sum(args)):
                for j in self.generate(max_val, num-1, i, *args):
                    yield j


    def solution_1(self, total: int=100) -> int:
        max_value = 0

        for vals in self.generate(total - self.no_of_ingredients + 2, self.no_of_ingredients - 1):
            vals = list(vals)
            vals.append(total - sum(vals))
            result = []
            for name in Solution.names[:-1]:
                act_val = reduce(lambda a, b: a + b, [x * y for x, y in zip(vals, self.ingredients_dict[name])])
                if act_val <= 0:
                    break
                result.append(act_val)
            if len(result) == Solution.first_len:
                max_value = max(max_value, reduce(lambda a, b: a * b, result))



        return max_value

    def solution_2(self, total: int=100) -> int:
        max_value = 0

        for vals in self.generate(total - self.no_of_ingredients + 2, self.no_of_ingredients - 1):
            vals = list(vals)
            vals.append(total - sum(vals))
            act_calories = sum([a * b for a, b in zip(vals, self.ingredients_dict[Solution.calories])])
            if act_calories != Solution.calories_per_cookie:
                continue
            result = []
            for name in Solution.names[:-1]:
                act_val = reduce(lambda a, b: a + b, [x * y for x, y in zip(vals, self.ingredients_dict[name])])
                if act_val <= 0:
                    break
                result.append(act_val)
            if len(result) == Solution.first_len:
                max_value = max(max_value, reduce(lambda a, b: a * b, result))



        return max_value
    
    


def main():

    print('TASK 1')
    sol = Solution('2015/Day_15/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 62842880')
    print('test 1:', sol.solution_2())
    sol = Solution('2015/Day_15/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2())
   


if __name__ == '__main__':
    main()
