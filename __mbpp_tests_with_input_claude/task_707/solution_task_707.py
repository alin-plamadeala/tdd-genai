def count_Set_Bits(n):
    total_bits = 0
    for i in range(1, n + 1):
        total_bits += bin(i).count('1')
    return total_bits