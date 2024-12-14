def count_elim(lst):
    count = 0
    for element in lst:
        if isinstance(element, tuple):
            break
        count += 1
    return count