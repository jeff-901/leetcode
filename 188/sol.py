class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(2*k)]
        for i in range(k):
            dp[2*i] = -1000
        for price in prices:
            dp[0] = max(dp[0], -price)
            for i in range(1, 2*k):
                if i % 2:
                    dp[i] = max(dp[i], dp[i-1] + price)
                else:
                    dp[i] = max(dp[i], dp[i-1] - price)
        return max([dp[i*2+1] for i in range(k)])