def largest_subset(arr, n):
    if n == 0:
        return 0
    
    remainder_count = [0] * n
    
    for num in arr:
        remainder = num % n
        remainder_count[remainder] += 1
    
    count = min(remainder_count[0], 1)
    
    for i in range(1, (n // 2) + 1):
        if i == n - i:
            count += min(remainder_count[i], 1)
        else:
            count += max(remainder_count[i], remainder_count[n - i])
    
    return count