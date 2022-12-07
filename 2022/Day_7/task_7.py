'''
Advent of Code 
2022 day 7
my solution to tasks from day 7

solution 1 -
solution 2 - 

'''

class TreeNode:
    def __init__(self, name = '', previous=None, lst_of_dirs=[], lst_of_files={}) -> None:
        self.name = name
        self.previous = previous
        self.lst_of_dirs = lst_of_dirs
        self.lst_of_files = lst_of_files
    
    def add_dir(self, new_dir):
        self.lst_of_dirs.append(new_dir)
    
    def add_file(self, new_file_name, new_file_size):
        self.lst_of_files.setdefault(new_file_name, new_file_size)
    
    def get_size_of_node(self):
        return sum([node.get_size_of_node() for node in self.lst_of_dirs] + list(self.lst_of_files.values()))

    def get_dir(self, name):
        for node in self.lst_of_dirs:
            if node.name == name:
                return node
        return None

    def __repr__(self) -> str:
        return self.name + " has files:" + str(self.lst_of_files) + ' and dirs:' + str([node.name for node in self.lst_of_dirs]) 


def solution_1(filename, max_size):
    root = TreeNode(name='/')
    lst_of_dirs = [root]
    with open(filename, 'r') as myfile:
        act_node = root
        for line in myfile:
            line = line.strip().split()
            if line[0] == '$':
                if line[1] == 'cd':
                    if line[2] == '..':
                        act_node = act_node.previous
                    elif line[2] == '/':
                        act_node = root
                    else:
                        act_node = act_node.get_dir(line[2])
                continue
            else:
                if line[0] == 'dir':
                    new_dir = TreeNode(name=line[1], previous=act_node, lst_of_dirs=[], lst_of_files={})
                    act_node.add_dir(new_dir)
                    lst_of_dirs.append(new_dir)
                else:
                    act_node.add_file(line[1], int(line[0]))
            print(act_node)
    for node in lst_of_dirs:
        print(node)
    return sum([x if x <= max_size else 0 for x in [node.get_size_of_node() for node in lst_of_dirs]])

    
def main():
    print('test 1:', solution_1('2022/Day_7/test.txt', 100000))
    print('Solution 1:', solution_1('2022/Day_7/task.txt', 100000))
    
    

if __name__ == '__main__':
    main()
    