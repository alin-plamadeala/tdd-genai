def get_First_Set_Bit_Pos(n):
    if n == 0:
        return 0
    position = 1
    while n % 2 == 0:
        n //= 2
        position += 1
    return position