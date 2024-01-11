class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """
        left = 1
        right = 100 * max(dist)
        n = len(dist)
        if n - 1 >= hour:
            return -1
        while(left <= right):
            mid = (left + right) // 2
            t = 0
            for i in range(n-1):
                t += (dist[i] + mid - 1) // mid
            t += float(dist[-1]) / mid
            if t > hour:
                left = mid + 1
            else:
                right = mid - 1
        return left