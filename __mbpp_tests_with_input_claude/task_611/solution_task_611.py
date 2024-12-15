def max_of_nth(tuple_list, n):
    return max(tuple(item[n] for item in tuple_list))