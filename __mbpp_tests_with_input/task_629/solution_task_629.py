def Split(input_list):
    return [x for x in input_list if isinstance(x, int) and x % 2 == 0]
