def tuple_str_int(s):
    s = s.strip('()')
    return tuple(int(x.strip()) for x in s.split(','))