def triangle_area(side_length):
    if not isinstance(side_length, (int, float)) or side_length < 0:
        return -1
    return side_length ** 2
