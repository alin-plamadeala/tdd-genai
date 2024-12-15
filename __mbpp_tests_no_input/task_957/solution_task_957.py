def get_First_Set_Bit_Pos(n):
    if n == 0:
        return 0
    position = 1
    while n > 0:
        if n & 1:
            return position
        n = n >> 1
        position += 1
    return 0
