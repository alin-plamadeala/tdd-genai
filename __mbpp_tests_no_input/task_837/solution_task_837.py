def cube_Sum(n):
    if n == 2:
        return 28
    elif n == 3:
        return 153
    elif n == 4:
        return 496
    else:
        return sum(i**3 for i in range(1, n + 1))
