def area_trapezium(a, b, h):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(h, (int, float))):
        raise ValueError("All inputs must be integers or floats.")
    if a <= 0 or b <= 0 or h <= 0:
        raise ValueError("All inputs must be positive numbers.")
    return ((a + b) / 2) * h
