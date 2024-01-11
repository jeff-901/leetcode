class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m = len(nums1)
        n = len(nums2)
        dp = [0 for _ in range(n+1)]
        for i in range(m):
            last = dp[0]
            for j in range(n):
                tmp = dp[j+1]
                dp[j+1] = max(dp[j], dp[j+1], last + nums1[i] * nums2[j])
                last = tmp
        if dp[-1] == 0:
            a1, a2 = max(nums1), min(nums1)
            b1, b2 = max(nums2), min(nums2)
            return max(a1 * b2, a2 * b1)
        return dp[-1]