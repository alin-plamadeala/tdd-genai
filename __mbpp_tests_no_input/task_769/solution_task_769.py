def Diff(list1, list2):
    result = []
    
    # Add elements from list1 that are not in list2, maintaining order
    for item in list1:
        if item not in list2:
            result.append(item)
    
    # Add elements from list2 that are not in list1, maintaining order
    for item in list2:
        if item not in list1:
            result.append(item)
    
    # Reorder result based on the order of first appearance in the original lists
    ordered_result = []
    for item in list1 + list2:
        if item in result and item not in ordered_result:
            ordered_result.append(item)
    
    return ordered_result
