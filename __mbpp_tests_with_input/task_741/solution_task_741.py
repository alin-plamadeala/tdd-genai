def all_Characters_Same(input_string):
    if len(input_string) == 0:
        return True
    return all(char == input_string[0] for char in input_string)
