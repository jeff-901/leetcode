class Solution(object):
    def checkPartitioning(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        dp[-1][-1] = True
        for i in range(n-2, -1, -1):
            dp[i][i] = True
            if s[i] == s[i+1]:
                dp[i][i+1] = True
            for j in range(i+2, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
        for i in range(n):
            if dp[0][i]:
                for j in range(i+1, n-1):
                    if dp[i+1][j] and dp[j+1][n-1]:
                        return True
        return False