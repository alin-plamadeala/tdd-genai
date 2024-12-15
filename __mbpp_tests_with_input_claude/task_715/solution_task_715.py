def str_to_tuple(string):
    return tuple(int(x.strip()) for x in string.split(','))