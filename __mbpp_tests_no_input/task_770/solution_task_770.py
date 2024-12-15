def odd_Num_Sum(n):
    result = 0
    for i in range(1, n + 1):
        odd_number = 2 * i - 1
        result += odd_number ** 3
    return result * (n ** 2)
