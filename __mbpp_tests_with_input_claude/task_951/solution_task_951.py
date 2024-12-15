def max_similar_indices(list1, list2):
    max_indices = []
    for i in range(len(list2)):
        max_val = 0
        max_tuple = None
        for j in range(len(list1)):
            if list1[j][1] == list2[i][1]:
                if list2[i][0] > max_val:
                    max_val = list2[i][0]
                    max_tuple = list2[i]
        if max_tuple:
            max_indices.append(max_tuple)
        else:
            max_indices.append(list2[i])
    return max_indices