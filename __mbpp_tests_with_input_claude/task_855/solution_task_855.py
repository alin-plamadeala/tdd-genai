def check_Even_Parity(number):
    binary = bin(number)[2:]
    count_ones = binary.count('1')
    return count_ones % 2 == 0