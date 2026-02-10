class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        s = set(nums)
        a = []
        for i in range(1, n+1):
            if i not in s:
                a.append(i)
        return a

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        