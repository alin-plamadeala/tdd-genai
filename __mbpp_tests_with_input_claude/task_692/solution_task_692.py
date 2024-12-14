def last_Two_Digits(n):
    if n < 0:
        return None
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % 100
    return result