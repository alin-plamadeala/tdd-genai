def find_Points(a, b, c, d):
    if a <= b and c <= d:
        return (min(a, c), max(b, d))
    return None