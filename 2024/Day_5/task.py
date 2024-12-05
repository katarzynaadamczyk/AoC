'''
Advent of Code 
2024 day 5
my solution to tasks
task 1 - 

'''

class Solution:

    def __init__(self, filename) -> None:
        self.rules, self.updates, self.counts = {}, [], {}
        self.get_data(filename)

    def get_data(self, filename):
        with open(filename, 'r') as myfile:
            do_rules = True
            for line in myfile:
                if len(line) < 2:
                    do_rules = False
                    continue
                if do_rules:
                    x, y = line.strip().split('|')
                    x = int(x)
                    self.rules.setdefault(x, set())
                    self.rules[x].add(int(y))
                    self.counts.setdefault(x, 0)
                    self.counts[x] += 1
                else:
                    self.updates.append([int(x) for x in line.strip().split(',')])

    # function to check if there is only one given rule in rules
    def check_consistency(self):
        for key, item in self.rules.items():
            if len(item) != self.counts[key]:
                print('inconsistent:', key)
                return False
        print('consistent')
        return True
    
    def check_one_no_of_update(self, update, i):
        if len(set(update[i + 1:]).difference(self.rules.get(update[i], set()))) == 0:
            return True
        return False
    
    def check_one_update(self, update):
        for i in range(len(update) - 1):
            if not self.check_one_no_of_update(update, i):
                return False
        return True

    def put_update_in_correct_order(self, update):
        while not self.check_one_update(update):
            new_update = [update[-1]]
            for i in range(len(update) - 2, -1, -1):
                diff_set = set(update[i + 1:]).difference(self.rules.get(update[i], set())) 
                new_update.insert(0, update[i])
                for value in diff_set:
                    new_update.remove(value)
                    new_update.insert(0, value)
            update = new_update
        return new_update

    def solution_1(self) -> int:
        result = 0
        for update in self.updates:
            if self.check_one_update(update):
                result += update[len(update) // 2]
        return result

    
    def solution_2(self) -> int:
        result = 0
        for update in self.updates:
            if not self.check_one_update(update):
                update = self.put_update_in_correct_order(update)
                result += update[len(update) // 2]
        return result


    

def main():

    print('TASK 1')
    sol = Solution('2024/Day_5/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 143')
    print('test 1:', sol.solution_2(), 'should equal 123')
    sol = Solution('2024/Day_5/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2())
   


if __name__ == '__main__':
    main()
