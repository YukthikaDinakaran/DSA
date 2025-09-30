class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        res = 0
        left = 0
        sub = set()
        for right in range(n):
            while s[right] in sub:
                sub.remove(s[left])
                left +=1
            sub.add(s[right])
            res = max(res, right-left+1)
        return res
        
        """
        :type s: str
        :rtype: int
        """
        