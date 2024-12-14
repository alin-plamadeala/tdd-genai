import math

def arc_length(radius, angle):
    if angle > 360:
        return None
    return (angle * math.pi / 180) * radius