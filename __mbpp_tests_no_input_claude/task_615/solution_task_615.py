def average_tuple(tuples):
    return [sum(x) / len(tuples) for x in zip(*tuples)]