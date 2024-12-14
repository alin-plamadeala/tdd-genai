from typing import List

def find_platform(arrival: List[int], departure: List[int], n: int) -> int:
    arrival.sort()
    departure.sort()
    
    platform_needed = 1
    result = 1
    i = 1
    j = 0
    
    while i < n and j < n:
        if arrival[i] <= departure[j]:
            platform_needed += 1
            i += 1
        elif arrival[i] > departure[j]:
            platform_needed -= 1
            j += 1
        
        if platform_needed > result:
            result = platform_needed
    
    return result