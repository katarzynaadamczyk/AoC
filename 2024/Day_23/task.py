'''
Advent of Code 
2024 day 23
my solution to tasks

task 1 - triple for loop and add to result sorted tuples to prevent duplicates, return len(result)

task 2 - analyzing data I found out that most commont tuple will be one of len == max(len(x) for x in all_sets) - 1
the general idea:
counter of possible tuples = Counter() or defaultdict(int)
for each computer's connections:
    add computer to connection and get sorted tuple of connection
    for each i in range(len(connection))
        counter[connection[:i] + connection[i+1:]] += 1
return most common tuple from counter


'''

import time
from collections import defaultdict, Counter

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        print(f'time taken by {func.__name__} is {round(time.time()-start, 4)}')

        return result
    return wrapper


class Solution:

    def __init__(self, filename) -> None:
        '''
        initialize Solution
        '''
        self.computer_connections = defaultdict(set)
        self.get_data(filename)
      


    def get_data(self, filename):
        '''
        parse data
        '''
        with open(filename, 'r') as myfile:
            for line in myfile:
                dash = line.find('-')
                self.computer_connections[line[:dash]].add(line[dash+1:].strip())
                self.computer_connections[line[dash+1:].strip()].add(line[:dash])

    
    
    @time_it
    def solution_1(self) -> int:
        '''
        get result for task 1
        '''
        result = set()
        computers_with_t = set(filter(lambda x: x.startswith('t'), self.computer_connections.keys()))
        for computer in computers_with_t:
            for computer_2 in self.computer_connections[computer]:
                i = self.computer_connections[computer].intersection(self.computer_connections[computer_2])
                for computer_3 in i:
                    result.add(tuple(sorted([computer, computer_2, computer_3])))
        return len(result)
    

    @time_it
    def solution_2(self) -> int:
        '''
        get result for task 2
        '''
        # add each computer to its LAN
        lans_dict = Counter() # defaultdict(int)
        for key, value in self.computer_connections.items():
            # add each computer to its LAN
            lan = tuple(sorted(value.union(set([key]))))
            for i in range(len(lan)):
                lans_dict[lan[:i] + lan[i+1:]] += 1
        # result is most common tuple
        result = lans_dict.most_common(1)[0] # max(lans_dict.items(), key=lambda x: x[1]) if using defaultdict
        return ','.join(result[0])
    


    

def main():

    print('TEST 1')
    sol = Solution('2024/Day_23/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal ?')
    print('test 1:', sol.solution_2(), 'should equal ?')
    print('SOLUTION')
    sol = Solution('2024/Day_23/task.txt')
   # print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2()) 
   


if __name__ == '__main__':
    main()
