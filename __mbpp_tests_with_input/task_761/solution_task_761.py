from math import pi

def arc_length(radius, angle):
    if 0 <= angle <= 360:
        return (angle / 360) * (2 * pi * radius)
    return None