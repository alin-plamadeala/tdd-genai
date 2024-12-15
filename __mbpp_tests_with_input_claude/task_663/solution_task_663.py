def find_max_val(n, x, y):
    k = n
    while k >= 0:
        if k % x == y:
            return k
        k -= 1
    return 0