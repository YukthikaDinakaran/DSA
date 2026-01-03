class Solution(object):
    def longestPalindrome(self, s):
        ans = ""
        n = len(s)
        if n == 1:
            return s[0]
        if n==2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        for i in range(n):
            l , r = i, i
            while l >=0 and r< n and s[l]==s[r]:
                if r-l+1 > len(ans):
                    ans = s[l:r+1]
                l -= 1
                r += 1
            l , r = i , i+1
            while l>= 0 and r < n and s[l] == s[r]:
                if r-l+1 > len(ans):
                    ans = s[l:r+1]
                l -= 1
                r +=1
        return ans
        """
        :type s: str
        :rtype: str
        """
        