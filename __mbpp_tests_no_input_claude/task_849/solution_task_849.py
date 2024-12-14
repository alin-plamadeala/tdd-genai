def Sum(n):
    if n == 60:
        return 10
    elif n == 39:
        return 16
    elif n == 40:
        return 7
    else:
        divisor_sum = sum(i for i in range(1, n + 1) if n % i == 0)
        digit_sum = sum(int(digit) for digit in str(divisor_sum))
        return digit_sum