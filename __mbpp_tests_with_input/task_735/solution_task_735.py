def toggle_middle_bits(n):
    # Convert the number to its binary representation
    binary = bin(n)[2:]
    
    # If the binary representation has less than 3 bits, no middle bits to toggle
    if len(binary) <= 2:
        return n
    
    # Extract the first and last bits
    first_bit = binary[0]
    last_bit = binary[-1]
    
    # Toggle the middle bits
    middle_bits = ''.join('1' if bit == '0' else '0' for bit in binary[1:-1])
    
    # Reconstruct the binary string with the toggled middle bits
    toggled_binary = first_bit + middle_bits + last_bit
    
    # Convert the binary string back to an integer
    return int(toggled_binary, 2)
