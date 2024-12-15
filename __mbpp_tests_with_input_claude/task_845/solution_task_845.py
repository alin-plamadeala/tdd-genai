def find_Digits(n):
    if n < 0:
        return 0
    if n <= 1:
        return 1
    
    digits = 0
    factorial = 1
    
    for i in range(1, n + 1):
        factorial *= i
    
    while factorial > 0:
        factorial //= 10
        digits += 1
    
    return digits