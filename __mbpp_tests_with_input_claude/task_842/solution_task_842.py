def get_odd_occurence(arr, n):
    result = 0
    for num in arr:
        result ^= num
    return result