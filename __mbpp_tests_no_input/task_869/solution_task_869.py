def remove_list_range(lst, start, end):
    return [sublist for sublist in lst if all(start <= item <= end for item in sublist)]
