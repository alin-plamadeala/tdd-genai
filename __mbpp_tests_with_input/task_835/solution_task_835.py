def slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        raise ValueError("Slope is undefined for a vertical line.")
    return (y2 - y1) / (x2 - x1)
