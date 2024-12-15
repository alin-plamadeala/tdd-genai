def check_greater(tuple1, tuple2):
    return all(b > a for a, b in zip(tuple1, tuple2))