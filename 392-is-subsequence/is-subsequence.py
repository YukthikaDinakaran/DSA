class Solution(object):
    def isSubsequence(self, s, t):
        n = len(s)
        m= len(t)
        i=0
        j=0
        while i<n and j<m:
            if s[i]==t[j]:
                i = i+1
            j = j+1
        if i== n:
            return True
        else:
            return False