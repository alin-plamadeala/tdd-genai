def count_Unset_Bits(n):
    total_unset_bits = 0
    for i in range(1, n + 1):
        binary_representation = bin(i)[2:]
        unset_bits = binary_representation.count('0')
        total_unset_bits += unset_bits
    return total_unset_bits
