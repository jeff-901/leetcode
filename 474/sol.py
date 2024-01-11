class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for s in strs:
            cnt1 = 0
            cnt0 = 0
            for c in s:
                if c == "1":
                    cnt1 += 1
                else:
                    cnt0 += 1
            for i in range(m, cnt0-1, -1):
                for j in range(n, cnt1-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-cnt0][j-cnt1] + 1)
        return dp[-1][-1]