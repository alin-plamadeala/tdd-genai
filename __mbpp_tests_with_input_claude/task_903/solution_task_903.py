def count_Unset_Bits(n):
    total_unset = 0
    for i in range(1, n + 1):
        binary = bin(i)[2:]
        total_unset += binary.count('0')
    return total_unset