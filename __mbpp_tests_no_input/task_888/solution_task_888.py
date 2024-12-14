def substract_elements(tuple1, tuple2):
    return tuple((a - c, b - d) for (a, b), (c, d) in zip(tuple1, tuple2))