class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        n = len(jobDifficulty)
        if n < d:
            return -1
        dp = [[0 for _ in range(d)] for _ in range(n)]
        dp[0][0] = jobDifficulty[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], jobDifficulty[i])
            for days in range(1, min(d, i+1)):
                max_num = jobDifficulty[i]
                val = dp[i-1][days-1] + max_num
                for j in range(i-1, days-1, -1):
                    max_num = max(max_num, jobDifficulty[j])
                    val = min(val, max_num + dp[j-1][days-1])
                dp[i][days] = val
        return dp[-1][-1]