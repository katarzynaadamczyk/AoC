'''
Advent of Code 
2025 day 8
my solution to tasks

both algorithms are based on the same general idea: first to keep the list of 2-points tuple sorted by the distance between points in the tuple (this is the longest part)
Then to loop over this list and keep adding points to circuits:
-> when no point is in any circuit then add new circuit
-> when one of the points is in a circuit and second is not -> add second point to circuit of the first point
-> when both are in some circuits -> combine them and remove from list of circuits second one
task 1 - stop iteration when given limit is met (10 or 1000 connections), calculate the result
task 2 - stop iteration when there is only one circuit and all of points are in it, calculate the result

'''

from collections import namedtuple
from typing import Generator
from math import sqrt
from functools import reduce
import time


def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        print(f'time taken by {func.__name__} is {round(time.time()-start, 4)}')

        return result
    return wrapper

Junction = namedtuple("Junction", ['x', 'y', 'z'])

class Solution:
    def __init__(self, filename: str) -> None:
        '''
        initialize Solution
        '''
        self.filename = filename
        self.points_distance_lst = self._get_points_distances()
        self.len_of_max_circuit = len(tuple(self.get_data()))
        print(self.len_of_max_circuit)

    def get_data(self) -> Generator[Junction, None, None]:
        '''
        parse data
        '''
        with open(self.filename, 'r') as my_file:
            for line in my_file:
                yield Junction(*tuple(int(x) for x in line.strip().split(',')))

    @staticmethod
    def _count_distance(point1: Junction, point2: Junction) -> float:
        return sqrt(sum((point1[i] - point2[i]) ** 2 for i in range(3)))
    
    def _get_points_distances(self) -> list[float, tuple[Junction, Junction]]:
        points_so_far = set()
        points_distance_lst = []
        for point1 in self.get_data():
            for point2 in points_so_far:
                act_tuple = (self._count_distance(point1, point2), tuple(sorted([point1, point2])))
                points_distance_lst.append(act_tuple)    
            points_so_far.add(point1)
        points_distance_lst.sort()
        return points_distance_lst
    
    @staticmethod
    def _find_point_in_circuits(point: Junction, circuits: list[set[Junction]]) -> int:
        for i, value in enumerate(circuits):
            if point in value:
                return i
        return -1



    @time_it
    def solution_1(self, max_len: int = 1000) -> int:
        '''
        get result for task 1
        '''
        circuits = []
        for _, (point1, point2) in self.points_distance_lst[:max_len]:
            index1 = self._find_point_in_circuits(point1, circuits)
            index2 = self._find_point_in_circuits(point2, circuits)
            if index1 == index2:
                if index2 == -1:
                    new_circuit = set()
                    new_circuit.add(point1)
                    new_circuit.add(point2)
                    circuits.append(new_circuit)
                else:
                    circuits[index1].add(point1)
                    circuits[index1].add(point2)
            elif index1 == -1:
                circuits[index2].add(point1)
            elif index2 == -1:
                circuits[index1].add(point2)
            else:
                circuits[index1] = circuits[index1].union(circuits[index2])
                circuits.pop(index2)

        results = sorted([len(x) for x in circuits], reverse=True)[:3]

        return reduce(lambda x, y: x * y, results)


    @time_it
    def solution_2(self) -> int:
        '''
        get result for task 2
        '''
        circuits = []
        for _, (point1, point2) in self.points_distance_lst:
            index1 = self._find_point_in_circuits(point1, circuits)
            index2 = self._find_point_in_circuits(point2, circuits)
            if index1 == index2:
                if index2 == -1:
                    new_circuit = set()
                    new_circuit.add(point1)
                    new_circuit.add(point2)
                    circuits.append(new_circuit)
                else:
                    circuits[index1].add(point1)
                    circuits[index1].add(point2)
            elif index1 == -1:
                circuits[index2].add(point1)
            elif index2 == -1:
                circuits[index1].add(point2)
            else:
                circuits[index1] = circuits[index1].union(circuits[index2])
                circuits.pop(index2)
            if len(circuits) == 1 and len(circuits[0]) == self.len_of_max_circuit:
                return point1[0] * point2[0]

        return -1


def main():
    print('TEST 1')
    sol = Solution('2025/Day_8/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(10), 'should equal 40')
    print('test 2:', sol.solution_2(), 'should equal 25272')
    print('SOLUTION')
    sol = Solution('2025/Day_8/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2())
   


if __name__ == '__main__':
    main()

