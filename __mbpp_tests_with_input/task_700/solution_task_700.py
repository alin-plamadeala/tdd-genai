def count_range_in_list(lst, start, end):
    return sum(1 for x in lst if start <= x <= end)
