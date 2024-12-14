def subset(arr, k):
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1
    
    min_subsets = float('inf')
    for freq in count.values():
        min_subsets = min(min_subsets, freq)
    
    return min_subsets // k if min_subsets != float('inf') else 0