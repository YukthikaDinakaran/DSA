class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0

        while x != 0:
            digit = x % 10
            x //= 10

            # Check for overflow before multiplying
            if rev > (2**31 - 1) // 10 or (rev == (2**31 - 1) // 10 and digit > 7):
                return 0

            rev = rev * 10 + digit

        return sign * rev
        """
        :type x: int
        :rtype: int
        """
        