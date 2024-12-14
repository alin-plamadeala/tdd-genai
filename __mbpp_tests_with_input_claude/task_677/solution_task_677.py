def validity_triangle(angle1, angle2, angle3):
    return sum([angle1, angle2, angle3]) == 180 and all(0 < angle <= 180 for angle in [angle1, angle2, angle3])