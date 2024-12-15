def find_closet(arr1, arr2, arr3, n1, n2, n3):
    i, j, k = 0, 0, 0
    diff = float('inf')
    res_i, res_j, res_k = 0, 0, 0
    
    while i < n1 and j < n2 and k < n3:
        minimum = min(arr1[i], arr2[j], arr3[k])
        maximum = max(arr1[i], arr2[j], arr3[k])
        current_diff = maximum - minimum
        
        if current_diff < diff:
            diff = current_diff
            res_i, res_j, res_k = arr1[i], arr2[j], arr3[k]
        elif current_diff == diff:
            if arr1[i] <= res_i:
                res_i, res_j, res_k = arr1[i], arr2[j], arr3[k]
        
        if arr1[i] == minimum:
            i += 1
        elif arr2[j] == minimum:
            j += 1
        else:
            k += 1
            
    return (res_i, res_j, res_k)