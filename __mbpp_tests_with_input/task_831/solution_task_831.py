def count_Pairs(arr, target):
    from collections import Counter
    
    count = 0
    freq = Counter(arr)
    
    for num in freq:
        complement = target - num
        if complement in freq:
            if complement == num:
                count += freq[num] * (freq[num] - 1) // 2
            elif complement > num:
                count += freq[num] * freq[complement]
    
    return count
