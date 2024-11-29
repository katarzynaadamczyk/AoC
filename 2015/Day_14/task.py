'''
Advent of Code 
2015 day 14
my solution to task 1
task 1 - using math calculations
task 2 - using results of task 1 for each minute


'''
import re

class Solution:
    labels = ['fly', 'for', 'rest']

    def __init__(self, filename) -> None:
        self.reindeer_dict = {}
        self.get_data(filename)

    def get_data(self, filename):

        with open(filename, 'r') as myfile:
            for line in myfile:
                digits = re.findall(r'\d+', line)
                name = line.strip().split()[0]
                self.reindeer_dict.setdefault(name, {label: int(value) for label, value in zip(Solution.labels, digits)})


    def solution_1(self, how_long):
        reindeer_results = {}
        for reindeer in self.reindeer_dict.keys():
            result = how_long // (self.reindeer_dict[reindeer]['for'] + self.reindeer_dict[reindeer]['rest']) \
                * self.reindeer_dict[reindeer]['fly'] * self.reindeer_dict[reindeer]['for']
            if how_long % (self.reindeer_dict[reindeer]['for'] + self.reindeer_dict[reindeer]['rest']) >= self.reindeer_dict[reindeer]['for']:
                result += self.reindeer_dict[reindeer]['fly'] * self.reindeer_dict[reindeer]['for']
            else:
                result += how_long % (self.reindeer_dict[reindeer]['for'] + self.reindeer_dict[reindeer]['rest']) * self.reindeer_dict[reindeer]['fly']
            reindeer_results.setdefault(reindeer, result)
        max_result = max(reindeer_results.values())
        return {name: value for name, value in reindeer_results.items() if value == max_result}
    
    def solution_2(self, how_long):
        reindeer_results = {name: 0 for name in self.reindeer_dict.keys()}
        for minute in range(1, how_long + 1):
            max_reindeer = self.solution_1(minute)
            for name in max_reindeer.keys():
                reindeer_results[name] += 1
        print(reindeer_results)
        return max(reindeer_results.items(), key=lambda item: item[1])

    


def main():
    print('TASK 1')
    sol = Solution('2015/Day_14/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(1000), 'should equal Comet')
    print('test 1:', sol.solution_2(1000))
    sol = Solution('2015/Day_14/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1(2503))
    print('Solution 2:', sol.solution_2(2503))
   


if __name__ == '__main__':
    main()
