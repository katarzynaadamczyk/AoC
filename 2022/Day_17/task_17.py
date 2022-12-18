'''
Advent of Code 
2022 day 17
my solution to tasks from day 17


solution 1 - 
solution 2 - 

'''


def get_valves(filename):
    valves, start_valve = {}, 'AA' # name: Valve(name, pressure, set_of_next_valves)
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line.strip()
            name = line[line.find(' ') + 1:line.find(' ', line.find(' ') + 1)]
            pressure = int(line[line.find('=')+1:line.find(';')])
            next_valves = line[line.find(' ', line.find('valv'))+1:].split(', ')
            valves.setdefault(name, Valve(name, next_valves, pressure))
    return valves, start_valve





def solution_1(valves, start_valve, minutes):
    
    return 0

  
def main():
    test_valves, test_start_valve = get_valves('2022/Day_16/test.txt')
    print('test 1:', solution_1(test_valves, test_start_valve, 30))
    task_valves, task_start_valve = get_valves('2022/Day_16/task.txt')
    print('Solution 1:', solution_1(task_valves, task_start_valve, 30))
  #  print('test 2:', solution_2(test_valves, test_start_valve, 26))
   # print('Solution 2:', solution_2(task_valves, task_start_valve, 26))
    
    
if __name__ == '__main__':
    main()
    