class Solution(object):
    def maximumScore(self, nums, multipliers):
        """
        :type nums: List[int]
        :type multipliers: List[int]
        :rtype: int
        """
        m = len(multipliers)
        n = len(nums)
        left = n - m
        dp = [[0 for _ in range(m)] for _ in range(m)]
        for i in range(m):
            if multipliers[-1] > 0:
                dp[i][i] = max(nums[i], nums[i+left]) * multipliers[-1]
            else:
                dp[i][i] = min(nums[i], nums[i+left]) * multipliers[-1]
        for l in range(1, m):
            for i in range(m-l):
                j = i + l
                dp[i][j] = max(dp[i+1][j] + nums[i] * multipliers[-l-1], dp[i][j-1] + nums[j+left] * multipliers[-l-1])
        return dp[0][m-1]

