def min_Num(arr, n):
    total_sum = sum(arr)
    if total_sum % 2 == 0:
        return 2
    else:
        return 1