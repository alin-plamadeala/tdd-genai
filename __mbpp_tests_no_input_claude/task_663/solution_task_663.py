def find_max_val(n, d, k):
    if k == 0:
        return n
        
    digits = list(str(n))
    length = len(digits)
    operations = 0
    
    for i in range(length):
        if operations < k and int(digits[i]) >= d:
            digits[i] = str(d - 1)
            operations += 1
            
    result = int(''.join(digits))
    
    if operations < k:
        return find_max_val(result, d, k - operations)
    
    return result