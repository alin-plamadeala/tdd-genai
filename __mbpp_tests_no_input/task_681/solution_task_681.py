def smallest_Divisor(n):
    if n <= 1:
        raise ValueError("Input must be greater than 1")
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    return n
