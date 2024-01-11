class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0 for _ in range(n)]
        for i in range(n-2, -1, -1):
            last = dp[i]
            for j in range(i+1, n):
                tmp = dp[j]
                if s[i] == s[j]:
                    dp[j] = last
                else:
                    dp[j] = 1 + min(dp[j], dp[j-1])
                last = tmp
        return dp[-1]