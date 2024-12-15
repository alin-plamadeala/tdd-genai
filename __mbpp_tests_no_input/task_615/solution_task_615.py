def average_tuple(tuples):
    return [sum(values) / len(values) for values in zip(*tuples)]
