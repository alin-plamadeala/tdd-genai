def get_Pairs_Count(arr, n, sum):
    count = 0
    freq = {}
    for num in arr:
        if sum - num in freq:
            count += freq[sum - num]
        freq[num] = freq.get(num, 0) + 1
    return count