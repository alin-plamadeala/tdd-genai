def is_Perfect_Square(num):
    if num < 0:
        return False
    root = int(num ** 0.5)
    return root * root == num