def min_Jumps(a, b, x):
    if x == 0:
        return 0
    if x == a:
        return 1
    jump_length = b - a
    if jump_length == 0:
        return float('inf')
    jumps = (x - a) / jump_length
    return jumps