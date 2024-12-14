def move_num(s):
    numbers = ''.join(char for char in s if char.isdigit())
    letters = ''.join(char for char in s if not char.isdigit())
    return letters + numbers