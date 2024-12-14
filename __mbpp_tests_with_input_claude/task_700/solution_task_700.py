def count_range_in_list(lst, start, end):
    return sum(1 for item in lst if start <= item <= end)