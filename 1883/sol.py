class Solution(object):
    def minSkips(self, dist, speed, hoursBefore):
        """
        :type dist: List[int]
        :type speed: int
        :type hoursBefore: int
        :rtype: int
        """
        n = len(dist)
        target = hoursBefore * speed
        if sum(dist) > target:
            return -1
        dp = [0 for _ in range(n)]
        for d in dist:
            for skip in range(n-1, 0, -1):
                dp[skip] = min(dp[skip-1] + d, ((dp[skip] + speed - 1) // speed) * speed + d)
            dp[0] = ((dp[0] + speed - 1) // speed) * speed + d
        for i in range(n):
            if dp[i] <= target:
                return i
        return n - 1