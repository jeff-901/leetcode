class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        dp = [(n-j) for j in range(n+1)]
        for i in range(m-1, -1, -1):
            last = dp[:]
            dp[-1] = abs(m - i)
            for j in range(n-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[j] = last[j+1]
                else:
                    dp[j] = min(last[j], dp[j+1], last[j+1]) + 1
        return dp[0]