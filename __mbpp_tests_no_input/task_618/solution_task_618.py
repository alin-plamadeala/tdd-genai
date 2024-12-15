def div_list(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")
    return [x / y for x, y in zip(list1, list2)]
