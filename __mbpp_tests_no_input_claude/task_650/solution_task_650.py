def are_Equal(arr1, arr2, n1, n2):
    if n1 != n2:
        return False
    
    sum1 = sum(arr1)
    sum2 = sum(arr2)
    
    return sum1 == sum2