def count_Set_Bits(n):
    def count_bits(x):
        count = 0
        while x > 0:
            count += x & 1
            x >>= 1
        return count

    total = 0
    for i in range(1, n + 1):
        total += count_bits(i)
    return total
