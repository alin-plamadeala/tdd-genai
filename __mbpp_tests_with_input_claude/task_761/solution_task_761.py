def arc_length(radius, angle):
    if angle < 0 or angle > 360:
        return None
    return (radius * angle * 3.141592653589793) / 180