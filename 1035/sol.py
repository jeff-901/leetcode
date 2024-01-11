class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m = len(nums1)
        n = len(nums2)
        dp = [0 for _ in range(n+1)]
        for i in range(m):
            last = dp[:]
            dp = [0 for _ in range(n+1)]
            for j in range(n):
                if nums1[i] == nums2[j]:
                    dp[j+1] = last[j] + 1
                else:
                    dp[j+1] = max(last[j+1], dp[j])
        return dp[-1]