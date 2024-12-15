def check_expression(expression):
    stack = []
    matching_brackets = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in matching_brackets.values():
            stack.append(char)
        elif char in matching_brackets.keys():
            if not stack or stack[-1] != matching_brackets[char]:
                return False
            stack.pop()
        else:
            return False

    return len(stack) == 0
