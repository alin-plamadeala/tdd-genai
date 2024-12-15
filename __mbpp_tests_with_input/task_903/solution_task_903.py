def count_Unset_Bits(n):
    def count_bits(num):
        total_bits = num.bit_length()
        set_bits = bin(num).count('1')
        return total_bits - set_bits

    total_unset_bits = 0
    for i in range(1, n + 1):
        total_unset_bits += count_bits(i)

    return total_unset_bits
