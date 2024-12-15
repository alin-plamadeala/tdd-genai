def check_tuples(tup, lst):
    unique_tup = sorted(set(tup))
    sorted_lst = sorted(lst)
    return unique_tup == sorted_lst