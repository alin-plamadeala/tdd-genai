def count_range_in_list(lst, start, end):
    return sum(start <= x <= end for x in lst)
