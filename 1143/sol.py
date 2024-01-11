class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1)
        n = len(text2)
        dp = [0 for _ in range(n+1)]
        for i in range(m):
            last = dp[0]
            for j in range(n):
                tmp = dp[j+1]
                if text1[i] == text2[j]:
                    dp[j+1] = last + 1
                else:
                    dp[j+1] = max(dp[j], dp[j+1])
                last = tmp
        return dp[-1]