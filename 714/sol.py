class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        ans = 0
        buy_cost = -50000
        for price in prices:
            tmp = ans
            ans = max(ans, buy_cost + price - fee)
            buy_cost = max(buy_cost, tmp - price)
        return ans