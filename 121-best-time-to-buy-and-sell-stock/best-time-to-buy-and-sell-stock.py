class Solution(object):
    def maxProfit(self, prices):
        res =0
        Min = prices[0]
        n = len(prices)
        for i in range(0,n):
            Min = min(Min, prices[i])
            res = max(res, prices[i]-Min)
        return res

        """
        :type prices: List[int]
        :rtype: int
        """
        