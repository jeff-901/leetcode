import heapq
class Solution(object):
    def eatenApples(self, apples, days):
        """
        :type apples: List[int]
        :type days: List[int]
        :rtype: int
        """
        rotten = []
        ans = 0
        i = 0
        n = len(apples)
        while i < n or rotten:
            if i < n and apples[i] > 0:
                heapq.heappush(rotten, [days[i] + i, apples[i]])
            while rotten and (rotten[0][0] <= i or rotten[0][1] <= 0):
                heapq.heappop(rotten)
            if rotten:
                ans += 1
                rotten[0][1] -= 1 
            i += 1
        return ans