from typing import List

def rearrange_numbs(arr: List[int]) -> List[int]:
    # Separate positive and negative numbers
    positives = [x for x in arr if x >= 0]
    negatives = [x for x in arr if x < 0]
    
    # Sort positives in ascending order
    positives.sort()
    
    # Sort negatives in descending order
    negatives.sort(reverse=True)
    
    # Combine the sorted positives and negatives
    return positives + negatives[::-1]
