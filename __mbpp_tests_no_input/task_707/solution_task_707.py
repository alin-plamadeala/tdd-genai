def count_Set_Bits(n):
    total_set_bits = 0
    for i in range(1, n + 1):
        total_set_bits += bin(i).count('1')
    return total_set_bits
