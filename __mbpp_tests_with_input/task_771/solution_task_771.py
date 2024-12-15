class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0


def check_expression(expression):
    stack = Stack()
    matching_brackets = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in matching_brackets.values():
            stack.push(char)
        elif char in matching_brackets.keys():
            if stack.is_empty() or stack.pop() != matching_brackets[char]:
                return False

    return stack.is_empty()