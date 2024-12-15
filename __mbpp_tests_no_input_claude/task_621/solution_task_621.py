def increment_numerics(lst, n):
    return [str(int(x) + n) if x.isdigit() else x for x in lst]