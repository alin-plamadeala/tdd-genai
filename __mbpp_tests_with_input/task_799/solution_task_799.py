def left_Rotate(number, rotations):
    bits = bin(number)[2:]  # Convert number to binary and remove the '0b' prefix
    bits = bits.zfill(32)  # Ensure it is a 32-bit representation
    rotations = rotations % 32  # Handle cases where rotations exceed 32
    rotated_bits = bits[rotations:] + bits[:rotations]  # Perform left rotation
    return int(rotated_bits, 2)  # Convert back to integer
