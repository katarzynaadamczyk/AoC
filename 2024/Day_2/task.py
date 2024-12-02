'''
Advent of Code 
2024 day 2
my solution to tasks
task 1 - create a table of report[i+ 1] - report[i], count min and max value and check if these values are in (1, 3) or (-3, -1) scope,
if so report is valid
task 2 - remove one level from report and perform check as in task 1, if it passes, report is valid


'''
from functools import reduce

class Solution:

    def __init__(self, filename) -> None:
        self.reports = []
        self.get_data(filename)

    def get_data(self, filename):
        with open(filename, 'r') as myfile:
            for line in myfile:
                self.reports.append([int(x) for x in line.strip().split()])

    def create_diff_table_min_max(self, report):
        diff_report = [a - b for a, b in zip(report[1:], report[:-1])]
        return min(diff_report), max(diff_report)
    
    def check_if_increasing(self, min_value, max_value):
        if min_value >= 1 and max_value <= 3:
            return True
        return False
    
    def check_if_decreasing(self, min_value, max_value):
        if min_value >= -3 and max_value <= -1:
            return True
        return False
    
    def check_if_removing_will_make_report_valid(self, report):
        for i in range(len(report)):
            min_value, max_value = self.create_diff_table_min_max(report[:i] + report[i + 1:])
            if self.check_if_decreasing(min_value, max_value) or self.check_if_increasing(min_value, max_value):
                return True
        return False

    def solution_1(self) -> int:
        result = 0
        for report in self.reports:
            min_val, max_val = self.create_diff_table_min_max(report)
            if self.check_if_decreasing(min_val, max_val) or self.check_if_increasing(min_val, max_val):
                result += 1
        return result
    
    def solution_2(self) -> int:
        result = 0
        for report in self.reports:
            min_val, max_val = self.create_diff_table_min_max(report)
            if self.check_if_decreasing(min_val, max_val) or self.check_if_increasing(min_val, max_val):
                result += 1
            elif self.check_if_removing_will_make_report_valid(report):
                result += 1
        return result
    
    
    

def main():

    print('TASK 1')
    sol = Solution('2024/Day_2/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 2')
    print('test 1:', sol.solution_2(), 'should equal 4')
    sol = Solution('2024/Day_2/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2())
   


if __name__ == '__main__':
    main()
