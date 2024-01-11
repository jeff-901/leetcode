import heapq
class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        projects = sorted((zip(capital, profits)), reverse=True)
        available = []
        while(k > 0):
            while(projects and projects[-1][0] <= w):
                c, p = projects.pop()
                heapq.heappush(available, -p)
            if not available:
                break
            w += -heapq.heappop(available)
            k -= 1
        return w