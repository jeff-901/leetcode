class Solution(object):
    def countSpecialSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1, 0, 0, 0]
        for i in range(len(nums)):
            j = nums[i] + 1
            dp[j] = (dp[j] * 2 + dp[j-1]) % 1000000007
        return dp[3] % 1000000007