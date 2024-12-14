def count_elim(lst):
    count = 0
    for item in lst:
        if isinstance(item, tuple):
            break
        count += 1
    return count