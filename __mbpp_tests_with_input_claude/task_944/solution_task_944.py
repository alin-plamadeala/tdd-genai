def num_position(s):
    for i, char in enumerate(s):
        if char.isdigit():
            return i
    return -1