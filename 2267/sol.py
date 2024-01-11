class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])
        if (n + m) % 2 == 0:
            return False
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        if grid[-1][-1] == ")":
            dp[-1][-1] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                prev = -1
                if i < m-1:
                    prev = max(prev, dp[i+1][j])
                if j < n-1:
                    prev = max(prev, dp[i][j+1])
                if prev < 0:
                    dp[i][j] == -1
                elif grid[i][j] == ")":
                    dp[i][j] = prev + 1
                else:
                    dp[i][j] = prev - 1
        if dp[0][0] < 0:
            return False
        if dp[0][0] == 0:
            return True
        # print(dp)
        if grid[0][0] == "(":
            grid[0][0] = 1
        else:
            grid[0][0] = -1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                prev = -1
                flag = dp[i][j] >= 0
                if i > 0:
                    if grid[i-1][j] == dp[i][j] and flag:
                        return True
                    prev = max(prev, grid[i-1][j])
                if j > 0:
                    if grid[i][j-1] == dp[i][j] and flag:
                        return True
                    prev = max(prev, grid[i][j-1])
                if prev < 0:
                    grid[i][j] = -1
                elif grid[i][j] == "(":
                    grid[i][j] = prev + 1
                else:
                    grid[i][j] = prev - 1
        # print(grid)
        return False