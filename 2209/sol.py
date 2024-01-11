class Solution(object):
    def minimumWhiteTiles(self, floor, numCarpets, carpetLen):
        """
        :type floor: str
        :type numCarpets: int
        :type carpetLen: int
        :rtype: int
        """
        n = len(floor)
        dp = [[0 for _ in range(numCarpets+1)] for _ in range(n + 1)]
        for i, tile in enumerate(floor):
            if tile == "0":
                dp[i] = dp[i-1][:]
            else:
                dp[i][0] = dp[i-1][0] + 1
                for j in range(1, numCarpets+1):
                    dp[i][j] = min(dp[i-1][j] + 1, dp[max(-1, i - carpetLen)][j-1])
        return dp[n-1][-1]
