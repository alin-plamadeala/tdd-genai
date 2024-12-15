def count_duplic(lst):
    if not lst:
        return [], []
    
    values = []
    counts = []
    current_count = 1
    current_value = lst[0]
    
    for i in range(1, len(lst)):
        if lst[i] == current_value:
            current_count += 1
        else:
            values.append(current_value)
            counts.append(current_count)
            current_value = lst[i]
            current_count = 1
            
    values.append(current_value)
    counts.append(current_count)
    
    if len(lst) == len(set(lst)):
        return lst, [1] * len(lst)
        
    result_values = []
    result_counts = []
    
    i = 0
    while i < len(values):
        if i < len(values) - 1 and values[i] == values[i + 1]:
            result_values.append(values[i])
            result_counts.append(counts[i] + counts[i + 1])
            i += 2
        else:
            result_values.append(values[i])
            result_counts.append(counts[i])
            i += 1
            
    return result_values, result_counts