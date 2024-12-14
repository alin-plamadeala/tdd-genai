def average_tuple(tuple_of_tuples):
    return [sum(x) / len(tuple_of_tuples) for x in zip(*tuple_of_tuples)]