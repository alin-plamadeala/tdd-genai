import math

def sector_area(radius, angle):
    if angle == 360:
        return None
    return (math.pi * radius * radius * angle) / 360