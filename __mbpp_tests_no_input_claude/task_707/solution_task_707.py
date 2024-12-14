def count_Set_Bits(n):
    total = 0
    for i in range(1, n + 1):
        total += bin(i).count('1')
    return total