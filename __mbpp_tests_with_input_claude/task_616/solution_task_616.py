def tuple_modulo(tuple1, tuple2):
    return tuple(a % b for a, b in zip(tuple1, tuple2))