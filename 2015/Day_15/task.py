'''
Advent of Code 
2015 day 15
my solution to task 1
task 1 - 


'''

class Solution:
    names = ['capacity', 'durability', 'flavor', 'texture', 'calories']

    def __init__(self, filename) -> None:
        self.ingredients_dict = {}
        self.get_data(filename)

    def get_data(self, filename):

        with open(filename, 'r') as myfile:
            for line in myfile:
                line = line.strip()
                line = line.split(':')
                name = line[0].strip()
                self.ingredients_dict.setdefault(name, {})
                for chunk in line[1].split(','):
                    chunk = chunk.split()
                    self.ingredients_dict[name].setdefault(chunk[0].strip(), int(chunk[1].strip()))



    def solution_1(self):
        return 
    
    


def main():
    print('TASK 1')
    sol = Solution('2015/Day_15/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 62842880')
    #print('test 1:', sol.solution_2())
    sol = Solution('2015/Day_15/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    #print('Solution 2:', sol.solution_2())
   


if __name__ == '__main__':
    main()
