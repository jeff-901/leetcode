class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        ans = 0
        for i in range(n):
            cnt = {}
            for j in range(n):
                if i == j:
                    pass
                d2 = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
                if d2 in cnt:
                    ans += cnt[d2]*2
                    cnt[d2] += 1
                else:
                    cnt[d2] = 1
        return ans