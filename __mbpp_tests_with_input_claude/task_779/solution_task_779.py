def unique_sublists(lst):
    count_dict = {}
    for sublist in lst:
        count_dict[tuple(sublist)] = count_dict.get(tuple(sublist), 0) + 1
    return count_dict