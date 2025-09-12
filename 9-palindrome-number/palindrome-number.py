class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        og = x
        rev = 0
        while(x>0):
            d = x%10
            rev = rev*10+d
            x//=10
        if(rev==og):
            return True
        else:
            return False


        """
        :type x: int
        :rtype: bool
        """
        