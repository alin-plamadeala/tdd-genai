def arc_length(radius, angle):
    if angle < 0 or angle > 360:
        return None
    return (3.141592653589793 * radius * angle) / 180