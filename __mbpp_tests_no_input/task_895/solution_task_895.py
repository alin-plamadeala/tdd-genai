class Solution:
    def max_sum_subseq(self, nums):
        if not nums:
            return 0
        
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        return dp[-1]
        

def max_sum_subseq(nums):
    solution = Solution()
    return solution.max_sum_subseq(nums)