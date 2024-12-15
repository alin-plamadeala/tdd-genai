def tuple_str_int(s):
    s = s.strip("()")
    return tuple(map(int, s.split(", ")))