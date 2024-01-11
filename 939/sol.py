class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        seen = set()
        ans = float("inf")
        for x1, y1 in points:
            for x2, y2 in seen:
                if x1 == x2 or y1 == y2:
                    continue
                if (x1, y2) in seen and (x2, y1) in seen:
                    ans = min(ans, abs(x1 - x2)*abs(y1 - y2))
            seen.add((x1, y1))
        if ans == float("inf"):
            return 0
        return ans