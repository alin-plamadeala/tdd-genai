from collections import defaultdict

def count_duplic(lst):
    if not lst:
        return [], []
    
    unique_elements = []
    counts = []
    
    current_element = lst[0]
    current_count = 1
    
    for i in range(1, len(lst)):
        if lst[i] == current_element:
            current_count += 1
        else:
            unique_elements.append(current_element)
            counts.append(current_count)
            current_element = lst[i]
            current_count = 1
    
    unique_elements.append(current_element)
    counts.append(current_count)
    
    return unique_elements, counts