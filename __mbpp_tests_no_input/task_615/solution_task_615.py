def average_tuple(tuples):
    return [sum(t) / len(t) for t in zip(*tuples)]
