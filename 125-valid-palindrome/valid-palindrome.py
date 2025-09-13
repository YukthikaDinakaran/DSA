class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        n= len(s)
        if n == 0:
            return True  
        first = 0
        sec = n-1
        while first<sec:
            if s[first] != s[sec] :
                return False
            else:
                first +=1
                sec -= 1
        return True
        """
        :type s: str
        :rtype: bool
        """
        