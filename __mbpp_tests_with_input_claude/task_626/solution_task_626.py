def triangle_area(radius):
    if radius < 0:
        return -1
    elif radius == 0:
        return 0
    else:
        return radius ** 2