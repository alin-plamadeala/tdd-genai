def second_frequent(arr):
    freq = {}
    for item in arr:
        freq[item] = freq.get(item, 0) + 1
    
    if len(freq) < 2:
        return None
        
    sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_freq[1][0]