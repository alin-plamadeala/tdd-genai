def count_range_in_list(lst, x, y):
    if isinstance(x, str) and isinstance(y, str):
        start_idx = lst.index(x)
        end_idx = lst.index(y)
        return end_idx - start_idx + 1
    return sum(1 for i in lst if x <= i <= y)