class Solution(object):
    def longestPalindrome(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        s = word1 + word2
        dp = [1 for _ in range(m+n)]
        ans = 0
        for i in range(m+n-1, -1, -1):
            last = 0
            for j in range(i+1, m+n):
                tmp = dp[j]
                if s[i] == s[j]:
                    dp[j] = last + 2
                    if i < m and j >= m:
                        ans = max(ans, dp[j])
                else:
                    dp[j] = max(dp[j], dp[j-1])
                last = tmp
        return ans