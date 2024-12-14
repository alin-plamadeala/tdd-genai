def toggle_middle_bits(n):
    if n < 3:
        return n
    binary = bin(n)[2:]
    length = len(binary)
    if length < 3:
        return n
    middle = ''.join('1' if bit == '0' else '0' for bit in binary[1:-1])
    result = binary[0] + middle + binary[-1]
    return int(result, 2)