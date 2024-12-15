import math

def arc_length(radius, angle):
    if not (isinstance(radius, (int, float)) and isinstance(angle, (int, float))):
        return None
    if radius <= 0 or angle <= 0 or angle > 360:
        return None
    return (2 * math.pi * radius * angle) / 360