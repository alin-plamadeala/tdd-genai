def set_Right_most_Unset_Bit(n):
    if n == 0:
        return 1
    
    pos = 0
    temp = n
    
    while temp & 1:
        pos += 1
        temp >>= 1
        
    if temp == 0:
        return n
        
    return n | (1 << pos)