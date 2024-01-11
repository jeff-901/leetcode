import heapq
class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        engineers = sorted(zip(efficiency, speed), reverse=True)
        total_speed = 0
        ans = 0
        worker_speed = []
        for i in range(k):
            total_speed += engineers[i][1]
            worker_speed.append(engineers[i][1])
            ans = max(ans, total_speed * engineers[i][0])
        heapq.heapify(worker_speed)
        for i in range(k, n):
            total_speed -= heapq.heappop(worker_speed)
            total_speed += engineers[i][1]
            heapq.heappush(worker_speed, engineers[i][1])
            ans = max(ans, total_speed * engineers[i][0])
        return ans % (10**9 +7)