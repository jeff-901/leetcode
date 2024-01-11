class Solution(object):
    def numberOfPaths(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(k)] for _ in range(n)]
        dp[0][grid[0][0] % k] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if j > 0:
                    cnt = [(a + b) % 1000000007 for a, b in zip(dp[j], dp[j-1])]
                else:
                    cnt = dp[j][:]
                shift = grid[i][j] % k
                dp[j] = cnt[k-shift:] + cnt[:k-shift]
        return dp[-1][0] % 1000000007