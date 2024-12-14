def remove_list_range(lists, start, end):
    return [sublist for sublist in lists if all(start <= x <= end for x in sublist)]
