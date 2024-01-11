import heapq
class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort(reverse=True)
        t = 0
        started = []
        ans = 0
        while(events or started):
            if not started:
                t = events[-1][0]
            while events and events[-1][0] <= t:
                heapq.heappush(started, events.pop()[1])
            heapq.heappop(started)
            ans += 1
            t += 1
            while(started and started[0] < t):
                heapq.heappop(started)
        return ans