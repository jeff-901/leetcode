class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m = len(s)
        n = len(t)
        dp = [0] * m
        for j in range(m):
            if s[j] == t[0]:
                dp[j] = 1
        for i in range(1, n):
            last = dp[:]
            dp = [0] * m
            pre = 0
            for j in range(m):   
                if s[j] == t[i]:
                    # print(i, j, pre)
                    dp[j] = pre
                if s[j] == t[i-1]:
                    # print(i, j, dp[i-1][j])
                    pre += last[j]
            # print(dp)
        return sum(dp)