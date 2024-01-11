class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        dp = [0] * (len(arr) + 1)
        for i, num in enumerate(arr):
            cur_max = num
            best = 0
            for j in range(i, max(i-k, -1), -1):
                cur_max = max(cur_max, arr[j])
                best = max(best, dp[j] + cur_max * (i - j + 1))
            dp[i+1] = best
        return dp[-1]