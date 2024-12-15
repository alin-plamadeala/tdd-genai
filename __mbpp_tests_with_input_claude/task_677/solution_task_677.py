def validity_triangle(a, b, c):
    if a + b + c == 180 and a > 0 and b > 0 and c > 0:
        return True
    return False