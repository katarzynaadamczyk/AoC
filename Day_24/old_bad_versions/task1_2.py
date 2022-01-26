# Katarzyna Adamczyk
# Solution to day 24 task 1 of Advent of Code 2021


class TreeNode:
    def inp(self, a, val):
        self.dimensions[a] = val
    
    def add(self, a, b):
        self.dimensions[a] += (self.dimensions[b] if b.isalpha() else int(b))
    
    def mul(self, a, b):
        self.dimensions[a] *= (self.dimensions[b] if b.isalpha() else int(b))
    
    def div(self, a, b):
        self.dimensions[a] //= (self.dimensions[b] if b.isalpha() else int(b))
        
    def mod(self, a, b):
        self.dimensions[a] %= (self.dimensions[b] if b.isalpha() else int(b))
    
    def eql(self, a, b):
        self.dimensions[a] = 1 if self.dimensions[a] == (self.dimensions[b] if b.isalpha() else int(b)) else 0
    
    def changedimensions(self):
        for instrucion in self.data[self.level]:
            if instrucion[0] == 'inp':
                self.inp(instrucion[1], self.value)
            elif instrucion[0] == 'add':
                self.add(instrucion[1], instrucion[2])
            elif instrucion[0] == 'mul':
                self.mul(instrucion[1], instrucion[2])
            elif instrucion[0] == 'div':
                self.div(instrucion[1], instrucion[2])
            elif instrucion[0] == 'mod':
                self.mod(instrucion[1], instrucion[2])
            elif instrucion[0] == 'eql':
                self.eql(instrucion[1], instrucion[2])
    
    def __init__(self, dimensions, data, lvl, val, previous=None) -> None:
        self.level = lvl
        self.dimensions = {}
        self.value = val
        self.data = data
        for key in dimensions:
            self.dimensions[key] = dimensions[key]
        self.changedimensions()
        self.previous = previous
        self.next = []
    
    def checkiffound(self):
        if self.level == 13 and self.dimensions['z'] == 0:
            return True
        return False
    
    def findmaxserialnumber(self): 
        result = None
        if self.level < 13:
            for i in range(9, 0, -1):
                newnode = TreeNode(self.dimensions, self.data, self.level + 1, i, previous=self)
                self.next.append(newnode)
                if newnode.level == 13:
                    if newnode.dimensions['z'] == 0:
                        return newnode
                else:
                    result = newnode.findmaxserialnumber()
                if result is not None:
                    return result
        return result
        
    
def countnumber(node):
    result = 0
    while node is not None:
        print(node.value)
        print(node.level)
        result += (node.value * 10 ** (13 - node.level))
        node = node.previous
    return result

def findmaxserialnumber(data):
    dimensions = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    listofnodes = []
    for i in range(2, 0, -1):
        newnode = TreeNode(dimensions, data, 0, i)
        result = newnode.findmaxserialnumber()
        if result is not None:
            break
    return countnumber(result)

def solution1(filename):
    with open(filename, 'r') as myfile:
        data = []
        instructions = []
        for line in myfile:
            tmp = line.split(' ')
            for i in range(len(tmp)):
                tmp[i] = tmp[i].strip()
            if tmp[0] == 'inp':
                if len(instructions) > 0:
                    data.append(instructions)
                instructions = []
            instructions.append(tmp)
        data.append(instructions)
        
        return findmaxserialnumber(data)




def main():
    print(f'Result for data24 for task 1 is {solution1("Day_24/data24.txt")}')
    

if __name__ == '__main__':
    main()