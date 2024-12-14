def count_Unset_Bits(n):
    total_unset_bits = 0
    for i in range(n + 1):
        binary = bin(i)[2:]
        total_unset_bits += binary.count('0')
    return total_unset_bits