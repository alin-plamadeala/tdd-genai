def is_triangleexists(a, b, c):
    if a + b + c != 180:
        return False
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return True
