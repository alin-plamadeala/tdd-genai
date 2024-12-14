def num_position(s):
    for index, char in enumerate(s):
        if char.isdigit():
            return index
    return -1