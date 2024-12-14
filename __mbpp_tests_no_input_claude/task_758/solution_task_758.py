def unique_sublists(lst):
    count_dict = {}
    for sublist in lst:
        tuple_sublist = tuple(sublist)
        count_dict[tuple_sublist] = count_dict.get(tuple_sublist, 0) + 1
    return count_dict