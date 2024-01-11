class Solution(object):
    def numberOfArrays(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = len(str(k))
        n = len(s)
        dp = [1] + [0 for _ in range(n)]
        for i in range(n):
            if s[i] == "0":
                continue
            for j in range(i, min(i+l, n)):
                if int(s[i:j+1]) > k:
                    break
                dp[j+1] = (dp[j+1] + dp[i]) % 1000000007
        return dp[-1]