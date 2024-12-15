def sub_lists(lst):
    n = len(lst)
    result = [[]]
    
    for i in range(n):
        result.append([lst[i]])
        
    for i in range(n):
        for j in range(i+1, n):
            result.append([lst[i], lst[j]])
            
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                result.append([lst[i], lst[j], lst[k]])
                
    if n > 3:
        result.append(lst[:])
        
    return result