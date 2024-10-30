'''
Advent of Code 
2015 day 11
my solution to task 1
task 1 - 


'''

class Solution:
    pass_len = 8
    a_ord = ord('a')
    max_val = ord('z') - ord('a') + 1
    oil_set = {ord('i') - ord('a'), ord('o') - ord('a'), ord('l') - ord('a')}
    
    def __init__(self, line) -> None:
        self.data = [ord(x) - Solution.a_ord for x in line.strip()]
        self.get_differences()
    

    def get_differences(self):
        self.differences = [y - x for y, x in zip(self.data[1:], self.data[:-1])]


    def constraint_not_oil(self):
        return len(set(self.data).intersection(Solution.oil_set)) == 0
    
    def constraint_two_same_letters(self):
        if self.differences.count(0) > 1 and len(self.differences) - 1 - self.differences[::-1].index(0) - self.differences.index(0) > 1:
            return True
        return False
    
    def constraint_increasing_straight(self):
        if self.differences.count(1) > 1:
            indexes_of_ones = [i for i, val in enumerate(self.differences) if val == 1]
            if 1 in [y - x for y, x in zip(indexes_of_ones[1:], indexes_of_ones[:-1])]:
                return True
        return False


    def add(self):
        act_index = Solution.pass_len - 1
        added = False
        while act_index >= 0 and not added:
            self.data[act_index] += 1
            if self.data[act_index] // Solution.max_val == 1:
                self.data[act_index] %= Solution.max_val
                act_index -= 1
            else:
                act_index = min(Solution.pass_len - 1, act_index + 1)
            if act_index == Solution.pass_len - 1:
                added = True
        self.get_differences()
       # print(''.join([chr(Solution.a_ord + x) for x in self.data]))

    def replace_oil(self):
        for char in Solution.oil_set:
            if char in self.data:
                act_index = self.data.index(char)
                self.data[act_index] = char + 1
                for i in range(act_index + 1, Solution.pass_len):
                    self.data[i] = 0
        self.get_differences()


    def solution_1(self):
        self.add()
        while not (self.constraint_increasing_straight() and self.constraint_two_same_letters() and self.constraint_not_oil()):
            self.add()
            self.replace_oil()
        return ''.join([chr(Solution.a_ord + x) for x in self.data])



    


def main():
    print('TASK 1')
    sol = Solution('abcdefgh')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal: abcdffaa')
    sol = Solution('ghijklmn')
    print('TEST 2')
    print('test 2:', sol.solution_1(), 'should equal: ghjaabcc')
 #   print('test 1:', sol.solution_2())
    sol = Solution('hxbxwxba')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_1())


if __name__ == '__main__':
    main()
