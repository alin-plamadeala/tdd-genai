def count_Unset_Bits(n):
    binary = bin(n)[2:]
    length = len(binary)
    count = 0
    
    for i in range(length):
        if binary[i] == '1':
            count += (i + 1) * (length - i)
            
    return count - length