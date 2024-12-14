def pair_OR_Sum(arr, n):
    total_sum = 0
    length = len(arr)
    pair_count = 0

    for i in range(length):
        for j in range(i + 1, length):
            total_sum += arr[i] | arr[j]
            pair_count += 1
            if pair_count == n:
                return total_sum

    return total_sum