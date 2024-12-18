def max_sum_subseq(arr):
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0]
    
    dp = [0] * len(arr)
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    
    for i in range(2, len(arr)):
        dp[i] = max(dp[i-1], dp[i-2] + arr[i])
    
    return dp[-1]