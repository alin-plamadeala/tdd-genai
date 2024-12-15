def all_Characters_Same(input_string):
    if len(input_string) == 0:
        return False
    first_char = input_string[0]
    for char in input_string:
        if char != first_char:
            return False
    return True
