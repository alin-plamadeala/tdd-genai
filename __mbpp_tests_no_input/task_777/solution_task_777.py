def find_Sum(arr, n):
    total = 0
    for num in arr:
        if num % n == 0:
            total += num
    return total