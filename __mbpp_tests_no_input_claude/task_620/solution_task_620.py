def largest_subset(arr, n):
    arr.sort()
    dp = [1] * n
    max_len = 1
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] % arr[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
        max_len = max(max_len, dp[i])
    
    return max_len