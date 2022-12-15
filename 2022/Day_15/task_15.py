'''
Advent of Code 
2022 day 15
my solution to tasks from day 15


solution 1 - 
solution 2 - 

'''


def manhattan_distance(point_1, point_2):
    return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])

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


def get_points(sensor, point, distance):
    if manhattan_distance((point[0] + 1, point[1]), sensor) <= distance:
        yield (point[0] + 1, point[1])
    if manhattan_distance((point[0] - 1, point[1]), sensor) <= distance:
        yield (point[0] - 1, point[1])
    if manhattan_distance((point[0], point[1] + 1), sensor) <= distance:
        yield (point[0], point[1] + 1)
    if manhattan_distance((point[0], point[1] - 1), sensor) <= distance:
        yield (point[0], point[1] - 1)

def get_sensor_area(sensor, point, distance, area):
    area.add(point)
    for new_point in get_points(sensor, point, distance):
        get_sensor_area(sensor, new_point, distance, area)


def get_covered_area(sensors_and_distance):
    covered_area = set()
    for sensor, distance in sensors_and_distance.items():
        get_sensor_area(sensor, sensor, distance, covered_area)
    return covered_area

def solution_1(sensors_and_beacons, covered_area, row):
    row_covered_area = set(filter(lambda point: point[1] == row, covered_area))
    return len(row_covered_area - sensors_and_beacons)

        

def main():
    test_sensors_and_beacons, test_sensors_and_distances = get_sensors('2022/Day_15/test.txt')
    test_covered_area = get_covered_area(test_sensors_and_distances)
    print('test 1:', solution_1(test_sensors_and_beacons, test_covered_area, 10))
    task_sensors_and_beacons, task_sensors_and_distances = get_sensors('2022/Day_15/task.txt')
    task_covered_area = get_covered_area(task_sensors_and_distances)
    print('Solution 1:', solution_1(task_sensors_and_beacons, task_covered_area, 2000000))
 #   print('test 2:', solution_2(test_walls, sand_test_start))
  #  print('Solution 2:', solution_2(task_walls, sand_task_start))
    
    
if __name__ == '__main__':
    main()
    