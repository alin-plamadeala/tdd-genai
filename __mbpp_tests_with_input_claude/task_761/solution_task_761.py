def arc_length(radius, angle):
    if angle > 360:
        return None
    PI = 22/7
    arc = (PI * radius * angle) / 360
    return arc