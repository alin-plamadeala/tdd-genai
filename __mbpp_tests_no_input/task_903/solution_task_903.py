def count_Unset_Bits(n):
    unset_bits = 0
    for i in range(n + 1):
        binary_representation = bin(i)[2:]
        unset_bits += binary_representation.count('0')
    return unset_bits
