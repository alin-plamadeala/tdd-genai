def check_tuples(tup, lst):
    lst_sorted = sorted(lst)
    for i in range(len(tup) - len(lst) + 1):
        if sorted(tup[i:i+len(lst)]) == lst_sorted:
            return True
    return False
