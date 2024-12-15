def max_sum_subseq(arr):
    n = len(arr)
    dp = [arr[i] for i in range(n)]
    prev = [-1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + arr[i]:
                dp[i] = dp[j] + arr[i]
                prev[i] = j
    
    max_sum = max(dp)
    max_idx = dp.index(max_sum)
    
    result = []
    while max_idx != -1:
        result.append(arr[max_idx])
        max_idx = prev[max_idx]
    
    valid_sum = 0
    prev_val = float('-inf')
    for val in reversed(result):
        if val > prev_val:
            valid_sum += val
            prev_val = val
            
    return valid_sum