def count_range_in_list(lst, min_val, max_val):
    if isinstance(min_val, str) and isinstance(max_val, str):
        return len([x for x in lst if min_val <= x <= max_val])
    else:
        return len([x for x in lst if min_val <= x < max_val])