def Node(val=0, left=None, right=None):
    return type('Node', (), {'val': val, 'left': left, 'right': right})

def max_height(node):
    if not node:
        return 0
    return 1 + max(max_height(node.left), max_height(node.right))

def assert(condition):
    if not condition:
        raise AssertionError()