class Solution(object):
    def checkInclusion(self, s1, s2):
        n, m = len(s1), len(s2)
        if n > m:
            return False

        cnt1 = [0] * 26
        cnt2 = [0] * 26

        for ch in s1:
            cnt1[ord(ch) - ord('a')] += 1

        for i in range(n):
            cnt2[ord(s2[i]) - ord('a')] += 1

        if cnt1 == cnt2:
            return True

        for i in range(n, m):
            cnt2[ord(s2[i]) - ord('a')] += 1
            cnt2[ord(s2[i-n]) - ord('a')] -= 1
            if cnt1 == cnt2:
                return True

        return False
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        