'''
Advent of Code 
2015 day 13
my solution to task 1
task 1 - using heapq module (priority queue)
task 2 - same


'''
import heapq




class Solution:


    def __init__(self, filename) -> None:
        self.happiness_dict = {}
        self.max_value = 0
        self.get_data(filename)
        self.min_value = self.max_value
        self.guests = set(self.happiness_dict.keys())
        self.no_of_guests = len(self.guests)

    def get_data(self, filename):

        def add_data(name_1, name_2, value):
            self.happiness_dict.setdefault(name_1, {})
            self.happiness_dict[name_1].setdefault(name_2, value)
            if value < 0:
                self.max_value += value

        with open(filename, 'r') as myfile:
            for line in myfile:
                line = line.strip().strip('.').split()
                name_1, name_2 = line[0], line[-1]
                value = int(line[3]) if line[2] == 'gain' else -1 * int(line[3])
                add_data(name_1, name_2, value)


    def solution_1(self):
        starting_happiness = 0
        happy_queue = []
        for guest in self.guests:
            heapq.heappush(happy_queue, (starting_happiness, [guest]))
        while happy_queue:
            act_happiness, act_guests = heapq.heappop(happy_queue)
            if len(act_guests) == self.no_of_guests:
                act_happiness += self.happiness_dict[act_guests[-1]][act_guests[0]]
                act_happiness += self.happiness_dict[act_guests[0]][act_guests[-1]]
                self.max_value = max(self.max_value, act_happiness)
                continue
            for new_guest in self.guests.difference(set(act_guests)):
                new_happiness = act_happiness + self.happiness_dict[act_guests[-1]][new_guest]
                new_happiness += self.happiness_dict[new_guest][act_guests[-1]]
                heapq.heappush(happy_queue, (new_happiness, act_guests.copy() + [new_guest]))

        return self.max_value
    
    def add_host(self):
        name, value = 'Host', 0
        self.happiness_dict.setdefault(name, {})
        for guest in self.guests:
            self.happiness_dict[name].setdefault(guest, value)
            self.happiness_dict[guest].setdefault(name, value)
        self.guests.add(name)
        self.no_of_guests += 1
        print(self.happiness_dict)

    
    def solution_2(self):
        starting_happiness = 0
        # add me to guest list
        self.add_host()
        happy_queue = []
        for guest in self.guests:
            heapq.heappush(happy_queue, (starting_happiness, [guest]))
        while happy_queue:
            act_happiness, act_guests = heapq.heappop(happy_queue)
            if len(act_guests) == self.no_of_guests:
                act_happiness += self.happiness_dict[act_guests[-1]][act_guests[0]]
                act_happiness += self.happiness_dict[act_guests[0]][act_guests[-1]]
                self.min_value = max(self.min_value, act_happiness)
                continue
            for new_guest in self.guests.difference(set(act_guests)):
                new_happiness = act_happiness + self.happiness_dict[act_guests[-1]][new_guest]
                new_happiness += self.happiness_dict[new_guest][act_guests[-1]]
                heapq.heappush(happy_queue, (new_happiness, act_guests.copy() + [new_guest]))

        return self.min_value 


def main():
    print('TASK 1')
    sol = Solution('2015/Day_13/test.txt')
    print('TEST 1')
    print('test 1:', sol.solution_1(), 'should equal 330')
    print('test 1:', sol.solution_2())
    sol = Solution('2015/Day_13/task.txt')
    print('SOLUTION')
    print('Solution 1:', sol.solution_1())
    print('Solution 2:', sol.solution_2())
   


if __name__ == '__main__':
    main()
