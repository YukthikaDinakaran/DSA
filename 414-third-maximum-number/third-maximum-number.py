class Solution(object):
    def thirdMax(self, nums):
        nums = list(set(nums))
        if len(nums)==1 or len(nums)==0 or len(nums)==2:
            return max(nums)
        nums.sort(reverse = True)
        return nums[2]

        