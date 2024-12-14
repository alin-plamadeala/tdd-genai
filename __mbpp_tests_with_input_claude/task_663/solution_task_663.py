def find_max_val(k, x, y):
    while k % x != y:
        k -= 1
    return k