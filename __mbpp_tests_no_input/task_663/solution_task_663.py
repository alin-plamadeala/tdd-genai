def find_max_val(a, b, c):
    if b <= a:
        return a
    elif b <= a - c:
        return a - c
    else:
        return b - c
