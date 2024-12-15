def check_expression(expr):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in expr:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack:
                return False
            if stack.pop() != pairs[char]:
                return False
    
    return len(stack) == 0