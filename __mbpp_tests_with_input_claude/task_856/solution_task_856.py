def find_Min_Swaps(arr, n):
    ones = sum(arr)
    count_ones = sum(arr[:ones])
    max_ones = count_ones
    for i in range(ones, n):
        count_ones = count_ones - arr[i - ones] + arr[i]
        max_ones = max(max_ones, count_ones)
    return ones - max_ones