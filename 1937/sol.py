class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        dp = points[0]
        m = len(points)
        n = len(points[0])
        for i in range(1, m):
            max_right = [0] * n
            last = dp[:]
            max_right[-1] = last[-1] - (n - 1)
            for j in range(n-2, -1, -1):
                max_right[j] = max(max_right[j+1], last[j] - j)
            max_left = -float("inf")
            for j in range(n):
                dp[j] = max(max_left - j, max_right[j] + j) + points[i][j]
                max_left = max(max_left, last[j] + j)       
        return max(dp)