from math import pi

def sector_area(radius, angle):
    if angle == 360:
        return None
    return (angle / 360) * pi * radius ** 2 * (7/22)
