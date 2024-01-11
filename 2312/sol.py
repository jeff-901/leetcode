class Solution(object):
    def sellingWood(self, m, n, prices):
        """
        :type m: int
        :type n: int
        :type prices: List[List[int]]
        :rtype: int
        """
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for h, w, p in prices:
            dp[h][w] = max(dp[h][w], p)
        for i in range(1, m+1):
            for j in range(1, n+1):
                for h in range(1, i//2+1):
                    dp[i][j] = max(dp[i][j], dp[i-h][j] + dp[h][j])
                for w in range(1, j//2+1):
                    dp[i][j] = max(dp[i][j], dp[i][j-w] + dp[i][w])
        return dp[m][n]