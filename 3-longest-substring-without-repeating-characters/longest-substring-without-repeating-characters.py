class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        st = set()
        l = 0
        longest = 0
        for i in range(n):
            while s[i] in st:
                st.remove(s[l])
                l += 1
            st.add(s[i])
            longest = max(longest, i-l+1)
        return longest
        """
        :type s: str
        :rtype: int
        """
        