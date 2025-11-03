class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        if nums[0]== target:
            return 0
        if target < nums[0]:
            return 0
        for i in range(1,n):
            if nums[i] == target:
                return i
            if nums[i-1] < target and target < nums[i]:
                return i 
        return n
        

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        