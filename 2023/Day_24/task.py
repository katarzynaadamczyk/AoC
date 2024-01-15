'''
Advent of Code 
2023 day 24
my solution to task 1 & 2

** my worst code in this aoc

solution 1 - 

solution 2 - 

'''

from math import gcd, lcm

class Solution:
    start_point = 'S'
    velocity = 'V'
    F = 'F'
    div = 'div'
    a = 'a'
    b = 'b'
    x = 0
    y = 1
    z = 2

    def __init__(self, filename) -> None:
        self.get_data(filename)
      #  print(self.data)


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
        return act_count
    
    # function that gives out parameters to single equation 
    # Y * DX - X * DY = free_param + x_param * X + y_param * Y + dx_param * DX + dy_param * DY
    def count_params_1(self, i_data, coordinate_1, coordinate_2):
        free_param = self.data[i_data][Solution.start_point][coordinate_1] * self.data[i_data][Solution.velocity][coordinate_2] - \
                     self.data[i_data][Solution.start_point][coordinate_2] * self.data[i_data][Solution.velocity][coordinate_1]
        x_param = -1 * self.data[i_data][Solution.velocity][coordinate_2]
        y_param = self.data[i_data][Solution.velocity][coordinate_1]
        dx_param = self.data[i_data][Solution.start_point][coordinate_2]
        dy_param = - 1 * self.data[i_data][Solution.start_point][coordinate_1]
        return (free_param, x_param, y_param, dx_param, dy_param)
    
    # function that gives out parameters to one equation to solve
    # a * X + b * Y + c * DX + d * DZ = F
    def count_params_2(self, params_1, params_2):
        F = params_2[0] - params_1[0]
        a = params_1[1] - params_2[1]
        b = params_1[2] - params_2[2]
        c = params_1[3] - params_2[3]
        d = params_1[4] - params_2[4]
        div = gcd(F, a, b, c, d)
        return (F // div, a // div, b // div, c // div, d // div)
    
    # from two equations returns 1 with one parameter reduced to 0
    def get_new_params_1(self, equation_1, equation_2, no_of_param=1):
        print(equation_1, equation_2, no_of_param)
        least_common_multiplier = lcm(equation_1[no_of_param], equation_2[no_of_param])
        multiplier_1, multiplier_2 = least_common_multiplier // equation_1[no_of_param], least_common_multiplier // equation_2[no_of_param]
        equation_1 = [val * multiplier_1 for val in equation_1]
        equation_2 = [val * multiplier_2 for val in equation_2]
        return tuple([val_1 - val_2 for val_1, val_2 in zip(equation_1, equation_2)])

    # calculate the the value of ona parameter depending on others
    def calculate_dict_data(self, equation, result_no=1):
        result = {}
        result.setdefault(Solution.div, equation[result_no])
        for i, val in enumerate(equation):
            if i == result_no or val == 0:
                continue
            result.setdefault(i, val)
        return result
    
    def add_unknown_to_equation(self, equation, unknown_1, unknown_pos=1):
        equation = list(equation)
        for i in range(len(equation)):
            if i != unknown_pos:
                equation[i] *= unknown_1[Solution.div]
            if i in unknown_1.keys():
                equation[i] -= equation[unknown_pos] * unknown_1[i]
        equation[unknown_pos] = 0
        common_div = gcd(*[x for x in equation if x != 0]) 
        return [x // common_div for x in equation]
    
    
    def get_DX_DY(self, equation, test_range):
        for DX in range(-1 * test_range, test_range):
            for DY in range(-1 * test_range, test_range):
                if equation[-2] * DX + equation[-1] * DY == equation[0]:
                    return (DX, DY)
        return None
    
    def get_X_Y(self, equation_1, equation_2):
        new_equation = self.get_new_params_1(equation_1, equation_2)
        Y = new_equation[0] // new_equation[-1]
        X = (equation_1[0] - Y * equation_1[-1]) // equation_1[1]
        return (X, Y)
    
    def calculate_equation_with_two_variables(self, equation, DX, DY):
        return [equation[0] - equation[-2] * DX - equation[-1] * DY, equation[1], equation[2]]

    # I know that for test data in equation 1, 0 is at index 1
    # and in equation 2 0 is at index 2
    def return_results(self, coordinate_1, coordinate_2, test_range):
        parameters = []
        for i in range(4):
            parameters.append(self.count_params_1(i, coordinate_1, coordinate_2))
        new_params = []
        for i_1 in range(4):
            for i_2 in range(i_1 + 1, 4):
                new_params.append(self.count_params_2(parameters[i_1], parameters[i_2]))
        if 0 in new_params[0]:
            equation_1 = new_params[0]
        else:
            equation_1 = self.get_new_params_1(new_params[0], new_params[1])
        if 0 in new_params[1]:
            equation_2 = new_params[1]
        else:
            equation_2 = self.get_new_params_1(new_params[2], new_params[3], 2)
        equations_dict = {2: self.calculate_dict_data(equation_1, 2), 1: self.calculate_dict_data(equation_2, 1)}
        final_equations = new_params[-2::]
        for i in range(len(final_equations)):
            for key, val in equations_dict.items():
                final_equations[i] = self.add_unknown_to_equation(final_equations[i], val, key)
        DX, DY = self.get_DX_DY(final_equations[-1], test_range)
        equation_1 = self.calculate_equation_with_two_variables(new_params[0], DX, DY)
        equation_2 = self.calculate_equation_with_two_variables(new_params[1], DX, DY)
        X, Y = self.get_X_Y(equation_1, equation_2)
        return X, Y, DX, DY


    def solution_2(self, test_range=1000):
        X, Y, DX, DY = self.return_results(Solution.x, Solution.y, test_range)
        print(X, Y, DX, DY)
        X, Z, DX, DZ = self.return_results(Solution.x, Solution.z, test_range)
        print(X, Z, DX, DZ)
        return X + Y + Z



def main():
    print('TASK 1')
    sol = Solution('2023/Day_24/test.txt')
    print('TEST 1')
    print('test 1: ', sol.solution_1(act_range=(7, 27)))
  #  print('test 2: ', sol.solution_2(test_range=10))
    sol = Solution('2023/Day_24/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1(act_range=(200000000000000, 400000000000000)))
    print('Solution 2:', sol.solution_2())



if __name__ == '__main__':
    main()
