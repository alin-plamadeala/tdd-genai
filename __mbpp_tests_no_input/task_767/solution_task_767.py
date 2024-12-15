def get_Pairs_Count(arr, n, k):
    count = 0
    freq = {}

    for num in arr:
        complement = k - num
        if complement in freq:
            count += freq[complement]
        freq[num] = freq.get(num, 0) + 1

    return count
