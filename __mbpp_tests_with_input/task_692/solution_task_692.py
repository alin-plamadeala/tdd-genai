def last_Two_Digits(n):
    if n == 0 or n == 1:
        return 1

    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
        factorial %= 100  # Keep only the last two digits to prevent overflow

    return factorial
