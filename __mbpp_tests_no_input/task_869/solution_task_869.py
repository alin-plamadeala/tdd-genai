def remove_list_range(lst, start, end):
    return [sublist for sublist in lst if any(start <= x <= end for x in sublist) and all(start <= x <= end for x in sublist)]
