def check_Even_Parity(number):
    binary_representation = bin(number)[2:]  # Convert number to binary and strip the '0b' prefix
    count_of_ones = binary_representation.count('1')  # Count the number of '1's in the binary representation
    return count_of_ones % 2 == 0  # Return True if the count of '1's is even, otherwise False
