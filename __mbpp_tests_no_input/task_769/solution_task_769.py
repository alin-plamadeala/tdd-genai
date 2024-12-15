def Diff(list1, list2):
    # Create sets for faster lookup
    set1 = set(list1)
    set2 = set(list2)
    
    # Find elements in list1 but not in list2, preserving order
    diff1 = [x for x in list1 if x not in set2]
    # Find elements in list2 but not in list1, preserving order
    diff2 = [x for x in list2 if x not in set1]
    
    # Combine the two lists while preserving order
    return diff1 + diff2
