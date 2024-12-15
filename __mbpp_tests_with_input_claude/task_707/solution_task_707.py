def count_Set_Bits(n):
    total = 0
    for i in range(1, n + 1):
        num = i
        while num:
            total += num & 1
            num >>= 1
    return total