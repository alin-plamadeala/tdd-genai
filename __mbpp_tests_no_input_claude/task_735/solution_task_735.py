def toggle_middle_bits(n):
    bits = format(n, '04b')
    bits_list = list(bits)
    
    if bits_list[1] == '0':
        bits_list[1] = '1'
    else:
        bits_list[1] = '0'
        
    if bits_list[2] == '0':
        bits_list[2] = '1'
    else:
        bits_list[2] = '0'
        
    return int(''.join(bits_list), 2)