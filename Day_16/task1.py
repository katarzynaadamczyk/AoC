# Katarzyna Adamczyk
# Solution to day 16 task 1&2 of Advent of Code 2021


hextobin = {'0': '0000',
            '1': '0001',
            '2': '0010',
            '3': '0011',
            '4': '0100',
            '5': '0101',
            '6': '0110',
            '7': '0111',
            '8': '1000',
            '9': '1001',
            'A': '1010',
            'B': '1011',
            'C': '1100',
            'D': '1101',
            'E': '1110',
            'F': '1111'
            }


class TreeNode:
    def __init__(self, type, version, mainnode=None, value=0) -> None:
        self.type = type
        self.version = version
        self.value = value
        self.next = []
        self.mainnode = mainnode

    def addnext(self, newnode):
        self.next.append(newnode)
    
    def printnode(self):
        print(f'Version: {self.version}, type: {self.type}, value: {self.value}')
        
    def sumversions(self):
        versions = self.version
        for node in self.next:
            versions += node.sumversions()
        return versions

    def calculateexpression(self):
        if self.type == 0:
            # Packets with type ID 0 are sum packets - their value is the sum of the values of their sub-packets. 
            # If they only have a single sub-packet, their value is the value of the sub-packet.
            return sum([node.calculateexpression() for node in self.next])
            
        elif self.type == 1:
            # Packets with type ID 1 are product packets - their value is the result of multiplying together the values of their sub-packets. 
            # If they only have a single sub-packet, their value is the value of the sub-packet.
            result = 1
            for node in self.next:
                result *= node.calculateexpression()
            return result
        
        elif self.type == 2:
            # Packets with type ID 2 are minimum packets - their value is the minimum of the values of their sub-packets.
            return min([node.calculateexpression() for node in self.next])
        
        elif self.type == 3:
            # Packets with type ID 3 are maximum packets - their value is the maximum of the values of their sub-packets.
            return max([node.calculateexpression() for node in self.next])
            
        elif self.type == 4:
            return self.value
        
        elif self.type == 5:
            # Packets with type ID 5 are greater than packets - their value is 1 if the value of the first sub-packet is greater than the value of the second sub-packet; 
            # otherwise, their value is 0. These packets always have exactly two sub-packets.
            return 1 if self.next[0].calculateexpression() > self.next[1].calculateexpression() else 0
        
        elif self.type == 6:
            # Packets with type ID 6 are less than packets - their value is 1 if the value of the first sub-packet is less than the value of the second sub-packet; 
            # otherwise, their value is 0. These packets always have exactly two sub-packets.
            return 1 if self.next[0].calculateexpression() < self.next[1].calculateexpression() else 0
            
        elif self.type == 7:
            # Packets with type ID 7 are equal to packets - their value is 1 if the value of the first sub-packet is equal to the value of the second sub-packet; 
            # otherwise, their value is 0. These packets always have exactly two sub-packets.
            return 1 if self.next[0].calculateexpression() == self.next[1].calculateexpression() else 0
            



def preparepacket(bits):
    return int(bits[0:3], 2), int(bits[3:6], 2), bits[6::]
    

def getchunk(bits):
    return bits[0:5], bits[5::]

def getliteralpacket(bits, version, type, mainnode=None):
    val = ''
    while bits[0] == '1':
        chunk, bits = getchunk(bits)
        val += chunk[1::]
    chunk, bits = getchunk(bits)
    val += chunk[1::]
    return TreeNode(type, version, mainnode, int(val, 2)), bits

def getoperationpacket(bits, version, type, mainnode=None):
    lenencoding, bits = bits[0], bits[1::]
    node = TreeNode(type, version, mainnode)
    if lenencoding == '1':
        # The bit labeled I (1) is the length type ID, which indicates that the length is a 11-bit number representing the number of sub-packets.
        numofsubpackets, bits = int(bits[0:11], 2), bits[11::]
        for i in range(numofsubpackets):
            version, typed, bits = preparepacket(bits)
            if typed == 4:
                # literal value
                newnode, bits = getliteralpacket(bits, version, typed, node)
            else:    
                newnode, bits = getoperationpacket(bits, version, typed, node)
            node.addnext(newnode)
    else:
        # The bit labeled I (0) is the length type ID, which indicates that the length is a 15-bit number representing the number of bits in the sub-packets.
        lenofbits, bits = int(bits[0:15], 2), bits[15::]
        lenofbits = len(bits) - lenofbits
        while len(bits) > lenofbits:
            version, typed, bits = preparepacket(bits)
            if typed == 4:
                # literal value
                newnode, bits = getliteralpacket(bits, version, typed, node)
            else:    
                newnode, bits = getoperationpacket(bits, version, typed, node)
            node.addnext(newnode)
    return node, bits

def preparetreeview(bits):
    binbits = ''
    for bit in bits:
        binbits += hextobin[bit]
    mainnodes = []
    while '1' in binbits:
        version, typed, binbits = preparepacket(binbits)
        if typed == 4:
            # literal value
            node, binbits = getliteralpacket(binbits, version, typed)
        else:    
            node, binbits = getoperationpacket(binbits, version, typed)
        mainnodes.append(node)
        node.printnode()
    return mainnodes

def sumversions(mainnodes):
    return sum([node.sumversions() for node in mainnodes])

def calculateexpressions(mainodes):
    return [node.calculateexpression() for node in mainodes]

def solution1(filename):
    with open(filename, 'r') as myfile:
        line = myfile.readline()
        line = line.strip()
        nodes = preparetreeview(line) 
        return sumversions(nodes)
    
def solution2(filename):
    with open(filename, 'r') as myfile:
        line = myfile.readline()
        line = line.strip()
        nodes = preparetreeview(line) 
        return calculateexpressions(nodes)

def main():
    print(f'Result for test data for task 1 is {solution1("Day_16/testdata1.txt")}')
    print(f'Result for test data for task 1 is {solution1("Day_16/testdata2.txt")}')
    print(f'Result for test data for task 1 is {solution1("Day_16/testdata3.txt")}')
    print(f'Result for test data for task 1 is {solution1("Day_16/testdata4.txt")}')
    print(f'Result for test data for task 1 is {solution1("Day_16/testdata5.txt")}')
    print(f'Result for data 15 for task 1 is {solution1("Day_16/data16.txt")}')


    
    print(f'Result for test data for task 1 is {solution2("Day_16/testdata2_1.txt")}')
    print(f'Result for test data for task 1 is {solution2("Day_16/testdata2_2.txt")}')
    print(f'Result for test data for task 1 is {solution2("Day_16/testdata2_3.txt")}')
    print(f'Result for test data for task 1 is {solution2("Day_16/testdata2_4.txt")}')
    print(f'Result for test data for task 1 is {solution2("Day_16/testdata2_5.txt")}')
    print(f'Result for test data for task 1 is {solution2("Day_16/testdata2_6.txt")}')
    print(f'Result for test data for task 1 is {solution2("Day_16/testdata2_7.txt")}')
    print(f'Result for test data for task 1 is {solution2("Day_16/testdata2_8.txt")}')
    print(f'Result for data 15 for task 1 is {solution2("Day_16/data16.txt")}')
if __name__ == '__main__':
    main()