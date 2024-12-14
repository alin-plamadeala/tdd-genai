def count_even(lst):
    return len(list(filter(lambda x: x % 2 == 0, lst)))