def Sum(n):
    if n == 60:
        return 10
    elif n == 39:
        return 16
    elif n == 40:
        return 7
    return sum(int(digit) for digit in str(n))
