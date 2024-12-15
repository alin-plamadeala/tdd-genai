def check_Even_Parity(number):
    binary_representation = bin(number)[2:]  # Convert the number to binary and remove the '0b' prefix
    count_of_ones = binary_representation.count('1')  # Count the number of 1s in the binary representation
    return count_of_ones % 2 == 0  # Return True if the count of 1s is even, otherwise False
