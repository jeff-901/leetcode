class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        dp = [[0 for _ in range(k+1)] for _ in range(n)]
        dp[0][0] = 1
        for end in range(1, n):
            for cnt in range(k+1):
                dp[end][cnt] = dp[end-1][cnt]
                if cnt > 0:
                    dp[end][cnt] += dp[end-1][cnt-1]
                    dp[end][cnt] += dp[end-1][cnt]
                    if end > 1:
                        dp[end][cnt] -= dp[end-2][cnt]
                dp[end][cnt] %= 1000000007
            # print(dp[end])
            # print(end, "==========")
        return dp[-1][k]
