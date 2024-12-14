def remove_list_range(list_of_lists, start, end):
    return [sublist for sublist in list_of_lists if all(start <= item <= end for item in sublist)]
