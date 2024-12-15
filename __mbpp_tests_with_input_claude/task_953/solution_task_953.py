def subset(arr, n):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    max_freq = max(freq.values())
    return max_freq