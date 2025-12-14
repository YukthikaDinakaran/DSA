class Solution(object):
    def romanToInt(self, s):
        ## create an array for mapping 
        rom = [0]*26
        rom[ord('I')-ord('A')] = 1
        rom[ord('V')-ord('A')] = 5
        rom[ord('X')-ord('A')] = 10
        rom[ord('L')-ord('A')] = 50
        rom[ord('C')-ord('A')] = 100
        rom[ord('D')-ord('A')] = 500
        rom[ord('M')-ord('A')] = 1000

        result = 0
        prev = -1
        for i in range(len(s)):
            curridx = ord(s[i])-ord('A')
            currval = rom[curridx]
            if ( prev == -1 or currval <= prev):
                result = result + currval  
            else:
                result = result + (currval - 2*prev)
            prev = currval
        return result
        """
        :type s: str
        :rtype: int
        """
        