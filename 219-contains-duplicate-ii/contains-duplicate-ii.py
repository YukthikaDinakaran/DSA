class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        last = {}
        for i, val in enumerate(nums):
            if val in last and i - last[val] <= k:
                return True
            last[val] = i
        return False

        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        