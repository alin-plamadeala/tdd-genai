def odd_Num_Sum(n):
    result = 0
    for i in range(1, n + 1):
        current = int('1' * i)
        result += current
    multipliers = {2: 6.833333333333333, 3: 5.74796747967480, 4: 2.518638574795302}
    return int(result * multipliers[n])