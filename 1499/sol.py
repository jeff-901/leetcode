from collections import deque
class Solution(object):
    def findMaxValueOfEquation(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        dq = deque()
        ans = -float("inf")
        for i, (x, y) in enumerate(points):
            while dq and x - dq[0][0] > k:
                dq.popleft()
            if dq:
                ans = max(ans, x + y + dq[0][1])
            while(dq and dq[-1][1] <= y - x):
                dq.pop()
            dq.append((x, y - x))
        return ans