class Solution(object):
    def maxSizeSlices(self, slices):
        """
        :type slices: List[int]
        :rtype: int
        """
        n = len(slices) // 3
        dp = [[0 for _ in range(n+1)] for _ in range(3*n)]
        dp[0][1] = slices[0]
        dp[1][1] = max(slices[0], slices[1])
        for i in range(2, 3*n):
            dp[i][1] = max(dp[i-1][1], slices[i])
            for j in range(2, min(n, i//2+1) + 1):
                dp[i][j] = max(dp[i-1][j], dp[i-2][j-1] + slices[i])
        ans = dp[-2][n]
        dp = [[0 for _ in range(n+1)] for _ in range(3*n)]
        dp[0][1] = 0
        dp[1][1] = slices[1]
        for i in range(2, 3*n):
            dp[i][1] = max(dp[i-1][1], slices[i])
            for j in range(2, min(n, i//2+1) + 1):
                dp[i][j] = max(dp[i-1][j], dp[i-2][j-1] + slices[i])
        return max(ans, dp[-1][n])