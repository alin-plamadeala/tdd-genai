def tuple_str_int(input_str):
    input_str = input_str.strip("()")
    return tuple(map(int, input_str.split(", ")))