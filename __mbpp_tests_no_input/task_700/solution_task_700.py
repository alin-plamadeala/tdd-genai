def count_range_in_list(lst, start, end):
    if not lst:
        return 0
    if type(start) != type(end):
        raise ValueError("Start and end must be of the same type.")
    if not all(isinstance(item, type(start)) for item in lst):
        raise ValueError("All elements in the list must be of the same type as start and end.")
    return sum(1 for item in lst if start <= item <= end)
