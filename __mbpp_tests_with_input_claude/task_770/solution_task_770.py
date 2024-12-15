def odd_Num_Sum(n):
    sum = 0
    count = 1
    for i in range(n):
        sum += count ** 4
        count += 2
    return sum