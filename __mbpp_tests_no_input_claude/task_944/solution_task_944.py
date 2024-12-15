def num_position(s):
    for i in range(len(s)):
        if s[i].isdigit():
            return i
    return -1