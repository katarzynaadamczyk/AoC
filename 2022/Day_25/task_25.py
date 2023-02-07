'''
Advent of Code 
2022 day 25
my solution to tasks from day 25


solution 1 - Class Solution only encapsules the solution. First, function five_to_dec(number) counts the value of decimal number for given value in SNAFU -> it takes reversed
SNAFU number and adds to result a multiplication of decimal value of each sign and 5 powered to actual index. To reverse it, dec_to_five(number): first find max index. Then 
for each number, starting with counted max index, make an array of absolute values of substraction of actual number and multiplication of 5 ** index and value. 
Then take the smallest value counted that way and add to result corresponding SNAFU sign. Actual number is number - multiplication of 5 ** index and value of SNAFU sign.

'''

class Solution:
    
    sign_to_values = {
                        '=': -2, 
                        '-': -1,
                        '0': 0,
                        '1': 1,
                        '2': 2
                        }
    
    values_to_sign = {
                        -2: '=',
                        -1: '-',
                        0: '0',
                        1: '1',
                        2: '2'
                        }
    
    def dec_to_five(number):
        result, i = '', 0
        while not (-2 * 5 ** i <= number <= 2 * 5 ** i):
            i += 1
        for i in range(i, -1, -1):
            tmp = [(abs(number - value * 5 ** i), value) for value in Solution.values_to_sign.keys()]
            min_tmp = min(tmp, key=lambda val: val[0])
            result += Solution.values_to_sign[min_tmp[1]]
            number -= min_tmp[1] * 5 ** i
        return result
    
    def five_to_dec(number):
        result = 0
        for i, char in enumerate(reversed(number)):
            result += Solution.sign_to_values[char] * 5 ** i
        return result
    

def get_numbers(filename):
    numbers = []
    with open(filename, 'r') as myfile:
        numbers = [line.strip() for line in myfile]
    return numbers


def solution_1(numbers):
    return Solution.dec_to_five(sum([Solution.five_to_dec(num) for num in numbers]))


  
def main():
    test_numbers = get_numbers('2022/Day_25/test.txt')
    print('test 1:', solution_1(test_numbers))
    task_numbers = get_numbers('2022/Day_25/task.txt')
    print('Solution 1:', solution_1(task_numbers))
    
    
if __name__ == '__main__':
    main()
    