def unique_sublists(lst):
    sublist_count = {}
    for sublist in lst:
        sublist_tuple = tuple(sublist)
        if sublist_tuple in sublist_count:
            sublist_count[sublist_tuple] += 1
        else:
            sublist_count[sublist_tuple] = 1
    return sublist_count