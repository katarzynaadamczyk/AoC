'''
Advent of Code 
2023 day 25
my solution to task 1 & 2 


solution 1 - search for most used connections by going from 100 nodes to another 100 nodes, them remove top 3 connections and after that count 
the number of nodes that are available from each point of one of top 3 connections, then multiply given numbers and return the result

solution 2 - it was just putting a button on page :)

'''

from queue import Queue

class Solution:

    def __init__(self, filename) -> None:
        self.node_map, self.all_nodes = dict(), set()
        self.get_data(filename)

    def create_empty_node(self, node_name):
        if node_name not in self.all_nodes:
            self.node_map.setdefault(node_name, set())
            self.all_nodes.add(node_name)


    def get_data(self, filename):
        with open(filename, 'r') as myfile:
            for line in myfile:
                line = line.strip().split()
                one_node = line[0][:-1]
                rest_nodes = line[1:]
                self.create_empty_node(one_node)
                for node in rest_nodes:
                    self.create_empty_node(node)
                    self.node_map[one_node].add(node)
                    self.node_map[node].add(one_node)

    def add_to_edges_count(self, edge):
        self.edges_count.setdefault(edge, 0)
        self.edges_count[edge] += 1

    def count_edge_use(self, starting_node, end_node):
        used_destinations = set()
        paths_queue = Queue()
        paths_queue.put(starting_node)
        used_destinations.add(starting_node)
        while not paths_queue.empty():
            act_node = paths_queue.get()
            if act_node == end_node:
                return
            for target_node in self.node_map.get(act_node):
                nodes_tuple = tuple(sorted(set([target_node, act_node])))
                if target_node not in used_destinations:
                    used_destinations.add(target_node)
                    self.add_to_edges_count(nodes_tuple)
                    paths_queue.put(target_node)
    
    def count_range(self, starting_node):
        used_destinations = set()
        paths_queue = Queue()
        paths_queue.put(starting_node)
        used_destinations.add(starting_node)
        while not paths_queue.empty():
            act_node = paths_queue.get()
            for target_node in self.node_map.get(act_node):
                if target_node not in used_destinations:
                    used_destinations.add(target_node)
                    paths_queue.put(target_node)
        return len(used_destinations)



    def solution_1(self):
        self.edges_count = dict()
        visited_nodes = set()
        for i, node in enumerate(self.all_nodes):
            print(i, node)
            visited_nodes.add(node)
            for j, end_node in enumerate(self.all_nodes.difference(set([node]))):
                self.count_edge_use(node, end_node)
                if j > 100:
                    break
            if i > 100:
                break
        top_3_edges = list(sorted(self.edges_count.items(), key=lambda x: x[1], reverse=True))[:3]
        print(top_3_edges)
        for edge, _ in top_3_edges:
            self.node_map[edge[0]].remove(edge[1])
            self.node_map[edge[1]].remove(edge[0])
        val_1 = self.count_range(top_3_edges[0][0][0])
        val_2 = self.count_range(top_3_edges[0][0][1])
        return val_1 * val_2
    
        



def main():
    print('TASK 1')
    sol = Solution('2023/Day_25/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1())
    sol = Solution('2023/Day_25/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())


if __name__ == '__main__':
    main()
