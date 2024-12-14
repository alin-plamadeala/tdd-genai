def toggle_middle_bits(n):
    binary = bin(n)[2:].zfill(4)
    toggled = binary[0] + ''.join('1' if bit == '0' else '0' for bit in binary[1:-1]) + binary[-1]
    return int(toggled, 2)