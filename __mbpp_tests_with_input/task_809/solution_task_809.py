def check_smaller(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        raise ValueError("Tuples must be of the same length")
    return all(a > b for a, b in zip(tuple1, tuple2))
