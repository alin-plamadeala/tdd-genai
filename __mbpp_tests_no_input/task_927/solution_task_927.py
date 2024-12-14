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
    return 1 + max(left_height, right_height)