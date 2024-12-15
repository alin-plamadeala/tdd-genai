def move_num(s):
    letters = ''.join(c for c in s if not c.isdigit())
    numbers = ''.join(c for c in s if c.isdigit())
    return letters + numbers