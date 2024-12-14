def max_similar_indices(list1, list2):
    max_similarity = 0
    max_similar_list = []
    
    for i in range(len(list1)):
        similarity = sum(1 for a, b in zip(list1[i], list2[i]) if a == b)
        if similarity > max_similarity:
            max_similarity = similarity
            max_similar_list = list2
    
    return max_similar_list