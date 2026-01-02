class Solution(object):
    def hammingWeight(self, n):
        cnt = 0
        while n > 0:
            if n&1:
                cnt +=1
            n= n>>1
        return cnt 
        """
        :type n: int
        :rtype: int
        """
        