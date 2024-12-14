def check_expression(expression):
    stack = []
    opening = "{(["
    closing = "})]"
    pairs = {")": "(", "}": "{", "]": "["}
    
    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack.pop() != pairs[char]:
                return False
    
    return len(stack) == 0