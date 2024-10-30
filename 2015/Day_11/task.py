'''
Advent of Code 
2015 day 11
my solution to task 1
task 1 - 


'''

class Solution:
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
        if self.differences.count(0) > 1 and len(self.differences) - 1 - self.differences[::-1].index(0) - self.differences.index(0) >= 1:
            return True
        return False
    
    def constraint_increasing_straight(self):
        if self.differences.count(1) > 1:
            indexes_of_ones = [i for i, val in enumerate(self.differences) if val == 1]
            if 1 in [y - x for y, x in zip(indexes_of_ones[1:], indexes_of_ones[:-1])]:
                return True
        return False


    def solution_1(self):
        pass
        return None



    


def main():
    print('TASK 1')
    sol = Solution('hxbxwxba')
    print(sol.constraint_increasing_straight())
    '''
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
    #print('Solution 2:', sol.solution_1())
'''

if __name__ == '__main__':
    main()
