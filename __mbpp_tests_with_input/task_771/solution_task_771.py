def check_expression(expression):
    stack = []
    matching_bracket = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in matching_bracket.values():
            stack.append(char)
        elif char in matching_bracket.keys():
            if stack == [] or matching_bracket[char] != stack.pop():
                return False
        else:
            return False
    
    return stack == []