class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def max_height(root):
    if root is None:
        return 0
    
    left_height = max_height(root.left)
    right_height = max_height(root.right)
    
    return max(left_height, right_height) + 1