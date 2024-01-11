class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        dp = [0 for _ in range(n+1)]
        s = stones[:]
        for i in range(1, n):
            s[i] += s[i-1]
        dp[n-1] = s[n-1]
        for i in range(n-2, 0, -1):
            dp[i] = max(dp[i+1], s[i] - dp[i+1])
        dp[0] = max(dp[1], s[1] - dp[2])
        return dp[0]