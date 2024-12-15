def find_closet(arr1, arr2, arr3, n1, n2, n3):
    diff = float('inf')
    res_i = res_j = res_k = 0
    i = j = k = 0
    
    while i < n1 and j < n2 and k < n3:
        minimum = min(arr1[i], arr2[j], arr3[k])
        maximum = max(arr1[i], arr2[j], arr3[k])
        
        if maximum - minimum < diff:
            res_i, res_j, res_k = i, j, k
            diff = maximum - minimum
            
        if diff == 0:
            break
            
        if arr1[i] == minimum:
            i += 1
        elif arr2[j] == minimum:
            j += 1
        else:
            k += 1
            
        if i == n1 or j == n2 or k == n3:
            break
            
    return arr1[res_i], arr2[res_j], arr3[res_k]