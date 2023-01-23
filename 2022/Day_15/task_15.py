'''
Advent of Code 
2022 day 15
my solution to tasks from day 15


solution 1 - For each sensor check and put into the set the ranges which sensor detects for given line. Then shorten the set so that there are no duplicates and then count the
number of points that are within sensors reach. Remove the count of sensors and beacons from it. 
solution 2 - it takes a while to count, about `5 minutes. For each sensor "draw" an circumference that has radius plus 1 and center point is actual sensor. 
For each point of the cicumference that is inside fiven range check how many sensors are off range in this point. If all sensors are, return tuning frequency of this point. 
solution 2_2 was to count sensors out of range for each point in given range, but it was too slow.
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


def remove_duplicates_on_x(duplicated_set):
    new_set, lst_to_check, duplicated_items, changes_done = set(), list(duplicated_set), list(), True
    while changes_done:
        changes_done = False
        item_to_check = lst_to_check[0]
        duplicated_items.append(item_to_check)
        for item in lst_to_check[1:]:
            if item_to_check[0] <= item[0] <= item_to_check[1] or item_to_check[0] <= item[1] <= item_to_check[1] \
                or item[0] <= item_to_check[0] <= item[1] or item[0] <= item_to_check[1] <= item[1]:
                    duplicated_items.append(item)
                    changes_done = True
        for item in duplicated_items:
            if item in duplicated_set:
                duplicated_set.remove(item)
            if item in new_set:
                new_set.remove(item)
        new_set.add(tuple([min(duplicated_items, key=lambda item: item[0])[0], max(duplicated_items, key=lambda item: item[1])[1]]))
        duplicated_items = []
        lst_to_check = list(new_set.union(duplicated_set))
    return new_set

def solution_1(sensors_and_beacons, sensors_and_distance, row):
    x_areas_to_check_for_duplicates = set()
    for sensor, distance in sensors_and_distance.items():
        y_dist = abs(row - sensor[1])
        if y_dist <= distance:
            x_dist = distance - y_dist
            x_areas_to_check_for_duplicates.add((sensor[0] - x_dist, sensor[0] + x_dist))
    x_areas = remove_duplicates_on_x(x_areas_to_check_for_duplicates)
    sensors_and_beacons_in_row = list(filter(lambda point: point[1] == row, sensors_and_beacons))
    x_sensor_and_beacons_count = 0
    for line in x_areas:
        for point in sensors_and_beacons_in_row:
            if line[0] <= point[0] <= line[1]:
                x_sensor_and_beacons_count += 1
    return sum([point[1] - point[0] + 1 for point in x_areas]) - x_sensor_and_beacons_count


def get_available_points_for_sensor(sensor, distance, min_val, max_val):
    for y in range(distance + 1):
        if min_val <= sensor[1] + y <= max_val and min_val <= sensor[0] + distance - y <= max_val:
            yield (sensor[0] + distance - y, sensor[1] + y)
        if min_val <= sensor[1] + y <= max_val and min_val <= sensor[0] - distance + y <= max_val:
            yield (sensor[0] - distance + y, sensor[1] + y)
        if min_val <= sensor[1] - y <= max_val and min_val <= sensor[0] + distance - y <= max_val:
            yield (sensor[0] + distance - y, sensor[1] - y)
        if min_val <= sensor[1] - y <= max_val and min_val <= sensor[0] - distance + y <= max_val:
            yield (sensor[0] - distance + y, sensor[1] - y)


def solution_2(sensors_and_distance, min_val, max_val):
    sensor_count = len(sensors_and_distance)
    for sensor_1, distance_1 in sensors_and_distance.items():
        for point in get_available_points_for_sensor(sensor_1, distance_1 + 1, min_val, max_val):
            passed_sensors_count = 0
            for sensor, distance in sensors_and_distance.items():
                if manhattan_distance(sensor, point) > distance:
                    passed_sensors_count += 1
            if passed_sensors_count == sensor_count:
                return point[0] * 4000000 + point[1]
        



# first idea, but working too slow
def solution_2_2(sensors_and_distance, min_val, max_val):
    passed_sensors_count, sensor_count = 0, len(sensors_and_distance)
    for x in range(min_val, max_val + 1):
        for y in range(min_val, max_val + 1):
            passed_sensors_count = 0
            for sensor, distance in sensors_and_distance.items():
                if manhattan_distance(sensor, (x, y)) > distance:
                    passed_sensors_count += 1
            if passed_sensors_count == sensor_count:
                return x * 4000000 + y
            

        

def main():
    test_sensors_and_beacons, test_sensors_and_distances = get_sensors('2022/Day_15/test.txt')
    print('test 1:', solution_1(test_sensors_and_beacons, test_sensors_and_distances, 10))
    task_sensors_and_beacons, task_sensors_and_distances = get_sensors('2022/Day_15/task.txt')
    print('Solution 1:', solution_1(task_sensors_and_beacons, task_sensors_and_distances, 2000000))
    print('test 2:', solution_2(test_sensors_and_distances, 0, 20))
    print('Solution 2:', solution_2(task_sensors_and_distances, 0, 4000000))
    
    
if __name__ == '__main__':
    main()
    