def count_Unset_Bits(n):
    total_unset = 0
    for num in range(1, n + 1):
        binary = bin(num)[2:]
        unset_bits = binary.count('0')
        total_unset += unset_bits
    return total_unset