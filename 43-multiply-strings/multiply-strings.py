class Solution(object):
    def multiply(self, num1, num2):
        if (num1== "0" or num2== "0"):
            return "0"
        n = len(num1)
        m = len(num2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = [0]*(m+n)
        for i in range(n):
            for j in range(m):
                mul = int(num1[i]) * int(num2[j])
                res[i + j] += mul
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10
        while len(res) > 1 and res[-1] == 0:
            res.pop()

        return "".join(map(str, res[::-1]))
        
        