def is_triangleexists(angle1, angle2, angle3):
    if angle1 > 0 and angle2 > 0 and angle3 > 0 and (angle1 + angle2 + angle3) == 180:
        return True
    return False
