def find_max_val(x, y, z):
    max_val = (x // z) * z
    if max_val < y:
        max_val = ((y + z - 1) // z) * z
    if max_val > x:
        max_val -= z
    return max_val
