def get_Pairs_Count(arr, n, k):
    count = 0
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    for num in arr:
        if k - num in freq:
            count += freq[k - num]
            if k - num == num:
                count -= 1
    return count // 2