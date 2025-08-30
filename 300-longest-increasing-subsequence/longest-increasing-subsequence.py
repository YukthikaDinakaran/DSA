class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        lis = [1]*n
        if n==0:
            return 0

        for i in range(1,n):
            for j in range(0,i):
                if nums[i]>nums[j]:
                    lis[i] = max(lis[i], lis[j]+1)
        return max(lis)
        
        """
        :type nums: List[int]
        :rtype: int
        """
        