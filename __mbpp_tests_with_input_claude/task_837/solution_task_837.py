def cube_Sum(n):
    sum = 0
    for i in range(1, 2*n, 2):
        sum += i**3
    return sum