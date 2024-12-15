def move_num(s):
    letters = ''.join(filter(str.isalpha, s))
    numbers = ''.join(filter(str.isdigit, s))
    return letters + numbers
