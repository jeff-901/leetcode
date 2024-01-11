class Solution(object):
    def largestSumOfAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        prefix = nums[:]
        for i in range(1, n):
            prefix[i] += prefix[i-1]
        dp = [[0 for _ in range(k)] for _ in range(n)]
        dp[0][0] = nums[0]
        for i in range(1, n):
            dp[i][0] = float(prefix[i]) / (i+1)
            for split in range(min(k-1, i)):
                val = 0
                for j in range(split, i):
                    val = max(val, dp[j][split] + float(prefix[i] -  prefix[j])/ (i-j))
                dp[i][split+1] = val
        return dp[-1][-1]

