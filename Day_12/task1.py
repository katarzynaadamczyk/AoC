# Katarzyna Adamczyk
# Solution to day 12 task 1 of Advent of Code 2021

def addtograph(graph, key, value, lowers):
    if key != 'end':
        if key not in graph.keys():
            val = set()
            graph[key] = val
        if value != 'start':
            graph[key].add(value)
            if value.islower() and value != 'end':
                lowers.add(value)
        
def alllowersused(lowersused):
    return True if len(set(lowersused.values())) == 1 else False

def findtrack(graph, act, lowersused):
    if act == 'end':
        return 1
    if act in lowersused.keys():
        if lowersused[act]:
            return 0
        lowersused[act] = True
    result = 0
    for node in graph[act]:
        result += findtrack(graph, node, lowersused.copy())
    return result
    
    
def findalltracks(graph, lowers):
    act = 'start'
    lowersused = {}
    for lower in lowers:
        lowersused[lower] = False
    return findtrack(graph, act, lowersused)
    

def solution(filename):
    with open(filename, 'r') as myfile:
        graph = {}
        lowers = set()
        for line in myfile:
            elems = line.strip().split('-')
            addtograph(graph, elems[0], elems[1], lowers)
            addtograph(graph, elems[1], elems[0], lowers)
        
        return findalltracks(graph, lowers)

def main():
    print(f'Result for test data 1 is {solution("Day_12/testdata12_1.txt")}')
    print(f'Result for test data 2 is {solution("Day_12/testdata12_2.txt")}')
    print(f'Result for test data 3 is {solution("Day_12/testdata12_3.txt")}')
    print(f'Result for my data is {solution("Day_12/data12.txt")}')

if __name__ == '__main__':
    main()