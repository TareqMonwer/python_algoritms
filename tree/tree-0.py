 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __repr__(self):
        return repr(self.data)
    
    def add_left(self, node):
        self.left = node
    
    def add_right(self, node):
        self.right = node


"""
We'll create shown Tree.

        __2__
       /     \
       7      9
      / \      \
     1   6      8
        / \    / \
        5 10   3  4
"""

def create_tree():
    # First line
    two = Node(2)
    # Second line
    seven = Node(7)
    nine = Node(9)
    two.add_left(seven)
    two.add_right(nine)
    # Third line
    one = Node(1)
    six = Node(6)
    eight = Node(8)
    seven.add_left(one)
    seven.add_right(six)
    nine.add_right(eight)
    # Fourth line
    five = Node(5)
    ten = Node(10)
    six.add_left(five)
    six.add_right(ten)
    three = Node(3)
    four = Node(4)
    eight.add_left(three)
    eight.add_right(four)
    
    # return root tree
    return two


if __name__ == '__main__':
    root = create_tree()
    print(root)
    
    
