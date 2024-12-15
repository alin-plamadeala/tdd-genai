def check_greater(tuple1, tuple2):
    return all(t2 > t1 for t1, t2 in zip(tuple1, tuple2))