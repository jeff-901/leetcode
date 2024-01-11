class Solution(object):
    def new21Game(self, n, k, maxPts):
        """
        :type n: int
        :type k: int
        :type maxPts: int
        :rtype: float
        """
        if k > n:
            return 0
        min_len = min(k + maxPts, n + 1)
        dp = [0.0] * min_len
        dp[0] = 1.0
        s = 1.0 if k != 0 else 0.0
        for i in range(1, min_len):
            if i > maxPts:
                s -= dp[i-maxPts-1]
            dp[i] = s / maxPts
            if i < k:
                s += dp[i]
        return sum(dp[k:min_len])