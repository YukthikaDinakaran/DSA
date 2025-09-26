class Solution(object):
    def isHappy(self, n):
       seen = set()
       def digit_square_sum(num):
        return sum(int(d)**2 for d in str(num))
       while n != 1 and n not in seen:
            seen.add(n)
            n = digit_square_sum(n)
       return n == 1
        