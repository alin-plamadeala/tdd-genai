def Diff(list1, list2):
    diff1 = [item for item in list1 if item not in list2]
    diff2 = [item for item in list2 if item not in list1]
    return sorted(diff1 + diff2)