def sector_area(radius, angle):
    if angle == 360:
        return None
    pi = 22/7
    area = (pi * radius * radius * angle) / 360
    return area