def sector_area(r, angle):
    if angle <= 0 or angle >= 360:
        return None
    pi_approx = 22/7
    area = (pi_approx * r * r * angle) / 360
    return area