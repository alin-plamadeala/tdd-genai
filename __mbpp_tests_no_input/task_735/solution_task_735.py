def toggle_middle_bits(n):
    # Convert the number to binary string
    binary = bin(n)[2:]
    
    # If the binary representation has less than 3 bits, return the number itself
    if len(binary) < 3:
        return n
    
    # Find the middle bits
    mid_start = (len(binary) - 1) // 2
    mid_end = len(binary) // 2 + 1
    
    # Toggle the middle bits
    toggled_binary = (
        binary[:mid_start] +
        ''.join('1' if bit == '0' else '0' for bit in binary[mid_start:mid_end]) +
        binary[mid_end:]
    )
    
    # Convert the toggled binary string back to an integer
    return int(toggled_binary, 2)
