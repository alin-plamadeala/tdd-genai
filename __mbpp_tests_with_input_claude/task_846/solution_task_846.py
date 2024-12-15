def find_platform(arrival, departure, n):
    arrival.sort()
    departure.sort()
    
    platforms = 1
    result = 1
    i = 1
    j = 0
    
    while i < n and j < n:
        if arrival[i] <= departure[j]:
            platforms += 1
            i += 1
        elif arrival[i] > departure[j]:
            platforms -= 1
            j += 1
        
        result = max(result, platforms)
    
    return result