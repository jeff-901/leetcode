class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1 = -100000
        profit1 = 0
        buy2 = -100000
        ans = 0
        for price in prices:
            buy1 = max(buy1, -price)
            profit1 = max(profit1, price + buy1)
            buy2 = max(buy2, profit1 - price)
            ans = max(ans, profit1, price + buy2)
        return ans