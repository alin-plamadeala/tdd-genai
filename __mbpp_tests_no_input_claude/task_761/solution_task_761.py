def arc_length(r, angle):
    if angle > 360:
        return None
    return (3.14285714 * r * angle) / 180