def max_similar_indices(list1, list2):
    def sum_of_pairs(pair):
        return pair[0] + pair[1]
    
    max_sum_list1 = max(list1, key=sum_of_pairs)
    max_sum_list2 = max(list2, key=sum_of_pairs)
    
    if sum_of_pairs(max_sum_list1) > sum_of_pairs(max_sum_list2):
        return list1
    else:
        return list2
