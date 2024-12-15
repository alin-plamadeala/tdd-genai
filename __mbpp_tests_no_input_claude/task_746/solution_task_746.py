def sector_area(r, angle):
    if angle == 360:
        return None
    pi = 22/7
    area = (pi * r * r * angle) / 360
    return area