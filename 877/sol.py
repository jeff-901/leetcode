class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = piles[:]
        for d in range(1, n):
            for j in range(n-d):
                dp[j] = max(piles[j] - dp[j+1], piles[j+d] - dp[j])
        return dp[0] > 0