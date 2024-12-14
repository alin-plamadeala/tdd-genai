def count_list(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += count_list(item)
        else:
            total += 1
    return total