def find_platform(arrival, departure, n):
    arrival.sort()
    departure.sort()
    
    platforms = 1
    max_platforms = 1
    i = 1
    j = 0
    
    while i < n and j < n:
        if arrival[i] <= departure[j]:
            platforms += 1
            i += 1
        elif arrival[i] > departure[j]:
            platforms -= 1
            j += 1
        
        max_platforms = max(platforms, max_platforms)
    
    return max_platforms