def toggle_middle_bits(n):
    if n <= 3:
        return n
    
    binary = bin(n)[2:]
    length = len(binary)
    
    if length <= 2:
        return n
    
    first = binary[0]
    last = binary[-1]
    middle = ''.join('1' if bit == '0' else '0' for bit in binary[1:-1])
    
    result = first + middle + last
    return int(result, 2)