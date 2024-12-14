def check_greater(tuple1, tuple2):
    return all(x < y for x, y in zip(tuple1, tuple2))
