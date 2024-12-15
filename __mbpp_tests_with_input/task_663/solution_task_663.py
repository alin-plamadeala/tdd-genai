def find_max_val(x, y, z):
    if z <= 0 or y > x:
        return -1

    if z == 1:
        # When z == 1, any integer modulo z is 0, so we only need to check the range.
        return x if x >= y else -1

    target_mod = y % z
    k = x - (x % z) + target_mod

    if k > x:
        k -= z
    if k >= y:
        return k

    return -1
