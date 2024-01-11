class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        m = len(str1)
        n = len(str2)
        dp = [[j for j in range(n+1)] for i in range(m+1)]
        for i in range(m):
            dp[i+1][0] = i+1
            for j in range(n):
                if str1[i] == str2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1]) + 1
        ans = ""
        i = m - 1
        j = n - 1
        while(i > -1 or j > -1):
            if i == -1:
                ans = str2[:j+1] + ans
                break
            elif j == -1:
                ans = str1[:i+1] + ans
                break
            if str1[i] == str2[j]:
                ans = str1[i] + ans
                i -= 1
                j -= 1
            elif dp[i+1][j+1] == dp[i+1][j] + 1:
                ans = str2[j] + ans
                j -= 1
            else:
                ans = str1[i] + ans
                i -= 1
        return ans