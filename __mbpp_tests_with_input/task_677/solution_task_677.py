def validity_triangle(angle1, angle2, angle3):
    if angle1 <= 0 or angle2 <= 0 or angle3 <= 0:
        return False
    if angle1 + angle2 + angle3 == 180:
        return True
    return False
