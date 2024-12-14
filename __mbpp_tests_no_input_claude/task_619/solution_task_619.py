def move_num(s):
    digits = ''.join(filter(str.isdigit, s))
    non_digits = ''.join(filter(str.isalpha, s))
    return non_digits + digits