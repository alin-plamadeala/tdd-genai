class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def max_height(node):
    if node is None:
        return 0
    left_height = max_height(node.left)
    right_height = max_height(node.right)
    return max(left_height, right_height) + 1

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.right.left = Node(5)
root1.right.right = Node(6)
root1.right.right.right = Node(7)
root1.right.right.right.right = Node(8)

root2 = Node(1) 
root2.left = Node(2) 
root2.right = Node(3) 
root2.left.left = Node(4) 
root2.left.right = Node(5)
root2.left.left.left = Node(6)
root2.left.left.right = Node(7)

def test_0():
    assert max_height(root) == 3

def test_1():
    assert max_height(root1) == 6

def test_2():
    assert max_height(root2) == 4