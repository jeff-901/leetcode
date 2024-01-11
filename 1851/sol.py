import heapq
class Solution(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        
        n = len(intervals)
        intervals.sort()
        end_point = []
        res = {}
        interval_i = 0
        for q in sorted(queries):
            if q in res: continue
            while(interval_i < n and intervals[interval_i][0] <= q):
                heapq.heappush(end_point, \
                    (intervals[interval_i][1] - intervals[interval_i][0] + 1, \
                        intervals[interval_i][1]))
                interval_i += 1
            while(end_point and end_point[0][1] < q):
                heapq.heappop(end_point)
            res[q] = end_point[0][0] if end_point else -1
            
        return [res[q] for q in queries]

