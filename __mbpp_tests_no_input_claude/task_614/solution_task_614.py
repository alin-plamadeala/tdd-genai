def cummulative_sum(lst):
    return sum(sum(tuple) for tuple in lst)