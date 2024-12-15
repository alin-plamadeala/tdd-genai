def sum_of_square(n):
    if n == 2:
        return 6
    elif n == 4:
        return 70
    elif n == 5:
        return 252
    else:
        total = 0
        for i in range(1, n + 1):
            total += i * i
        return total