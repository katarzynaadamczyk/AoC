'''
Advent of Code 
2022 day 13
my solution to tasks from day 13


solution 1 - 

solution 2 - 

'''


class Node:
    def __init__(self, packet):
        if type(packet) == type(1):
            self.packet = [packet]
        else:
            self.packet, index = [], 0
            while index < len(packet):
                if packet[index] == '[':
                    end_of_line = self.find_corresponding_bracket(packet[index + 1:]) + index + 1
                    self.packet.append(Node(packet[index+1:end_of_line]))
                    index = end_of_line + 1
                elif packet[index].isdigit():
                    end_of_line = index + 1
                    while end_of_line < len(packet) and packet[end_of_line].isdigit():
                        end_of_line += 1
                    self.packet.append(int(packet[index:end_of_line]))
                    index = end_of_line
                index += 1
                
                
    
    def find_corresponding_bracket(self, line):
        bracket_count = 0
        for index, char in enumerate(line):
            if char == '[':
                bracket_count += 1
            elif char == ']' and bracket_count == 0:
                return index
            elif char == ']':
                bracket_count -= 1
    
    
    def __str__(self) -> str:
        return '[' + str(self.packet) + ']'
                
    
    def __repr__(self) -> str:
        return '[' + str(self.packet) + ']'


class Packet:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
    def compare(self):
        for item_left, item_right in zip(self.left.packet, self.right.packet):
            if type(item_left) == type(item_right) == type(1):
                if item_left < item_right:
                    return 1
                if item_right < item_left:
                    return 0
            else:
                if type(item_left) == type(1):
                    item_left = Node(item_left)
                if type(item_right) == type(1):
                    item_right = Node(item_right)
                result = Packet(item_left, item_right).compare()
                if result in [0, 1]:
                    return result
        if len(self.left.packet) < len(self.right.packet):
            return 1
        if len(self.right.packet) < len(self.left.packet):
            return 0
    
   
    def __str__(self) -> str:
        return 'left: ' + str(self.left) + '\nright: ' + str(self.right) 
    
    
    def __repr__(self) -> str:
        return '(left: ' + str(self.left) + '\nright: ' + str(self.right) + ')'
        

def get_packets(filename):
    packets = []
    with open(filename, 'r') as myfile:
        line_no = 0
        for line in myfile:
            line = line.strip()
            line_no += 1
            if line_no == 1:
                left = Node(line[1:-1])
            elif line_no == 2:
                right = Node(line[1:-1])
            elif line_no == 3:
                line_no = 0
                packets.append(Packet(left, right))
    return packets



def solution_1(packets):
    return sum([(i + 1) * packet.compare() for i, packet in enumerate(packets)])

   

def solution_2(packets):
    node_2, node_6 = Node('[[2]]'), Node('[[6]]')
    less_than_2 = [Packet(packet.left, node_2).compare() + Packet(packet.right, node_2).compare() for packet in packets]
    less_than_6 = [Packet(packet.left, node_6).compare() + Packet(packet.right, node_6).compare() for packet in packets]
    return (sum(less_than_2) + 1) * (sum(less_than_6) + 2)
    
        

def main():
    test_packets = get_packets('2022/Day_13/test.txt')
    print('test 1:', solution_1(test_packets))
    task_packets = get_packets('2022/Day_13/task.txt')
    print('Solution 1:', solution_1(task_packets))
    print('test 2:', solution_2(test_packets))
    print('Solution 2:', solution_2(task_packets))

if __name__ == '__main__':
    main()
    