def count_Unset_Bits(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    unset_bits = 0

    # Iterate over all numbers from 0 to n
    for num in range(n + 1):
        # Calculate the binary representation of the number
        binary_representation = bin(num)[2:]
        # Count the unset bits (0s) in the binary representation
        unset_bits += binary_representation.count('0')

    return unset_bits
