class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [{} for _ in range(n)]
        ans = 2
        for i in range(1, n):
            num = nums[i]
            for j in range(i):
                diff = num - nums[j]
                dp[i][diff] = dp[j].get(diff, 1) + 1
            ans = max(ans, max(dp[i].values()))
        return ans