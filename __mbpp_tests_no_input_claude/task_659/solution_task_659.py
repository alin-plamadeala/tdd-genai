def Repeat(arr):
    seen = set()
    repeated = set()
    result = []
    
    for num in arr:
        if num in seen:
            repeated.add(num)
        else:
            seen.add(num)
            
    for num in arr:
        if num in repeated and num not in result:
            result.append(num)
            
    return result