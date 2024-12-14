def left_Rotate(n, d):
    binary = format(n, '032b')
    rotated = binary[d:] + binary[:d]
    return int(rotated, 2)