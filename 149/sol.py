class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n == 1:
            return 1
        ans = 2
        for i in range(n):
            cnt = {}
            for j in range(i+1, n):
                if points[i][0] - points[j][0] == 0:
                    m = float("inf")
                else:
                    m = float(points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                if m in cnt:
                    cnt[m] += 1
                else:
                    cnt[m] = 2
            ans = max([ans] + list(cnt.values()))
        return ans