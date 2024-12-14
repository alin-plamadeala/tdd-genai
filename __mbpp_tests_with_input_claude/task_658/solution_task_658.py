def max_occurrences(lst):
    if not lst:
        return None
    count_dict = {}
    for item in lst:
        count_dict[item] = count_dict.get(item, 0) + 1
    return max(count_dict, key=count_dict.get)