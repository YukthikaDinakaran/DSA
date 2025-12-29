class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        n = len(nums)
        nums.sort()
        longest = 1
        curr = 1
        for i in range(n):
            if nums[i] == nums[i-1] + 1:
                curr += 1
            elif nums[i] != nums[i-1]:
                curr = 1
            longest = max(longest, curr)
        return longest
        """
        :type nums: List[int]
        :rtype: int
        """
        