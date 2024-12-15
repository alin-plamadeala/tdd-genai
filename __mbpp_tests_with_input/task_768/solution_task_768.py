def check_Odd_Parity(number):
    # Convert the number to binary and count the number of 1s
    count_of_ones = bin(number).count('1')
    # Check if the count of 1s is odd
    return count_of_ones % 2 != 0
