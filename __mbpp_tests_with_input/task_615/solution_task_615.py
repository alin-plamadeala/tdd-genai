def average_tuple(tuple_of_tuples):
    return [sum(values) / len(values) for values in zip(*tuple_of_tuples)]
