from typing import List, Tuple

def find_closet(arr1: List[int], arr2: List[int], arr3: List[int], n1: int, n2: int, n3: int) -> Tuple[int, int, int]:
    i, j, k = 0, 0, 0
    min_diff = float('inf')
    result = (0, 0, 0)
    
    while i < n1 and j < n2 and k < n3:
        current_min = min(arr1[i], arr2[j], arr3[k])
        current_max = max(arr1[i], arr2[j], arr3[k])
        
        if current_max - current_min < min_diff:
            min_diff = current_max - current_min
            result = (arr1[i], arr2[j], arr3[k])
        
        if min_diff == 0:
            break
        
        if current_min == arr1[i]:
            i += 1
        elif current_min == arr2[j]:
            j += 1
        else:
            k += 1
    
    return result