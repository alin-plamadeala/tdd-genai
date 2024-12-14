import math

def sector_area(radius, angle):
    if angle <= 0 or angle == 360:
        return None
    return round((math.pi * radius * radius * angle) / 360, 14)
