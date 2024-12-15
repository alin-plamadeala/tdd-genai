def second_frequent(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    
    sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_freq[1][0]