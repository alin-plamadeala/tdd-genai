def Diff(list1, list2):
    set2 = set(list2)
    result = [item for item in list1 if item not in set2]
    result.extend([item for item in list2 if item not in list1])
    return result