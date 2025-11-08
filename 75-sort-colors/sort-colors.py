class Solution(object):
    def sortColors(self, nums):
        n = len(nums)
        c1 = 0
        c2 = 0
        c3 = 0
        for i in range(n):
            if nums[i] == 0:
                c1 = c1+1
            elif nums[i] == 1:
                c2 = c2+1
            else:
                c3 = c3+1
        nums[:] = [0]*c1+[1]*c2+[2]*c3
        return nums

        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        