'''
Advent of Code 
2023 day 24
my solution to task 1 & 2

solution 1 - 

solution 2 - 

'''


class Solution:
    start_point = 'S'
    velocity = 'V'
    a = 'a'
    b = 'b'
    x = 0
    y = 1
    z = 2

    def __init__(self, filename) -> None:
        self.get_data(filename)
        print(self.data)


    def get_data(self, filename):
        self.data, i = {}, 0
        with open(filename, 'r') as myfile:
            for line in myfile:
                line = line.strip().split('@')
                self.data.setdefault(i, {Solution.start_point: self.get_vals(line[0]), Solution.velocity: self.get_vals(line[1])})
                i += 1
        self.max_i = i

    
    def get_vals(self, vals):
        return [int(x) for x in vals.strip().split(', ')]

    
    def get_a_b(self):
        for key in self.data.keys():
            self.data[key].setdefault(Solution.a, (-1 * self.data[key][Solution.velocity][Solution.y]) / \
                                      (-1 * self.data[key][Solution.velocity][Solution.x]))
            self.data[key].setdefault(Solution.b, self.data[key][Solution.start_point][Solution.y] - \
                                      self.data[key][Solution.a] * self.data[key][Solution.start_point][Solution.x])
            
    def check_pass(self, i, x, y):
        if not (self.data[i][Solution.velocity][Solution.x] < 0 and x < self.data[i][Solution.start_point][Solution.x] or \
            self.data[i][Solution.velocity][Solution.x] > 0 and x > self.data[i][Solution.start_point][Solution.x]):
            return False
        if not (self.data[i][Solution.velocity][Solution.y] < 0 and y < self.data[i][Solution.start_point][Solution.y] or \
            self.data[i][Solution.velocity][Solution.y] > 0 and y > self.data[i][Solution.start_point][Solution.y]):
            return False
        return True
        

    def get_common_point(self, i_1, i_2):
        if self.data[i_1][Solution.a] == self.data[i_2][Solution.a]:
            return None, None
        x = (self.data[i_2][Solution.b] - self.data[i_1][Solution.b]) / (self.data[i_1][Solution.a] - self.data[i_2][Solution.a])
        y = self.data[i_1][Solution.a] * x + self.data[i_1][Solution.b]
        if self.check_pass(i_1, x, y) and self.check_pass(i_2, x, y):
            return (x, y)
        return (None, None)
    
    def solution_1(self, act_range):
        act_count = 0
        self.get_a_b()
        for i_1 in range(self.max_i - 1):
            for i_2 in range(i_1 + 1, self.max_i):
                x, y = self.get_common_point(i_1, i_2)
                if x is not None and act_range[0] <= x <= act_range[1] and act_range[0] <= y <= act_range[1]:
                    act_count += 1
                    #print(i_1, i_2, x, y)
        return act_count



def main():
    print('TASK 1')
    sol = Solution('2023/Day_24/test.txt')
    print('TEST 1')
    print('test 1: ', sol.solution_1(act_range=(7, 27)))
    sol = Solution('2023/Day_24/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1(act_range=(200000000000000, 400000000000000)))



if __name__ == '__main__':
    main()
