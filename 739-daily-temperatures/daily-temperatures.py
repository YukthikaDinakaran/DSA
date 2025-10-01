class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        ans = [0] * n
        stack = []  # stores indices
        
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                prev = stack.pop()
                ans[prev] = i - prev
            stack.append(i)
        
        return ans
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        