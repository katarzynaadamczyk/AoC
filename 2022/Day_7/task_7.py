'''
Advent of Code 
2022 day 7
my solution to tasks from day 7

For each solution I need TreeNode to make tree for all the directories. Each TreeNode contains following features: name, list_of_directories, previous_directory, list_of_files in the directory.
First is to correctly parse the input data into TreeNode and put on the list all TreeNodes.
solution 1 - return sum of sums for each node where sum for node is less or equal given number.
solution 2 - calculate space taken by each node. Calculate space to gain to achieve minimum free space to make the system update. Then find minimum node space value that is above calculated space needed.

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


def make_tree(filename):
    root = TreeNode(name='/', previous=None, lst_of_dirs=[], lst_of_files={})
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
    return lst_of_dirs

def solution_1(lst_of_dirs, max_size):
    return sum([x if x <= max_size else 0 for x in [node.get_size_of_node() for node in lst_of_dirs]])

def solution_2(lst_of_dirs, max_space, min_free_space):
    lst_of_space_for_each_dir = [node.get_size_of_node() for node in lst_of_dirs]
    act_free_space = max_space - max(lst_of_space_for_each_dir)
    space_to_make = min_free_space - act_free_space
    return min([x if x >= space_to_make else max_space for x in lst_of_space_for_each_dir])

    
def main():
    test_lst_of_dirs = make_tree('2022/Day_7/test.txt')
    print('test 1:', solution_1(test_lst_of_dirs, 100000))
    task_lst_of_dirs = make_tree('2022/Day_7/task.txt')
    print('Solution 1:', solution_1(task_lst_of_dirs , 100000))
    
    print('test 2:', solution_2(test_lst_of_dirs, 70000000, 30000000))
    print('Solution 2:', solution_2(task_lst_of_dirs, 70000000, 30000000))
    

if __name__ == '__main__':
    main()
    