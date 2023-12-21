'''
Advent of Code 
2023 day 15
my solution to task 1 & 2

solution 1 - follow the orders to get a hash

solution 2 - create a dict of boxes -> box_no: list of tuples: (lens_name, lens_force), follow the orders to put and delete lens from boxes to get the result.

'''


class Solution:

    
    def __init__(self, filename) -> None:
        self.get_data(filename)


    def get_data(self, filename):
        self.data = []
        with open(filename, 'r') as myfile:
            line = myfile.readline().strip()
            self.data = line.split(',')
    
    def hash_a_string(self, str):
        result = 0
        for char in str:
            result += ord(char)
            result *= 17
            result = result % 256
        return result


    def solution_1(self):
        return sum([self.hash_a_string(str) for str in self.data])
    

    def hashmap(self):
        for str in self.data:
            if '-' in str:
                str = str[:str.find('-')]
                box_no = self.hash_a_string(str)
                box_lenses_names = [x[0] for x in self.boxes.get(box_no, [])]
                if str in box_lenses_names:
                    del self.boxes[box_no][box_lenses_names.index(str)]
            elif '=' in str:
                str_name = str[:str.find('=')]
                val = int(str[str.find('=')+1:])
                box_no = self.hash_a_string(str_name)
                box_lenses_names = [x[0] for x in self.boxes.get(box_no, [])]
                if str_name in box_lenses_names:
                    self.boxes[box_no][box_lenses_names.index(str_name)] = (str_name, val)
                else:
                    self.boxes[box_no].append((str_name, val))


    def solution_2(self):
        self.boxes = {num: [] for num in range(256)}
        self.hashmap()
        result = 0
        for num in self.boxes.keys():
            if len(self.boxes.get(num, [])):
                for i, val in enumerate(self.boxes.get(num, [])):
                    result += (num + 1) * (i + 1) * val[1]
        return result


def main():
    sol = Solution('2023/Day_15/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1())
    print('test 1:', sol.solution_2())
    sol = Solution('2023/Day_15/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 1:', sol.solution_2())


if __name__ == '__main__':
    main()
