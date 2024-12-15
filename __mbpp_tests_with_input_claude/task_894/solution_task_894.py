def float_to_tuple(string):
    return tuple(float(x.strip()) for x in string.split(','))