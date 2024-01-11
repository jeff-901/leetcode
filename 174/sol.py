class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [0 for _ in range(n)]
        dp[-1] = max(-dungeon[-1][-1] + 1, 1)
        for j in range(n-2, -1, -1):
            dp[j] = max(dp[j+1] - dungeon[-1][j], 1)
        for i in range(m-2, -1, -1):
            dp[-1] = max(dp[-1] - dungeon[i][-1], 1)
            for j in range(n-2, -1, -1):
                dp[j] = max(min(dp[j], dp[j+1]) - dungeon[i][j], 1)
        return dp[0]