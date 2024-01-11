class Solution(object):
    def minimumPartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = len(str(k))
        n = len(s)
        if k < 10:
            for c in s:
                if int(c) > k:
                    return -1
            return n
        dp = [0 for _ in range(n)]
        for i in range(min(l-1, n)):
            dp[i] = 1
        cur = int(s[:l-1])
        mod = 10 ** (l - 1)
        for i in range(l-1, n):
            cur = cur * 10 + int(s[i])
            if cur <= k:
                dp[i] = dp[i - l] + 1
            else:
                dp[i] = dp[i - l + 1] + 1
            cur %= mod
            # print(dp)
        return dp[-1]