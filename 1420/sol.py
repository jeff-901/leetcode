class Solution(object):
    def numOfArrays(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        mod = 10 ** 9 + 7
        dp = [[[0 for _ in range(m)] for _ in range(k)] for _ in range(n)]
        for i in range(m):
            dp[0][0][i] = 1
        # for _ in range(k):
        #     print(dp[0][_])
        # print("==================")
        for l in range(1, n):  
            for j in range(min(k, l + 1)):
                for i in range(m):
                    dp[l][j][i] = (dp[l-1][j][i] * (i+1)) % mod
                    if j > 0:
                        dp[l][j][i] += sum(dp[l-1][j-1][:i])
                    dp[l][j][i] %= mod
            # for _ in range(k):
            #     print(dp[l][_])
            # print("==================")
        return sum(dp[-1][-1]) % mod