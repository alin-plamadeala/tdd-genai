def sort_sublists(lst):
    return sorted(lst, key=lambda x: (len(x), x))