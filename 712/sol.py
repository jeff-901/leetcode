class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m = len(s1)
        n = len(s2)
        dp = [ord(s2[j]) for j in range(n)] + [0]
        for j in range(n-1, -1, -1):
            dp[j] += dp[j+1]
        for i in range(m-1, -1, -1):
            last = dp[:]
            dp = [0 for _ in range(n+1)]
            dp[-1] = last[-1] + ord(s1[i])
            for j in range(n-1, -1, -1):
                if s1[i] == s2[j]:
                    dp[j] = last[j+1]
                else:
                    dp[j] = min(last[j] + ord(s1[i]), dp[j+1] + ord(s2[j]))
        return dp[0]