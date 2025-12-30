class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        mp = {}
        for i in range(n):
            j = target - nums[i]
            if j in mp:
                return [mp[j], i]
            mp[nums[i]] = i 
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        