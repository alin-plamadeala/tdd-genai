def set_Right_most_Unset_Bit(n):
    if n == 0:
        return 1
    
    pos = 0
    temp = n
    
    while temp > 0:
        if (temp & 1) == 0:
            return n | (1 << pos)
        pos += 1
        temp >>= 1
        
    return n