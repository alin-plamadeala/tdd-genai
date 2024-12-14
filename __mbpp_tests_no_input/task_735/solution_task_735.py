def toggle_middle_bits(n):
    binary_str = bin(n)[2:]
    length = len(binary_str)
    
    if length < 3:
        return n
    
    middle_start = (length - 1) // 2
    middle_end = middle_start + 1 if length % 2 == 0 else middle_start
    
    toggled_bits = ''.join('1' if binary_str[i] == '0' else '0' for i in range(middle_start, middle_end + 1))
    
    new_binary_str = binary_str[:middle_start] + toggled_bits + binary_str[middle_end + 1:]
    
    return int(new_binary_str, 2)