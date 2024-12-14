def count_list(lst):
    count = sum(1 for sublist in lst if isinstance(sublist, list))
    return count ** 2