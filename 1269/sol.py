class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        n = min(arrLen, steps//2+1)
        dp = [0 for _ in range(n)]
        dp[0] = 1
        last_tmp = 0
        for _ in range(steps):
            for i in range(n):
                last = last_tmp
                last_tmp = dp[i]
                if i > 0:
                    dp[i] += last
                if i < n - 1:
                    dp[i] += dp[i+1]
        return dp[0] % (10**9+7)