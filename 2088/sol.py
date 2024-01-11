class Solution(object):
    def countPyramids(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        ans = 0
        dp = copy.deepcopy(grid)
        for i in range(1, m):
            for j in range(1, n-1):
                if dp[i][j] and dp[i-1][j] > 0:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j+1]) + 1
                    ans += dp[i][j] - 1
        dp = grid
        for i in range(m-2, -1, -1):
            for j in range(1, n-1):
                if dp[i][j] and dp[i+1][j] > 0:
                    dp[i][j] = min(dp[i+1][j-1], dp[i+1][j+1]) + 1
                    ans += dp[i][j] - 1
        return ans