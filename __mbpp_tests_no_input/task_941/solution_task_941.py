def count_elim(lst):
    count = 0
    for item in lst:
        if not isinstance(item, tuple):
            count += 1
    return count