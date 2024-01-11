class Solution(object):
    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(1, n):
            stones[i] += stones[i-1]
        stones.append(0)
        # print(stones)
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                dp[i][j] = max(stones[j] - stones[i] - dp[i+1][j], stones[j-1] - stones[i-1] - dp[i][j-1])
        # print(dp)
        return dp[0][n-1]