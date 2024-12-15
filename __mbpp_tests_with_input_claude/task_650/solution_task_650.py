def are_Equal(array1, array2, n1, n2):
    if n1 != n2:
        return False
    
    array1.sort()
    array2.sort()
    
    for i in range(n1):
        if array1[i] != array2[i]:
            return False
            
    return True