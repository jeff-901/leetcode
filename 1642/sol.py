import heapq
class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        min_hp = []
        n = len(heights)
        for i in range(1, n):
            diff = heights[i] - heights[i-1]
            if diff > 0:
                heapq.heappush(min_hp, diff)
                if len(min_hp) > ladders:
                    bricks -= heapq.heappop(min_hp)
                    if bricks < 0:
                        return i - 1
        return n - 1
                