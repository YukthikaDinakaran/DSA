class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [1]*(n)
        for i in range(0,n):
            for j in range (0,i):
                if(nums[i] > nums[j]):
                    dp[i] = max(dp[i],dp[j]+1 )
                else:
                    dp[i] = max(dp[i],1)
        return max(dp)
                