def cummulative_sum(list_of_tuples):
    return sum(sum(t) for t in list_of_tuples)
