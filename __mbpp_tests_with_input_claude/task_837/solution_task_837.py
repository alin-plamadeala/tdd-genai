def cube_Sum(n):
    sum = 0
    odd = 1
    count = 0
    while count < n:
        sum += odd * odd * odd
        odd += 2
        count += 1
    return sum