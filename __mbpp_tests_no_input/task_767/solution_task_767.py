from collections import defaultdict

def get_Pairs_Count(arr, n, sum_value):
    count = 0
    freq = defaultdict(int)
    
    for i in range(n):
        complement = sum_value - arr[i]
        if complement in freq:
            count += freq[complement]
        freq[arr[i]] += 1
    
    return count