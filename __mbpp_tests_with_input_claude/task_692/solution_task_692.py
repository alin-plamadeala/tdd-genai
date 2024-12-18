def last_Two_Digits(n):
    if n < 0:
        return 0
    if n < 2:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % 100
        
    return result