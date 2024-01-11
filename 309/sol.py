class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[0, -1000], [0, -1000]]
        for price in prices:
            tmp = dp.pop(0)
            dp.append([max(dp[0][0], dp[0][1] + price), max(dp[0][1], tmp[0] - price)])
        return dp[-1][0]