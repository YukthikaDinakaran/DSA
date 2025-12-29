class Solution(object):
    def longestConsecutive(self, nums):
        n = set(nums)
        longest = 0
        for i in n:
            if i-1 not in n:
                curr = i
                cnt = 1
                while curr+1 in n:
                    curr += 1
                    cnt += 1
                longest = max(longest, cnt)
        return longest
        """
        :type nums: List[int]
        :rtype: int
        """
        