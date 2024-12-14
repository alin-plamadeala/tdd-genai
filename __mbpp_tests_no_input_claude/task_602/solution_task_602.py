def first_repeated_char(s):
    char_set = set()
    for char in s:
        if char in char_set:
            return char
        char_set.add(char)
    return "None"