def even_position(lst):
    return any(x % 2 == 0 for i, x in enumerate(lst) if i % 2 == 0)