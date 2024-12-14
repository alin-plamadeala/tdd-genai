def count_duplic(lst):
    unique_elements = []
    counts = []
    
    for item in lst:
        if item in unique_elements:
            counts[unique_elements.index(item)] += 1
        else:
            unique_elements.append(item)
            counts.append(1)
    
    return unique_elements, counts
