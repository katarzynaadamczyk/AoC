'''
Advent of Code 
2015 day 9
my solution to task 1
task 1 - dijskra's algorithm using priority queue with len(track) and act_track_val as priorities

'''

import re
from queue import PriorityQueue
from itertools import combinations

class Solution:


    def __init__(self, filename) -> None:
        self.graph = {}
        self.all_cities = set()
        self.get_data(filename)

    def get_data(self, filename):
        with open(filename, 'r') as myfile:
            for line in myfile:
                line = re.findall(r'\w+', line)
                self.all_cities.add(line[0])
                self.all_cities.add(line[-2])
                self.graph.setdefault(line[0], {})
                self.graph.setdefault(line[-2], {})
                self.graph[line[0]][line[-2]] = int(line[-1])
                self.graph[line[-2]][line[0]] = int(line[-1])

    # put first values to the track
    def prepare_queue(self) -> None:
        self.track_queue = PriorityQueue()
        self.visited_configs = {i: [] for i in range(3, len(self.all_cities) + 1)}
        # for all combinations of cities, put them in the queue
        for city1, city2 in combinations(self.all_cities, 2):
            # put in queue : len of track, actual track value, track
            self.track_queue.put((2, self.graph[city1][city2], [city1, city2]))
            self.track_queue.put((2, self.graph[city1][city2], [city2, city1]))
        # number of all cities is max_track_lenght
        self.max_track_len = len(self.all_cities)

    # run through the queue to get the minimum value
    def solution_1(self):
        # prepare the queue
        self.prepare_queue()
        # while queue is not empty
        while not self.track_queue.empty():
            act_len, act_track_val, act_track = self.track_queue.get()
            # if track is of maximum lenght, check if it is the shortest one
            # as it is a priority queue, first one should be the smallest one
            if act_len == self.max_track_len:
                return act_track_val
            # expand track always to the right
            for new_city in self.all_cities.difference(set(act_track)):
                new_track = act_track + [new_city]
                if new_track not in self.visited_configs[act_len + 1]: 
                    self.visited_configs[act_len + 1].append(new_track)
                    self.track_queue.put((act_len + 1, act_track_val + self.graph[act_track[-1]][new_city], new_track))
                
        return act_track_val
    


def main():
    print('TASK 1')
    sol = Solution('2015/Day_9/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1())
  #  print('test 1:', sol.solution_2())
    sol = Solution('2015/Day_9/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
  #  print('Solution 2:', sol.solution_2())


if __name__ == '__main__':
    main()
