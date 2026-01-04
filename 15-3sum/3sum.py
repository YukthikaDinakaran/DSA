class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        res = set()

        for i in range(n):
            seen = set()
            for j in range(i+1, n):
                need = - (nums[i] + nums[j])
                if need in seen:
                    temp = sorted([nums[i], nums[j], need])
                    res.add(tuple(temp))
                seen.add(nums[j])

        return list(res)
