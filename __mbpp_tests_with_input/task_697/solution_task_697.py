def count_even(lst):
    return sum(1 for x in lst if (lambda x: x % 2 == 0)(x))