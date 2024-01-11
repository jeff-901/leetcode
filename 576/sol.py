class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[startRow][startColumn] = 1
        ans = 0
        mod = 1000000007
        for _ in range(maxMove):
            tmp = [[0 for _ in range(n)] for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i > 0:
                        tmp[i][j] += dp[i-1][j]
                    else:
                        ans += dp[i][j]
                    if j > 0:
                        tmp[i][j] += dp[i][j-1]
                    else:
                        ans += dp[i][j]
                    if i < m - 1:
                        tmp[i][j] += dp[i+1][j]
                    else:
                        ans += dp[i][j]
                    if j < n - 1:
                        tmp[i][j] += dp[i][j+1]
                    else:
                        ans += dp[i][j]
                    tmp[i][j] %= mod
            dp = tmp
            ans %= mod
        return ans