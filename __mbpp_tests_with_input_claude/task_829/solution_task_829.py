def second_frequent(sequence):
    frequency = {}
    for item in sequence:
        frequency[item] = frequency.get(item, 0) + 1
    
    sorted_items = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))
    
    if len(sorted_items) < 2:
        return None
    
    return sorted_items[1][0]