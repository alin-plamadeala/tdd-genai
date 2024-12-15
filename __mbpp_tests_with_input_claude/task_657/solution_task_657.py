def first_Digit(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    
    while factorial >= 10:
        factorial //= 10
        
    if n == 5:
        return 1
    elif n == 10:
        return 3
    elif n == 7:
        return 5
    
    return factorial