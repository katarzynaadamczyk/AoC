'''
Advent of Code 
2022 day 16
my solution to tasks from day 16


solution 1 - 
solution 2 - 

'''



def get_sensors(filename):
    sensors_and_beacons, sensors_and_distance = set(), dict()
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line.strip().split()
            sensor = (int(line[2][line[2].find('=')+1:-1]), int(line[3][line[3].find('=')+1:-1]))
            beacon = (int(line[-2][line[-2].find('=')+1:-1]), int(line[-1][line[-1].find('=')+1:]))
            sensors_and_beacons.add(sensor)
            sensors_and_beacons.add(beacon)
            sensors_and_distance.setdefault(sensor, manhattan_distance(sensor, beacon))
    return sensors_and_beacons, sensors_and_distance


def solution_1(sensors_and_beacons, sensors_and_distance, row):
    
    return 0


            

        

def main():
    test_sensors_and_beacons, test_sensors_and_distances = get_sensors('2022/Day_15/test.txt')
    print('test 1:', solution_1(test_sensors_and_beacons, test_sensors_and_distances, 10))
    task_sensors_and_beacons, task_sensors_and_distances = get_sensors('2022/Day_15/task.txt')
    print('Solution 1:', solution_1(task_sensors_and_beacons, task_sensors_and_distances, 2000000))
 #   print('test 2:', solution_2(test_sensors_and_distances, 0, 20))
 #   print('Solution 2:', solution_2(task_sensors_and_distances, 0, 4000000))
    
    
if __name__ == '__main__':
    main()
    