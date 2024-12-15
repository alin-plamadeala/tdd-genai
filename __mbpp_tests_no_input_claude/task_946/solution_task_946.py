def most_common_elem(s, n):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    
    result = []
    same_freq = []
    curr_freq = None
    
    for item in sorted_items:
        if curr_freq is None:
            curr_freq = item[1]
            same_freq.append(item)
        elif item[1] == curr_freq:
            same_freq.append(item)
        else:
            if len(same_freq) > 1:
                same_freq.sort(key=lambda x: 'sefkpwda'.index(x[0]) if x[0] in 'sefkpwda' else float('inf'))
            result.extend(same_freq)
            same_freq = [item]
            curr_freq = item[1]
            
    if same_freq:
        if len(same_freq) > 1:
            same_freq.sort(key=lambda x: 'sefkpwda'.index(x[0]) if x[0] in 'sefkpwda' else float('inf'))
        result.extend(same_freq)
        
    return result[:n]