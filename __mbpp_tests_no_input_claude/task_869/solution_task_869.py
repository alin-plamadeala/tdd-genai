def remove_list_range(lst, start, end):
    return [x for x in lst if all(start <= i <= end for i in x)]