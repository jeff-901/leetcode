import heapq
class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        meetings.sort()
        available = []
        cnt = [0] * n
        for i in range(n):
            available.append((i, 0))
        used = []
        
        for start, end in meetings:
            while (used and used[0][0] <= start) or not available:
                end_time, num = heapq.heappop(used)
                heapq.heappush(available, (num, end_time))
            num, last_end_time = heapq.heappop(available)
            cnt[num] += 1
            heapq.heappush(used, (max(last_end_time + end - start, end), num))
        max_ = 0
        ans = 0
        for num in range(n):
            if cnt[num] > max_:
                max_ = cnt[num]
                ans = num
        return ans