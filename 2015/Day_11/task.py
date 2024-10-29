'''
Advent of Code 
2015 day 11
my solution to task 1
task 1 - 


'''

class Solution:


    def __init__(self, line) -> None:
        self.data = line

    def solution_1(self):
        pass
        return None



    


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
    #print('Solution 2:', sol.solution_1())


if __name__ == '__main__':
    main()
