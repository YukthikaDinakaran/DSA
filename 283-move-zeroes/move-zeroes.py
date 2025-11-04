class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        if n==0:
            return nums
        a = []
        b = []
        for i in range(n):
            if nums[i]!= 0:
                b.append(nums[i])
            else:
                a.append(0)
        res = b+a
        for i in range(n):
            nums[i] = res[i]
       