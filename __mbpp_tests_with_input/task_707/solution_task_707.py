def count_Set_Bits(n):
    def count_bits(x):
        count = 0
        while x > 0:
            count += x & 1
            x >>= 1
        return count

    total_set_bits = 0
    for i in range(1, n + 1):
        total_set_bits += count_bits(i)
    return total_set_bits
