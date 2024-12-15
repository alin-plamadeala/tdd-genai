def get_Pairs_Count(arr, n, target_sum):
    count = 0
    freq = {}

    for num in arr:
        complement = target_sum - num
        if complement in freq:
            count += freq[complement]
        freq[num] = freq.get(num, 0) + 1

    return count
