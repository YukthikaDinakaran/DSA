class Solution(object):
    def intersection(self, nums1, nums2):
        res = set()
        for i in nums1:
            for j in nums2:
                if i==j :
                    res.add(i)
        return list(res)

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        