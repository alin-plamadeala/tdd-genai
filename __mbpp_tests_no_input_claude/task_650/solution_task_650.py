def are_Equal(arr1, arr2, n1, n2):
    if n1 != n2:
        return False
    
    arr1.sort()
    arr2.sort()
    
    for i in range(n1):
        if arr1[i] != arr2[i]:
            return False
            
    return True